from utils import *


def get_object_class_name(object_):
    return object_.__class__.__name__


def test_seconds_to_days():
    seconds = 86400
    days = seconds_to_days(seconds)
    print(days)
    assert days == float(1)


def test_get_config():
    actual = get_config()
    assert get_object_class_name(actual) == 'dict'
    assert actual.get('config_path') is not None
    
    actual2 = get_cleanup_targets(actual)
    assert get_object_class_name(actual2) == 'dict'
    
    actual_paths = actual2.get('paths')
    assert actual_paths is not None
    assert get_object_class_name(actual_paths) == 'dict'
    assert len(actual_paths) > 0
    
    for key, _ in actual_paths.items():
        path_config = actual_paths[key]
        path = path_config.get('path')
        delete_empty_folder = path_config.get('delete_empty_folder')
        age_threshold = path_config.get('age_threshold')
        assert path is not None
        assert delete_empty_folder is not None
        assert age_threshold is not None
