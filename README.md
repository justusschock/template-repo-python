## <span style="color:red">*What to maintain*</span>

<div align="center">

![Logo](docs/source/_images/logos/PACKAGE_NAME_logo.svg)

# REPONAME

**This repository contains a fully-functionable package structure including (empty) tests..**

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="https://PACKAGE_NAME.readthedocs.io/en/stable/">Docs</a> •
  <a href="#examples">Examples</a> •
  <!-- <a href="#community">Community</a> • -->
  <a href="#licence">Licence</a>
</p>

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/PACKAGE_NAME)](https://pypi.org/project/PACKAGE_NAME)
[![PyPI Package Version](https://badge.fury.io/py/PACKAGE_NAME.svg)](https://badge.fury.io/py/PACKAGE_NAME)
[![image](https://img.shields.io/pypi/v/PACKAGE_NAME)](https://pypi.org/project/PACKAGE_NAME)
[![PyPI Status](https://pepy.tech/badge/PACKAGE_NAME)](https://pepy.tech/project/PACKAGE_NAME)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/PACKAGE_NAME)](https://pypi.org/project/PACKAGE_NAME)

[![DockerHub](https://img.shields.io/docker/pulls/AUTHOR_NAME/PACKAGE_NAME.svg)](https://hub.docker.com/r/AUTHOR_NAME/PACKAGE_NAME)

[![codecov](https://codecov.io/gh/AUTHOR_NAME/REPONAME/branch/master/graph/badge.svg)](https://codecov.io/gh/AUTHOR_NAME/PACKAGE_NAME)
[![image](https://img.shields.io/codecov/c/github/AUTHOR_NAME/REPONAME)](https://codecov.io/gh/AUTHOR_NAME/REPONAME)

[![image](https://img.shields.io/github/workflow/status/AUTHOR_NAME/REPONAME/python-3.6?label=python%203.6)](https://github.com/GITHUB_NAME/REPONAME/actions)
[![image](https://img.shields.io/github/workflow/status/AUTHOR_NAME/REPONAME/python-3.7?label=python%203.7)](https://github.com/GITHUB_NAME/REPONAME/actions)
[![image](https://img.shields.io/pypi/status/REPONAME)](https://pypi.org/project/REPONAME)

[![ReadTheDocs](https://readthedocs.org/projects/PACKAGE_NAME/badge/?version=stable)](https://PACKAGE_NAME.readthedocs.io/en/stable/)
[![Slack](https://img.shields.io/badge/slack-chat-green.svg?logo=slack)](https://join.slack.com/t/PACKAGE_NAME/shared_invite/zt-f6bl2l0l-JYMK3tbAgAmGRrlNr00f1A)
[![Discourse status](https://img.shields.io/discourse/status?server=https%3A%2F%2Fforums.AUTHOR_NAME.ai)](https://forums.AUTHOR_NAME.ai/)
[![license](https://img.shields.io/badge/License-LICENSE-blue.svg)](https://github.com/GITHUB_NAME/REPONAME/blob/master/LICENSE)
[![Next Release](https://img.shields.io/badge/Next%20Release-Jan-Dec%20xx-<COLOR>.svg)](https://shields.io/)


[![image](https://img.shields.io/pypi/implementation/PACKAGE_NAME)](https://pypi.org/project/PACKAGE_NAME)

[![image](https://img.shields.io/snyk/vulnerabilities/github/AUTHOR_NAME/PACKAGE_NAME)](https://github.com/GITHUB_NAME/REPONAME/network/alerts)

[![image](https://img.shields.io/github/v/tag/AUTHOR_NAME/PACKAGE_NAME)](https://github.com/GITHUB_NAME/REPONAME/releases)

</div>

---

## How To Use

### Step 0: Install locally

```bash
# clone project
git clone https://github.com/GITHUB_NAME/REPONAME.git

# install project
cd PACKAGE_NAME
pip install .
pip install -r requirements.txt
```

### Step 0: Install from remote

Simple installation from PyPI

```bash
pip install PACKAGE_NAME
```

From Conda

```bash
conda install PACKAGE_NAME -c conda-forge
```

### Step 1: ...

Describe step 1

```python
Python examples
```

### Step 2: ...

Describe step 1

```python
Python examples
```

---

## Examples

###### Hello world

[hello world example](url)

###### Example category 2

[example 1](url)

[example 2](url)

---

## Asking for help

If you have any questions please:

1. [Read the docs](https://PACKAGE_NAME.rtfd.io/en/latest/).
1. [Look it up in our forum (or add a new question)](https://forums.PACKAGE_NAME.ai/)
1. [Search through the issues](https://github.com/GITHUB_NAME/REPONAME/issues?utf8=%E2%9C%93&q=my++question).
1. [Join our slack](https://join.slack.com/t/PACKAGE_NAME/shared_invite/zt-f6bl2l0l-JYMK3tbAgAmGRrlNr00f1A).
1. [Ask on stackoverflow](https://stackoverflow.com/questions/ask?guided=false) with the tag PACKAGE_NAME.

---

## Licence

Please observe the LICENSE license that is listed in this repository.

## BibTeX

If you want to cite the framework feel free to use this:

```bibtex
@article{ARTICLE_NAME,
 title={TITLE},
 author={AUTHOR_NAME},
 journal={GitHub. Note: https://github.com/GITHUB_NAME/REPONAME},
 volume={VOLUME},
 year={YEAR}
}
```

<hr style="border:2px solid green"> </hr>


## <span style="color:red">*Info about this template*</span>

## Template Content

It's features include (but are not limited to):

* An already working package structure
* A working requirement handling
* Minimal effort PyPI releases
* Pre-Configured CI/CD (With Github Actions or CircleCI)
* Code coverage analysis
* Python Code Style Checks

> If you want to add something to this repo, please submit a PR. Contributions are very welcome.

<hr style="border:2px solid green"> </hr>

## <span style="color:red">*What to change*</span>


## Customize it!

To customize this repo, you need to have a look at the following chapters.

### Directory-Name

You might want to customize your package-name.

To do this, you simply have to rename the `template-repo` directory to whatever you want.
> Make sure, to also change it in [line 32 of your setup.py](setup.py#L32), or you won't be able to install your package anymore!

### Python Package Metadata

To customize your python package, you just have to change your `setup.py`.

Currently the important part looks like

```python
setup(
    name='template_package',
    version=_version,
    packages=find_packages(),
    url='https://github.com/FlorianFM/template-repo-python',
    test_suite="unittest",
    long_description=readme,
    long_description_content_type='text/markdown',
    install_requires=requirements,
    tests_require=["coverage"],
    python_requires=">=3.5",
    author="Florian Müller-Fouarge",
    author_email="florian.mueller.fouarge@gmail.com",
    license=license,
)
```

This includes the default information for me and must be adjusted to your needs:

* `name` provides the package-name you can later import
* `version` provides the package-version (which will currently be extracted from your package's `__init__.py`, but be also set manually)
* `packages` is a list defining all packages (and their sub-packages and the sub-packages of their sub-packages and so on...), that should be installed. This is automatically extracted by `find_packages`, which also accepts some sub-packages to ignore (besides some other arguments).
* `url` specifies the packages homepage (in this case the current GitHub repo); You might want to change it to your repos homepage.
* `test_suite` defines the test-suite to use for your unittests. In this repo template, we'll python's built-in framework `unittest`, but you can change this too; *Just make sure to also change this, when we get to CI/CD.*
* `long_description` does what it sayes: It provides a long description of your package. Currently this is parsed from your `README.md`
* `long_description_content_type` defines your description type; I set it to markdown in most cases
* `install_requires` is a list containing all your package requirements. They are automatically parsed from a `requirements.txt` file
* `tests_require` does the same thing for your unittests.
* `python_requires` specifies the python version, your package can be installed to (here it's been set to python 3.5 or above, since this is what I usually use). *Depending on the version you specify here, you might not be able to use all of python's latest features*
* `author` and `author_email` specify who you are.
* `license` specifies the license you want to release your code with. This is parsed from a `LICENSE` file.

There are still many other options to include here, but these are the most basic ones.

### Unittests

If you want to add/change some unit-tests, you should do this in a new python file starting with `test_`. [Here](https://docs.python.org/3/library/unittest.html) is a good introduction on how to write unittests with the `unittest` framework. After you added these tests, you may run them with either `coverage run -m unittest` or `python -m unittest`.

They are basically doing the same, but `coverage` additionally checks, how many of your code-lines are currently covered by your tests.

The unittests are also automatically triggered within [CI/CD](#cicd)

### Specifying Codecov

The [`.codecov.yml`](.codecov.yml) file specifies, how coverage should behave, how to calculate the coverage (i.e. what files to include for line counting) etc.

### Requirements

If you want to add new requirements, simply add them to the [`requirements/install.txt`](requirements/install.txt) file.

### Packaging on PyPi

If you plan to release your package on pypi, ship wheels for it, you might need the [`MANIFEST.in`](MANIFEST.in) file, since it specifies (among other things), which files to include to your binaries.

### Setup.cfg

The [`setup.cfg`](setup.cfg) file currently only specifies, which directories to exclude from style checking.

### Gitignore

The `.gitignore` file is a real life saver. It prevents files and directories that match certain patterns from being added to your git repository, when you push new stuff to it. You may append more specific patterns [here](.gitignore#L109).

### CI/CD

Now, we talked a lot about CI/CD. This repository uses [`travis`](https://travis-ci.com) as CI/CD and per default simply runs tests and style checks for your code.

To use this feature, you have to enable travis for your repository.

#### YAML-Specifications

The [`.travis.yml`](.travis.yml) file specifies the CI/CD behavior. Currently it only runs tests and style-checks with Python 3.7 on Linux Xenial. You may also include additional cases to the test matrix or add deployment (e.g. deploying your docs to GitHub Pages or similar stuff).

#### Scripts

The scripts used b CI/CD to install the requirements and run your tests are lying at [`scripts/ci`](scripts/ci).
The file names indicate pretty well, what tey're doing. Of course you can customize them too.

If you want Travis to automatically fix your code style where possible you have to add a github access token to travis, comment in the [lines 6-28](scripts/ci/run_style_checks.sh#L6-L28) and change the environment variable and the repository in [line 27](scripts/ci/run_style_checks.sh#L27).

