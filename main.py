import time
from pathlib import Path
from os import *

# from distutils.dir_util import *

target = Path("C:")
start = Path("D:")
# list(start.glob('**/**'))
file = [x for x in start.iterdir() if not x.is_dir()]
folder = [x for x in start.iterdir() if x.is_dir()]
lastModifiedEpoc = path.getmtime(file[0])
lastModified = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(lastModifiedEpoc))

if __name__ == '__main__':
    print("Folder: " + str(folder))
    print("File: " + str(file))
    print("Last Modified Time : ", lastModified)

# copy_tree(start, target)
