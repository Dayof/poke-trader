Table of Contents
=================

1. [Contributing](#contributing)
2. [System Requirements](#system-requirements)
3. [App Requirements](#app-requirements)
4. [Repository Contribution](#repository-contribution)
5. [Testing](#testing)
6. [Code Coverage](#code-coverage)
7. [Code Style](#code-style)
8. [Linter](#linter)
9. [Author](#author)


Contributing
------------

To contribute with `Poke Trader` follow the guidelines below. Try not to run away from any step below, otherwise you will have problems with the installation and standardization of this package.


System Requirements
-------------------

- Python >= 3.6
- MongoDB >= 3.6.8


App Requirements
----------------

- Setup development environment

```bash
python -m venv venv
source venv/bin/activate
(venv) pip install -U pip  # update pip version to retrieve up to date lib versions
(venv) pip install -e .[dev]
```

- Addition of new libraries into this package

Insert your new library inside of [setup.py](setup.py) file, choose the appropriate list,
e.g. a production library goes into:

```python
prod = [..., 'new_library']
```


Repository Contribution
-----------------------

1. Create a issue with a feature or bug.
2. Fork the project into your own repository and create a branch called ``feature/[feature]``, where *feature* is the name of the feature that you are working on.
3. Update the branch ``feature/[feature]`` and send commits with the number of your issue at the message, e.g.:
  ```bash
  git commit -m "solves commit #5"
  ```
4. Run tests to check if everything is working fine (more information about how to run the tests in the section below).
5. After run the tests and passed all of them, push your modifications and send a *PR* (Pull Resquest) to master.


Testing
-------

This project has both unit and integration tests. They have same setup but a different way of running them:


- Running unit tests:

  ```bash
  pytest tests/unit
  ```

- Running integrations tests

  ```bash
  pytest tests/integration
  ```

Code Coverage
-------------

```bash
pytest -vv tests/integration tests/unit --cov=src --cov=src/collector --cov=src/routers --cov=src/service --cov-report xml:coverage-reports/pytest-coverage-report-int.xml --junitxml=xunit-reports/xunit-result-pytest-int.xml --cov-report=html
```

Code Style
----------

Use `Google Style Python Docstrings` for comments, e.g.:

```python
def function_with_types_in_docstring(param1, param2):
    """Example function with types documented in the docstring.

    `PEP 484`_ type annotations are supported. If attribute, parameter, and
    return types are annotated according to `PEP 484`_, they do not need to be
    included in the docstring:

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    Returns:
        bool: The return value. True for success, False otherwise.

    .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/

    """
```

Linter
------

To automate import sorting and check for PEP8 problems:

```bash
isort --atomic --skip venv .  # recursively modify files conform import sorting guidelines, skipping virtual environment folder
pycodestyle . # check for pep8 standards
bandit -r src  # test python security analysis
```

`[OPTIONAL]` Install a [pre-commit hook](https://raw.githubusercontent.com/cbrueffer/pep8-git-hook/master/pre-commit) to check pep8 errors before every commit. The hook can be overridden: `git commit --no-verify`.

```bash
wget https://raw.githubusercontent.com/cbrueffer/pep8-git-hook/master/pre-commit && mv pre-commit .git/hooks/ && chmod +x .git/hooks/pre-commit
```


Author
------

- Dayanne Fernandes:
  - Github : [@Dayof](https://github.com/Dayof)
  - E-mail : dayannefernandesc@gmail.com
