import sys
from pathlib import Path
from typing import List


def main(root_folder: str, destination_folder: str, extensions: List[str]):
    print(f"Root folder: {root_folder}")
    print(f"Destination folder: {destination_folder}")
    print(f"Extensions: {extensions}")

    path = Path(root_folder)
    if not path.exists():
        print("The folder does not exist.")
        return

    destination_folder_path = Path(destination_folder)
    if not destination_folder_path.exists():
        destination_folder_path.mkdir(parents=True)

    # Normalize the extensions for comparison
    normalized_extensions = [ext.lower() for ext in extensions]

    for file in path.rglob('*'):
        if file.is_file() and file.suffix.lower()[1:] in normalized_extensions:
            try:
                print(f"Copying file: {file}")
                destination_file = destination_folder_path / file.name

                if destination_file.exists():
                    print(f"File {destination_file} already exists. Skipping.")
                    continue

                destination_file.write_bytes(file.read_bytes())
            except Exception as e:
                print(f"Error copying file {file}: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: script.py <root_folder> <destination_folder> <extensions>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2], sys.argv[3:])

# python move_files.py "C:\source_folder" "C:\destination_folder" .txt .jpg
