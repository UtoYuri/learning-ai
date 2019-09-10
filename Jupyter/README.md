# Jupyter

## install
edit `jupyter_notebook_config.py`, reset `c.NotebookApp.password`.
default password is `abc123_`
```
docker-compose up -d
```

## usage
open `http://localhost:10000` in browser and log in.

## Tips
to install packages
```bash
$ docker exec -it jupyter sh
# in container
$ pip install <package>
```
