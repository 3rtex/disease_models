# Usage

If you have already set up your virtual env and your dependencies, just write the following commands, otherwise please consult the **Installation** section.

```
cd disease_models/

Mac/Linux: source venv/bin/activate
Windows :  C:\> <venv>\Scripts\activate.bat

jupyter notebook
```

Then you get redirected to your browser with the project tree structure, you can then select the folders and then the files you want to see (`.ipynb`). In the files you can run the cells, write markdown comments, etc. If you have errors, please `Restart & Run All` in the `Kernel` tab.

To leave the virtual env when you've finished to work.

```
deactivate
```


# Installation

## Prerequisites

You need to have git and python installed on your computer. Git permits you to interact with the disease project hosted on GitHub. Python is a programmatin language.

- Install Python from https://www.python.org or any package manager. (Project tested with 3.9)
- Install Git from https://git-scm.com/ or any package manager.

**Note:** In the following steps, we will install a virtual environment for Python. This step is optional, you could directly install the dependencies listed in the ```requirements.txt``` file globally. We do not recommend this, firstly because if you have several projects with different dependencies, you will have too many dependencies installed on your Python. The second reason is related to the versions of your Python. If you decide to upgrade the version of Python you are using, your old projects may not work anymore. With virtual environments, you won't have this problem since it makes a copy of the version of Python you want and won't update it if you upgrade your global Python.

## Steps

1. Install the project on your computer

```
git clone https://github.com/3rtex/disease_models.git
```

2. We are going to create a virtual environnement in the project to isolate the packages we will install for this project. A virtual environnement permits to keep your global Python clean.

```
cd disease_models/
python -m venv venv
```
3. Then you can connect to your python virtual environnement. You will have to activate the virtual env every time you want to use it. You can check you are in the virtual env with the "venv" added at the left of the path of your command line interface.

```
Mac/Linux: source venv/bin/activate
Windows :  C:\> <venv>\Scripts\activate.bat
```

4. Install dependencies needed for this project.

```
pip install -r requirements.txt
```

5. Try it out. This command will open your browser with the project tree structure. You can then go to the folder and open the `.ipynb` files and edit them.

```
jupyter notebook
```