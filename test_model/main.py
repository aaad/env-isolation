import logging
import pandas as pd

class Model():
    def __init__(self):
        logging.info('Test Model initialised')
        
    def execute(self, arguments: dict) -> dict:
        logging.info(f'Test Model executed with arguments: {arguments}')
        return pd.read_csv('test.csv').to_dict()