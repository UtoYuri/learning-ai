import os
from operator import itemgetter
from functools import reduce
from math import log

def create_dataset():
  """
  Desc:
    create data set
  Args:
    None
  Return:
    dataset and labels
  """
  with open(os.path.join(os.path.dirname(__file__), './data/lenses.txt')) as file:
    dataset = [line.strip().split('\t') for line in file.readlines()]
  labels = ['age', 'prescript', 'astigmatic', 'tearRate']
  return dataset, labels

def generate_decision_tree(dataset, labels):
  """
  Desc:
    generate decision tree
  Args:
    dataset
    labels
  Return:
    tree
  """
  classes = [sample[-1] for sample in dataset]
  if len(set(classes)) == 1:
    return classes[0]
  if len(labels) == 0:
    return major_class(classes)
  
  best_attribute_index, gain = select_best_attribute_by_entropy(dataset)
  best_attribute = labels[best_attribute_index]

  tree = {}
  tree[best_attribute] = {
    'gain': gain,
    'child': {},
  }

  attribute_values = set([sample[best_attribute_index] for sample in dataset])
  print(best_attribute)
  for value in attribute_values:
    samples = [sample for sample in dataset if sample[best_attribute_index] == value]
    if len(samples) == 0:
      tree[best_attribute]['child'][value] = major_class(classes)
    else:
      samples = list(map(lambda item: clone_array_except_index(item, best_attribute_index), samples))
      tree[best_attribute]['child'][value] = generate_decision_tree(samples, clone_array_except_index(labels, best_attribute_index))

  return tree

def select_best_attribute_by_entropy(dataset):
  attribute_count = len(dataset[0]) - 1

  max_gain, best_attribute_index = 0, -1
  for i in range(attribute_count):
    gain_value = gain(dataset, i)
    if gain_value > max_gain:
      max_gain = gain_value
      best_attribute_index = i

  return best_attribute_index, max_gain

def entropy(dataset):
  total_count = len(dataset)
  counts = {}
  for sample in dataset:
    class_name = sample[-1]
    counts[class_name] = counts.get(class_name, 0) + 1
  
  ent = 0
  for class_name in counts.keys():
    percent = counts[class_name] / total_count
    ent -= percent * log(percent, 2)
  return ent

def gain(dataset, attribute_index):
  splited_dataset = {}
  for sample in dataset:
    splited_dataset[sample[attribute_index]] = splited_dataset.get(sample[attribute_index], [])
    splited_dataset[sample[attribute_index]].append(sample)
  
  gain = entropy(dataset)
  for attribute_name in splited_dataset.keys():
    samples = splited_dataset[attribute_name]
    gain -= len(samples) / len(dataset) * entropy(samples)
  return gain

def major_class(classes):
  counts = {}
  for class_name in classes:
    counts[class_name] = counts.get(class_name, 0) + 1
  sorted_count = sorted(counts.items(), key=itemgetter(1), reverse=True)
  return sorted_count[0][0]

def clone_array_except_index(array, attribute_index):
  new_array = array.copy()
  new_array.pop(attribute_index)
  return new_array

def print_decision_tree(tree):
  import json
  print(json.dumps(tree))

if __name__ == "__main__":
  dataset, labels = create_dataset()
  tree = generate_decision_tree(dataset, labels)
  print_decision_tree(tree)
