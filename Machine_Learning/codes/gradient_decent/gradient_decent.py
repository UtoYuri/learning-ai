import numpy as np
import matplotlib.pyplot as plt

x_data = [338, 333, 328, 207, 226, 25, 179, 60, 208, 606]
y_data = [640, 633, 619, 393, 428, 27, 193, 66, 226, 1591]

def gradient_decent():
  b = 0
  w = 0
  learning_rate = 1
  learning_round = 1000000

  b_learning_rate = 0
  w_learning_rate = 0

  b_history = [ b ]
  w_history = [ w ]

  for round_index in range(learning_round):
    b_gradient = 0
    w_gradient = 0

    for i in range(len(x_data)):
      b_gradient = b_gradient - 2 * (y_data[i] - w * x_data[i] - b)
      w_gradient = w_gradient - 2 * (y_data[i] - w * x_data[i] - b) * x_data[i]

    b_learning_rate = b_learning_rate + b_gradient ** 2
    w_learning_rate = w_learning_rate + w_gradient ** 2

    b = b - learning_rate / np.sqrt(b_learning_rate) * b_gradient
    w = w - learning_rate / np.sqrt(w_learning_rate) * w_gradient

    b_history.append(b)
    w_history.append(w)

  return b_history, w_history

def print_history(b_history, w_history):
  plt.plot(b_history, w_history, 'ro')
  plt.show();

if __name__ == "__main__":
    b_history, w_history = gradient_decent()
    print('b result ==> ', b_history[-1])
    print('w result ==> ', w_history[-1])
    print_history(b_history, w_history)