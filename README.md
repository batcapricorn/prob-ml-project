# Probablistic Machine Learning - Summer 2023 - Project
We apply Gaussian Processes to predict daily climate data.

## Quick Start

1. Start a `Jupyter` server by running `docker run -p 8888:8888 -v $(pwd):/home/jovyan/work jupyter/scipy-notebook`. Make sure you have `docker` up and running. Token-authentication is enabled, meaning you can access the application by opening `http://127.0.0.1:8888/lab?token=<YOUR_TOKEN>`. The URL, including your token, is displayed in your terminal.
2. Open `src/main.py` and explore our data analysis 🔥

## Developer Guide
### Setup
Install all dependencies
```
pip install --user pipenv
pipenv install --dev
```
Extract the corresponding virtual environment and adapt the corresponding configuration of your IDE:
```
pipenv --py
```

You should be good to go! 🐥 We use the [VS Code Jupyter Extension](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) to run our notebooks.

### Quality Guidelines
We use two main tools to assure code quality 😇
- [black](https://github.com/psf/black) for formatting: `pipenv run black src` 
- [pyint](https://pypi.org/project/pylint/) for linting: ` pipenv run pylint src`


Both is checked by a GitHub Actions pipeline (see `.github/workflows/build.yml`).