class Filesystem:
    def __init__(self, root_dir: str):
        self.root_dir = root_dir
        self.contains = {f'{root_dir}': []}

    def add_file(self, parent_dir: str, filename: str) -> bool:
        if not parent_dir in self.contains:
            print(f'Error: Directory not found {dir}')
            return False
        self.contains[parent_dir].append(filename)
        return True
    
    def remove_file(self, parent_dir: str, filename: str) -> bool:
        if not filename in self.contains[parent_dir]:
            print(f'Error: File not found {filename}')
            return False
        self.contains[parent_dir].pop(filename)
        return True

    def add_folder(self, parent_dir: str, folder_name: str) -> bool:
        if not parent_dir in self.contains:
            print(f'Error: Parent directory not found {parent_dir}')
            return False
        self.contains[parent_dir].append(folder_name)
        return True
    
    def remove_folder(self, parent_dir: str, folder_name: str) -> bool:
        if not parent_dir in self.contains:
            print(f'Error: Folder not found {folder_name}')
            return False
        self.contains[parent_dir].pop(folder_name)
        return True