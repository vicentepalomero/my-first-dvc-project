# my-first-dvc-project

## set up

### 1. Fork / Clone this repo

```bash
git clone git@github.com:vicentepalomero/my-first-dvc-project.git
cd my-first-dvc-project
```

### 2. Create and activate the virtual environment

Creating a virtual environment `env`
```bash
virtualenv env
source env/bin/activate
```

Install python libraries
```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

Add virtual environment to Jupyter Notebook
```bash
python -m ipykernel install --user --name=env
```

Configure ToC for jupyter notebook (optional)

```bash
jupyter contrib nbextension install --user
jupyter nbextension enable toc2/main
```

### 3. Run Jupyter Notebook
```bash
jupyter notebook
```

## Other configuration
Use Cookiecutter data sciente template
```bash
pip install cookiecutter
cookiecutter https://github.com/drivendata/cookiecutter-data-science
```

## Steps to convert a raw, ugly Notebook into a beautiful file.
### params.yaml
* Create a params.yaml file with four categories: base, data, train, reports
* In the Notebook, import yaml and %cd .. to set the path into the same folder than params.yaml
* safe_load the params.yaml into a config variable
* Move the variables into the params.yaml file

### visualization code
* Copy the code of the function into a src/visualization/visualize.py file (or another similar)
* change the code in the notebook for a `from src.visualization.visualize import plot_confusion_matrix`
