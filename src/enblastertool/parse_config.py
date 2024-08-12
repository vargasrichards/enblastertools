'''
Safely reads in a config file in yaml format
09.08.2024, A. Vargas Richards
'''
import yaml

def parse_config():
    return yaml.safe_load('config.yaml')

print(parse_config())