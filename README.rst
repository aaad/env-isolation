Python Library env-isolation
========================================

The `env-isolation` is a library that allows to create isolated environments for running Python code. It is useful for seperating pip environments.

Note: The Library do not isolate the environments for security purposes.


Installation
~~~~~~~~~~~~

Install this library in a `venv`_ using pip. `venv`_ is a tool to
create isolated Python environments.

.. _`venv`: https://docs.python.org/3/library/venv.html


Supported Python Versions
^^^^^^^^^^^^^^^^^^^^^^^^^
Python >= 3.6

Mac/Linux
^^^^^^^^^

.. code-block:: console

    pip install venv
    python -m venv <your-env>
    source <your-env>/bin/activate
    <your-env>/bin/pip install env-isolation

Windows
^^^^^^^

.. code-block:: console

    pip install venv
    python -m venv <your-env>
    <your-env>\Scripts\activate
    <your-env>\Scripts\pip.exe install env-isolation

Example Usage
~~~~~~~~~~~~~

Create a directory `test-model` with a file `test-model/requirements.txt` with the following content:

.. code-block:: text

    pandas

Create a file `test-model/main.py` with the following content:

.. code-block:: python
    
    import logging
    import pandas as pd

    class Model():
        def __init__(self, arguments: dict):
            logging.info(f'Test Model initialised arguments: {arguments}')
            
        def execute(self, arguments: dict) -> dict:
            logging.info(f'Test Model executed with arguments: {arguments}')
            return pd.read_csv('test.csv').to_dict()

Execute the following code:

.. code-block:: python

    import logging
    logging.basicConfig(level=logging.INFO)
    from envisolation import EnvIsolatedModel

    model = EnvIsolatedModel(model_id="test-model", model_path="test_model", pip_requirements_path="test_model/requirements.txt", model_arguments={"test_argument":1})
    logging.info(model.execute({"input": "test"}))
    model.unload()