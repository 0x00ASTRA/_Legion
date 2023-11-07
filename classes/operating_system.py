from classes.filesystem import Filesystem

class OS:
    def __init__(self, name, kernel, version, kernel_version):
        self.name = name
        self.kernel = kernel
        self.version = version
        self.kernel_version = kernel_version
        self.filesystem = Filesystem('/')

    def update(self):
        pass

    def list_files(self):
        return str(self.filesystem.contains)
    
    def delete_file(self, path):
        pass

    def create_file(self, path, name):
        pass

    def create_folder(self, path: str, name: str):
        self.filesystem.add_folder(path, name)

    def delete_folder(self, path):
        pass

    def rename_file(self, old_path, new_path):
        pass

    def rename_folder(self, old_path, new_path):
        pass

    def move_file(self, old_path, new_path):
        pass

    def move_folder(self, old_path, new_path):
        pass

    def copy_file(self, old_path, new_path):
        pass

    def copy_folder(self, old_path, new_path):
        pass

    def install_package(self, package):
        pass

    def uninstall_package(self, package):
        pass

    def execute_command(self, command):
        pass

    def create_process(self, command):
        pass

    def kill_process(self, process):
        pass

    def new_shell(self):
        pass

