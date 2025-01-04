from collections import Counter
from pathlib import Path
import os

def tree(directory):
    print(f"+ {directory}")
    for path in sorted(directory.rglob("*")):
        depth = len(path.relative_to(directory).parts)
        spacer = "    " * depth
        print(f"{spacer}+ {path.name}")

def main():
    current_path = Path(__file__).parent
    root_path = current_path.parent
    current_dir = Path(__file__).parent.absolute()
    print(current_dir)
    print(root_path)
    print(current_path)
    my_python_files = current_path.rglob("**/*.py")
    for file in my_python_files:
       print(file.stem,end=" -- ")
       print(file.suffix)
    config_dir = current_dir.parent.joinpath("config", "settings.ini")
    print(config_dir)
    tree(Path.cwd())
    for file_path in Path.cwd().glob("*.txt"):
        new_path = Path("archive") / file_path.name
        file_path.rename(new_path)
    c=Counter(path.suffix for path in Path.cwd().iterdir())
    for ext, count in c.items():
        print(f"{ext}: {count}")

"""
https://realpython.com/python-pathlib/
"""


if __name__ == "__main__":
    main()


