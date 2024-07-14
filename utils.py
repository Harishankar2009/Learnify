import yaml
import logging
import logging.config


def load_config(config_path = 'config/config.yaml'):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def setup_logging(logging_config_path = ' config/logging.yaml'):
    with open(logging_config_path, 'r') as file:
        logging_config = yaml.safe_load(file)
        logging.config.dictConfig(logging_config)
    logger = logging.getLogger(__name__)
    return logger 
