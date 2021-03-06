# Wardoff

[![Build Status](https://travis-ci.org/4383/wardoff.svg?branch=master)](https://travis-ci.org/4383/wardoff)
![PyPI](https://img.shields.io/pypi/v/wardoff.svg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/wardoff.svg)
![PyPI - Status](https://img.shields.io/pypi/status/wardoff.svg)
[![Downloads](https://img.shields.io/pypi/dm/wardoff.svg)](https://pypi.python.org/pypi/wardoff/)

Wardoff (pronounced `ward off`) aim to help you to maintain your code base
clean and up-to-date by reducing the pain of collect informations about all
your underlaying libraries in your stack in a proactively manner.

Wardoff grab for you many informations about your stacks, it can be used to:
- looking for deprecated stuffs in project requirements and underlying
- grab requirements' infos (detailed or not) (cf. see the examples in the `infos` section)
- convert source code into python token

For each analyze a dedicated python virtual environment is built and project's
requirements are installed within. Then installed source code files of
project's requirement are analyzed one by one.

Code analyze of the requirements is based on
[AST](https://docs.python.org/3/library/ast.html) and
[python tokens](https://docs.python.org/3/library/tokenize.html). Each
source code file of each underlaying library is analyzed in this way.

You can pass a list of constraints to apply to your analyze to be sure
to match the right versions of your underlaying libraries.

Traditionally projects maintainers are informed that functions will become
deprecated or removed by reading documentation or by
observing deprecation warning at the runtime in logs. When your stack
grow and the number of requirements in your stack increase it could be
painful to stay up-to-date, wardoff aim to collect for you all these infos
by using only 1 command without needing any runtime environment setup.

## Install

Still in development and really unstable, however you can install unstable
development versions by using:

```shell
$ python3 -m pip install --user wardoff
```

## Requirements

- python3.8+
- git

## Usages

### Looking for deprecated things in stacks

The main goal here is to analyze all requirements of a given project
to extract deprecated things from their codes.

#### From a named package

Found deprecated things from a named package (directly from pypi):

```sh
$ wardoff niet # will list all deprecations founds in niet is requirements
$ wardoff oslo.messaging # will list all deprecations founds in oslo.messaging is requirements
$ wardoff oslo.messaging==12.2.2 # will list all deprecations founds in oslo.messaging 12.2.2 is requirements
$ wardoff oslo.messaging==1.3.0 # will list all deprecations founds in oslo.messaging 1.3.0 is requirements
```

#### From the current directory

Retrieve deprecated things from the current working directory.

Retrieve requirements from:
- `requirements.txt`
- `test-requirements.txt`
- `*-requirements.txt`
- `**/*requirements.txt`

Example:

```sh
$ wardoff # will list all deprecations founds in requirements founds in current directory
```

#### From a local repository

Retrieve deprecated things from a distgit repo.

Retrieve requirements from:
- `requirements.txt`
- `test-requirements.txt`
- `*-requirements.txt`
- `**/*requirements.txt`

Example:

```sh
$ wardoff ~/dev/nova # from a local clone of openstack/nova
```

#### From a distant repository

*(Coming soon - not yet implemented)*

Retrieve deprecated things from a distgit repo.

Example:

```sh
$ wardoff https://opendev.org/openstack/nova/ # from opendev.org
$ wardoff https://github.com/openstack/nova # from github.com
$ wardoff git@github.com:openstack/nova # by using git format
```


### tokenizer

Wardoff provide a CLI tokenizer which can be used against code passed through
the CLI or by passing a file path and a specific line to read.

Example with raw code passed through the CLI:

```sh
$ wardoff-tokenizer "def person(name, age):"
TokenInfo(type=62 (ENCODING), string='utf-8', start=(0, 0), end=(0, 0), line='')
TokenInfo(type=1 (NAME), string='def', start=(1, 0), end=(1, 3), line='def person(name, age):')
TokenInfo(type=1 (NAME), string='person', start=(1, 4), end=(1, 10), line='def person(name, age):')
TokenInfo(type=54 (OP), string='(', start=(1, 10), end=(1, 11), line='def person(name, age):')
TokenInfo(type=1 (NAME), string='name', start=(1, 11), end=(1, 15), line='def person(name, age):')
TokenInfo(type=54 (OP), string=',', start=(1, 15), end=(1, 16), line='def person(name, age):')
TokenInfo(type=1 (NAME), string='age', start=(1, 17), end=(1, 20), line='def person(name, age):')
TokenInfo(type=54 (OP), string=')', start=(1, 20), end=(1, 21), line='def person(name, age):')
TokenInfo(type=54 (OP), string=':', start=(1, 21), end=(1, 22), line='def person(name, age):')
TokenInfo(type=4 (NEWLINE), string='', start=(1, 22), end=(1, 23), line='')
TokenInfo(type=0 (ENDMARKER), string='', start=(2, 0), end=(2, 0), line='')
```

Another example by passing a file line to tokenize:

```sh
wardoff-tokenizer ~/dev/wardoff/wardoff/tokenizer.py+12
```

It will tokenize the line number 12 of the file
`~/dev/wardoff/wardoff/tokenizer.py`

For further options with this command:

```sh
$ wardoff-tokenizer -h
```

### infos

Wardoff allow you to retrieve infos of all your requirements. It will provide
a similar output than `pip show` but it will print all the requirements
related the given package. Returned output also contains the pypi classifiers
and also some useful infos that are not returned by `pip show`.
You can see that command as an advanced `pip show` where you can apply
different kinds of filters (cf. examples bellow)

Examples:

```sh
$ wardoff-infos oslo.cache
-----
name: certifi
version: 2020.6.20
sources_path: /tmp/wardoff-25781/lib/python3.8/site-packages/certifi
summary: Python package for providing Mozilla's CA Bundle.
home-page: https//certifiio.readthedocs.io/en/latest/
author: Kenneth Reitz
author-email: me@kennethreitz.com
license: MPL-2.0
location: /tmp/wardoff-25781/lib/python3.8/site-packages
requires:
required-by: requests
Development Status :: 5 - Production/Stable
Intended Audience :: Developers
License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)
Natural Language :: English
Programming Language :: Python
Programming Language :: Python :: 3
Programming Language :: Python :: 3.3
Programming Language :: Python :: 3.4
Programming Language :: Python :: 3.5
Programming Language :: Python :: 3.6
Programming Language :: Python :: 3.7
Programming Language :: Python :: 3.8
-----
name: chardet
version: 3.0.4
sources_path: /tmp/wardoff-25781/lib/python3.8/site-packages/chardet
summary: Universal encoding detector for Python 2 and 3
home-page: https//github.com/chardet/chardet
author: Daniel Blanchard
author-email: dan.blanchard@gmail.com
license: LGPL
location: /tmp/wardoff-25781/lib/python3.8/site-packages
requires:
required-by: requests
Development Status :: 4 - Beta
Intended Audience :: Developers
License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)
Operating System :: OS Independent
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.3
Programming Language :: Python :: 3.4
Programming Language :: Python :: 3.5
Programming Language :: Python :: 3.6
Topic :: Software Development :: Libraries :: Python Modules
Topic :: Text Processing :: Linguistic
-----
...
```

Previously, packages infos and classifiers have been displayed, in this way
by example it could allow you to find which package doesn't support specific
python version.

Moreover you can use `wardoff-infos` to grab more informations than that,
by example you can retrieve all the projects home pages of your stack:

```sh
$ wardoff-infos oslo.cache --keep-env --filter home-page --no-separator --no-key
https//certifiio.readthedocs.io/en/latest/
https//github.com/chardet/chardet
https//docs.openstack.org/debtcollector/latest
https//github.com/micheles/decorator
https//github.com/sqlalchemy/dogpile.cache
https//github.com/kjd/idna
https//bitbucket.org/micktwomey/pyiso8601
https//msgpack.org/
https//github.com/drkjam/netaddr/
https//github.com/al45tair/netifaces
https//docs.openstack.org/oslo.config/latest/
https//docs.openstack.org/oslo.context/latest/
https//docs.openstack.org/oslo.i18n/latest
https//docs.openstack.org/oslo.log/latest
https//docs.openstack.org/oslo.serialization/latest/
https//docs.openstack.org/oslo.utils/latest/
https//github.com/pypa/packaging
https//docs.openstack.org/pbr/latest/
http//github.com/seb-m/pyinotify
https//github.com/pyparsing/pyparsing/
https//dateutil.readthedocs.io
http//pythonhosted.org/pytz
https//github.com/yaml/pyyaml
https//requests.readthedocs.io
http//rfc3986.readthedocs.io
https//github.com/benjaminp/six
https//docs.openstack.org/stevedore/latest/
https//urllib3.readthedocs.io/
https//github.com/GrahamDumpleton/wrapt
```

Or retrieve who are the main maintainers of the analyzed stack
(here in oslo.cache):

```sh
$ wardoff-infos oslo.cache --filter author --no-separator --no-key | sort | uniq
Alastair Houghton
Andrey Petrov
Benjamin Peterson
Daniel Blanchard
David P. D. Moss, Stefan Nordhausen et al
Donald Stufft and individual contributors
Graham Dumpleton
Gustavo Niemeyer
Ian Stapleton Cordasco
Inada Naoki
Kenneth Reitz
Kim Davies
Kirill Simonov
Michael Twomey
Michele Simionato
Mike Bayer
OpenStack
Paul McGuire
Sebastien Martini
Stuart Bishop
```

Another useful option is the `--support` option that allow you to retrieve
project that only support specific versions of python. You can mix supported
version by example to retrieve the project's requirements that support the
given versions, example:

```sh
$ wardoff-infos oslo.cache --no-separator --support 2.7,3.4 --filter name --no-key
chardet
decorator
idna
netifaces
packaging
pyinotify
pyparsing
pytz
rfc3986
wrapt
```

The previous example looking for requirements who still support python 2.7 and
3.4 in the same time, displayed results match this condition.

Here is another example:

```sh
$ wardoff-infos oslo.cache --no-separator --support 3.7,3.8 --filter name --no-key
certifi
idna
msgpack
netaddr
oslo.config
oslo.context
oslo.i18n
oslo.log
oslo.serialization
packaging
pyparsing
PyYAML
requests
urllib3
wrapt
```

This kind of filter can be used to focus some of your developments or works
on specific versions of python.

### freeze

Wardoff allow you to freeze installed requirements. It will provide a similar
output than `pip freeze` but it will only print requirements related the given
package.

Example:

```
$ wardoff-freeze oslo.messaging==1.3.0
amqp==2.6.0
Babel==2.8.0
certifi==2020.6.20
chardet==3.0.4
debtcollector==2.2.0
dnspython==2.0.0
eventlet==0.25.2
greenlet==0.4.16
idna==2.10
iso8601==0.1.12
kombu==4.6.11
monotonic==1.5
netaddr==0.8.0
oslo.config==8.3.1
oslo.i18n==5.0.0
pbr==5.4.5
pytz==2020.1
PyYAML==5.3.1
requests==2.24.0
rfc3986==1.4.0
six==1.15.0
stevedore==3.2.0
urllib3==1.25.10
vine==1.3.0
wrapt==1.12.1
```

## Wardoff's environment

To works wardoff generate environment on your laptop, you can name
and reuse them. All the generated environment can be conserved by passing
`--keep-env`or destroyed
(by default the current generated environment is destroyed at each execution).

You can list your environments by using `wardoff-list-env` or simply remove
all of them by using `--wardoff-rm-env`.

If you pass a name at your command and if this environment already exist then
it will be reused, example:

```sh
$ wardoff-freeze ~/dev/redhat/upstream/openstack/oslo/oslo.cache --ignore-extra-req --keep-env --env oslo-cache -vvv
INFO: Reusing an existing environment /tmp/wardoff-oslo-cache
certifi==2020.6.20
chardet==3.0.4
debtcollector==2.2.0
decorator==4.4.2
dogpile.cache==1.0.1
idna==2.10
iso8601==0.1.12
msgpack==1.0.0
netaddr==0.8.0
netifaces==0.10.9
oslo.config==8.3.1
oslo.context==3.1.0
oslo.i18n==5.0.0
oslo.log==4.3.0
oslo.serialization==4.0.0
oslo.utils==4.4.0
packaging==20.4
pbr==5.4.5
pyinotify==0.9.6
pyparsing==2.4.7
python-dateutil==2.8.1
pytz==2020.1
PyYAML==5.3.1
requests==2.24.0
rfc3986==1.4.0
six==1.15.0
stevedore==3.2.0
urllib3==1.25.10
wrapt==1.12.1
```

In the previous command we reused an existing environment called `oslo-cache`
and we ask to keep this one at the end of our command to reusing it again. If
this environment doesn't exist it will created automatically.

## Output's Verbosity

You can increase the output verbosity on all your commands by passing the `-v`
option. The `v` you pass the more the verbosity will be increased. By example
`-vvv` will display logs error, warn, info, and debug.

This option could be useful to debug some situations and observe what's
happening.

## The future of wardoff

We plan to introduce more features like issues and pull requests or
patches harvesting.
