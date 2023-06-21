# Probablistic Machine Learning - Summer 2023 - Project
We apply Gaussian Processes to predict daily climate data.

## Quick Start

### Google Colab
Discover our notebooks using [Google Colab](https://colab.research.google.com/?utm_source=scs-index):
- [Basics of Gaussian Processes](https://colab.research.google.com/github/batcapricorn/prob-ml-project/blob/main/src/GP_Background.ipynb)
- [Main Analysis](https://colab.research.google.com/github/batcapricorn/prob-ml-project/blob/main/src/GP_Main.ipynb)

### Local Setup
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
- [pylint](https://pypi.org/project/pylint/) for linting: `pipenv run pylint src`

Both is checked by a GitHub Actions pipeline (see `.github/workflows/build.yml`). If you work with Jupyter Notebooks, checkout [nbAQ](https://nbqa.readthedocs.io/en/latest/).

### Versioning
Since comparing pull requests can be quite tricky using Jupyter Notebooks, we use [reviewNB](https://www.reviewnb.com/) to display diffs.