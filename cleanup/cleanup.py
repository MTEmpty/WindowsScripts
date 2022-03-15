from cleaner import Cleaner
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

        cleaner = Cleaner(settings)
        cleaner.cleanup_items()

        folders_scanned = cleaner.total_directories
        objects_scanned = cleaner.total_objects
        old_objects = cleaner.old_objects
        empty_folders = cleaner.empty_folders
        print(
            f'Folders scanned: {folders_scanned}, ' \
            f'Objects scanned: {objects_scanned}, ' \
            f'{old_objects} were old and ' \
            f'there were {empty_folders} empty folders')



if __name__ == '__main__':
    main()
