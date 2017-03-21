import os


class Templater(object):
    def __init__(self, path=None, templates=None, pattern=None, name=None, *args, **kwargs):
        self.path = path
        self.templates = templates
        self.pattern = pattern
        self.name = name

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = os.path.abspath(os.path.expanduser(value))

    @property
    def templates(self):
        return self._templates

    @templates.setter
    def templates(self, value):
        self._templates = os.path.abspath(os.path.expanduser(value))

    def generate_template(self):
        root_folder = self.templates
        destination_folder = self.path

        walk_list = os.walk(root_folder)

        for root, sub_folders, files in walk_list:
            folder_path = destination_folder
            if root is not root_folder:
                folder = os.path.split(root)[1]
                folder_path = os.path.join(destination_folder, folder)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            self.create_files(root, files, folder_path)

    def create_files(self, files_root, files, folder_path):
        for element in files:
            template_path = os.path.join(files_root, element)
            with open(template_path) as template:
                file_path = os.path.join(folder_path, element)
                file_name = file_path.replace(self.pattern, self.name)
                element = open(file_name, 'w')
                for line in template:
                    content = line.replace(self.pattern, self.name)
                    element.write(content)
                element.close()


