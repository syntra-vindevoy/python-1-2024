from pathlib import Path

current_path = Path(__file__).parent
root_path = current_path.parent

my_python_files = root_path.rglob("**/*.py")

print(list(my_python_files))