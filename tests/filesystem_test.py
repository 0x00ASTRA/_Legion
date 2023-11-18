import sys
import os

# Get the absolute path of the project's root directory
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add the root directory to the Python path
sys.path.append(root_path)

from src.filesystem import Filesystem

f1 = Filesystem('/')
f1.add_file('/', 'hello.txt')
f1.add_folder('/', 'Docs')
print(f1.contains)