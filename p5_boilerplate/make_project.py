import shutil
import sys
import os

try:
    directory_name = sys.argv[1]
except IndexError:
    print(f"usage {__file__} directory_name")
    quit()

if __name__ == '__main__':
    try: 
        os.mkdir(directory_name)
    except FileExistsError: 
        print("directory already exists, copying files. . .")

    shutil.copy(f"./index.html", f'./{directory_name}/index.html')
    shutil.copy("./run.py", f'{directory_name}/run.py')
    print(f"created starter project at {directory_name}")
