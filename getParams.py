import yaml

def get_params():
    f = open("config.yaml")
    config = yaml.load(f)
    return config
