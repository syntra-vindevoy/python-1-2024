from pathlib import Path

current_path = Path(__file__).parent
root_path = current_path.parent

my_python_files = root_path.rglob("**/*.py")

for file in my_python_files:
    print(file)
