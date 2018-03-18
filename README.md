# Twitter monitor Application

written on [Python 3](https://www.python.org/download/releases/3.0/) 

## Infrastructure dependencies

pylint==1.7.4
TwitterAPI==2.5.0
argparse
PyQt5
PyQtGraph

## Configurations

Configurations Secrets can be set via Environment Variables.

file activate has demo account use it 'source ./activate'

## Building, testing and running

Install dependenies:
```
pip install --no-cache-dir -r requirements.txt
```

To run tests:
```
PYTHONPATH=$PYTHONPATH:$(pwd) python -m unittest discover -v tests
```

To start application:
```
PYTHONPATH=$PYTHONPATH:$(pwd) python apps/twitter_app.py --sentence "Samsung"
```

## Folders structures
* apps - contains applications that can be executed
* config - contains configuration related code
* generic_components - contains single responsibility testable components.
* ioc - (inversion of control) single place for instantiating classes, building complex components.
* tests - self explained
