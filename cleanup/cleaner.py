import os

from utils import current_time, seconds_to_days


def file_age(file):
    return os.path.getmtime(file)


def delete_file(file):
    try:
        os.remove(file)
    except PermissionError:
        pass
    except Exception as e:
        print(f'Failed to delete file: {str(e)}')
    else:
        return True


def delete_folder(folder):
    try:
        os.rmdir(folder)
    except PermissionError:
        pass
    except Exception as e:
        print(f'Failed to delete folder: {str(e)}')
    else:
        return True


def archive_file(old_file, new_file):
    try:
        os.rename(old_file, new_file)
    except PermissionError:
        pass
    except Exception as e:
        print(f'Failed to move files to archive: {str(e)}')
    else:
        return True


class Cleaner:
    def __init__(self, config):
        self.path = config.get('path')
        self.action = config.get('action', 'delete')
        self.threshold = config.get('age_threshold')
        self.delete_empty_folder = config.get('delete_empty_folder')
        self.current_time = current_time()

        if self.action == 'archive':
            self.archive_path = config.get('archive_path')

        self.total_directories = 0
        self.total_objects = 0
        self.old_objects = 0
        self.empty_folders = 0

        # generator that will contain all the items in the path
        # items can either be files or folders
        self.items = self._list_items()

        # list of items to be deleted
        self.delete_file_list = []
        self.delete_folder_list = []

        # list of items to be archived
        self.archive_file_list = []

    def cleanup_items(self):
        for item in self.items:
            self.total_directories += 1
            # item can be a file or a directory
            item_path = item[0]

            directories_in_item = item[1]
            files_in_item = item[2]
            for file in files_in_item:
                self.total_objects += 1
                self._classify_file(item_path, file)
            
            if directories_in_item == [] and files_in_item == []:
                self._classify_directory(item_path)

        for file in self.delete_file_list:
            delete_file(file)

        for folder in self.delete_folder_list:
            delete_folder(folder)

        for file in self.archive_file_list:
            new_path = file.replace(self.path, self.archive_path)
            archive_file(file, new_path)

    def _classify_file(self, item_path, file_name):
        path_to_file = os.path.join(item_path, file_name)
        
        last_modified_epoch = file_age(path_to_file)
        age_seconds = self.current_time - last_modified_epoch
        age_days = seconds_to_days(age_seconds)
        old_item = age_days > self.threshold
        if self.action == 'delete' and old_item is True:
            self.old_objects += 1
            self.delete_file_list.append(path_to_file)
        elif (self.action == 'archive'
                and self.archive_path not in path_to_file
                and old_item is True):
            self.old_objects += 1
            self.archive_file_list.append(path_to_file)
            print(path_to_file)

    def _classify_directory(self, item_path):
        last_modified_epoch = file_age(item_path)
        age_seconds = self.current_time - last_modified_epoch
        age_days = seconds_to_days(age_seconds)
        if age_days > self.threshold:
            self.empty_folders += 1
            self.delete_folder_list.append(item_path)

    def _list_items(self):
        directories = os.walk(self.path, topdown=False)
        return directories
