import srsly
import os

prod_file = '/prod.json'
dir_path =os.path.dirname(os.path.realpath(__file__))
config_file  =fr'{dir_path}/{prod_file}'
config = srsly.read_json(config_file)

DB_PROD_URL = config.get("DB_PROD_URL")
