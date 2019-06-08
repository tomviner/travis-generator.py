<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/travis-generator.svg?longCache=True)](https://pypi.org/project/travis-generator/)
[![](https://img.shields.io/pypi/v/travis-generator.svg?maxAge=3600)](https://pypi.org/project/travis-generator/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/travis-generator.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/travis-generator.py/)

#### Installation
```bash
$ [sudo] pip install travis-generator
```

#### Features
+   `travis_generator.Travis` generator class
    +   `.travis.yml` keys support
    +   python versions from classifiers

#### Classes
class|`__doc__`
-|-
`travis_generator.Classifiers` |python classifiers class
`travis_generator.Travis` |`.travis.yml` generator class

#### Functions
function|`__doc__`
-|-
`travis_generator.dump(data)` |dump a dictionary to a YAML document string
`travis_generator.load(path='.travis.yml')` |return a dictonary with `.travis.yml` data
`travis_generator.quote(value)` |return a double quoted string
`travis_generator.save(data, path='.travis.yml')` |save a dictionary to a file

#### Examples
classifiers
```bash
$ python setup.py --classifiers
Programming Language :: Python
Programming Language :: Python :: 3.4
Programming Language :: Python :: 3.5
Programming Language :: Python :: 3.6
Programming Language :: Python :: 3.7
```

```python
import travis_generator
class Travis(travis_generator.Travis):
    install = "curl -fLs https://git.io/<xxx> | bash -s"
    script = "curl -fLs https://git.io/<yyy> | bash -s"

Travis().save()
```

```bash
$ cat .travis.yml
language: python
python:
- "3.4"
- "3.5"
- "3.6"
- "3.7"
install: curl -fLs https://git.io/<xxx> | bash -s
script: curl -fLs https://git.io/<yyy> | bash -s
```

#### Related projects
+   [`classifiers-generator` - python classifiers generator](https://pypi.org/project/classifiers-generator/)
+   [`commands-generator` - shell commands generator](https://pypi.org/project/commands-generator/)
+   [`launchd-generator` - launchd.plist generator](https://pypi.org/project/launchd-generator/)
+   [`readme-generator` - `README.md` generator](https://pypi.org/project/readme-generator/)
+   [`setupcfg-generator` - `setup.cfg` generator](https://pypi.org/project/setupcfg-generator/)
+   [`travis-generator` - `.travis.yml` generator](https://pypi.org/project/travis-generator/)
+   [`travis-exec` - execute command for all travis repos](https://pypi.org/project/travis-exec/)
+   [`travis-cron` - manage travis cron](https://pypi.org/project/travis-cron/)
+   [`travis-env` - manage travis environment variables](https://pypi.org/project/travis-env/)

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>