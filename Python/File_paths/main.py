import os
print([item for item in os.scandir(".")])

from pathlib import Path
print([item for item in Path('.').iterdir()])

# List all file in a directory using listdir()
basepath = '.'
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        print(entry)

# List all files in a directory using scandir()
basepath = '.'
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_file():
            print(entry.name)

#List all files in a directory using pathlib.Path
basepath = Path('.')
files_in_basepath = basepath.iterdir()
for item in files_in_basepath:
    if item.is_file():
        print(item.name)

# List all subdirectories using os.listdir
basepath = '.'
for entry in os.listdir(basepath):
    if os.path.isdir(os.path.join(basepath, entry)):
        print(entry)

# List all subdirectories using scandir()
basepath = '.'
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_dir():
            print(entry.name)

# List all subdirectory using pathlib
basepath = Path('.')
for entry in basepath.iterdir():
    if entry.is_dir():
        print(entry.name)

# cwd = Current working directory
print(Path.cwd())

# Prints C:\Users\svein and appends python\scripts\test.py to the path
print(Path.home() / 'python' / 'scripts' / 'test.py')
print(Path.home().joinpath('python', 'scripts', 'test.py'))

def tree(directory):
    print(f'+ {directory}')
    for path in sorted(directory.rglob('*')):
        depth = len(path.relative_to(directory).parts)
        spacer = '    ' * depth
        print(f'{spacer}+ {path.name}')

tree(Path.cwd())