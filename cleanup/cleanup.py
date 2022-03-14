from utils import get_config, get_cleanup_targets

def main():
    print('Starting cleanup')
    config = get_config()
    cleanup_targets = get_cleanup_targets(config)
    paths = cleanup_targets.get('paths')
    for path, settings in paths.items():
        print('\n' * 2)
        print('- ' * 10, 'Cleaning up for:', path, ' -' * 10)
        print('Threshold:', settings.get('age_threshold'), 'days')
        print('Delete empty folders:', settings.get('delete_empty_folder'))



if __name__ == '__main__':
    main()
