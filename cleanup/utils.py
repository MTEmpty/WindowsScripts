import json
import time


def get_config():
    with open('config.json', 'r') as f:
        # print('This is what I am getting', f.read())
        config = json.load(f)
    return config


def get_cleanup_targets(config):
    path_to_config = config.get('config_path')
    print('Getting list of targets from:', path_to_config)
    with open(path_to_config, 'r') as f:
        # print('This is what I am getting', f.read())
        cleanup_config = json.load(f)
    return cleanup_config


def current_time():
    return time.time()


def seconds_to_days(seconds, round=False):
    if round is True:
        days = int(seconds/86400)
    else:
        days = seconds/86400
    return days
