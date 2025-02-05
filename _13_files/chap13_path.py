import os
from pathlib import Path

names = ["Thomas\n", "Meersschaut\n"]
current_dir = Path(__file__).parent.absolute()      #Directory of file
#cwd = os.getcwd()      #Get Current Working Directory

#with open(f"{cwd}/outputpath.txt", "w") as file:
#    file.writelines(names)

with open(f"{current_dir}/outputpath2.txt", "w") as file:
    file.writelines(names)

print(current_dir)

config_dir = current_dir.parent.joinpath("config", "settings.ini")
print(config_dir)

os.path.pathsep
windows_path = r"c:\temp\output.txt"        #raw string