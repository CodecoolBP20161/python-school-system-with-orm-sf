import json


class Config():
    config_file = 'config.json'

    @classmethod
    def load(cls, key):
        try:
            with open(cls.config_file, 'r') as f:
                config = json.load(f)
                return config[key]
        except KeyError or ValueError as e:
            print("No such config option!", e)
