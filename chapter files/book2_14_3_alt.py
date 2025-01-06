from pathlib import Path
import hashlib

def search_for_duplicates(search_dir):
    hashes = {}
    if Path.exists(search_dir):
        print ("path exists")
    else:
        print ("path does not exist")
        return
    files = list(search_dir.rglob("*"))
    for file in files:
        if file.is_file():
            with open (file, "rb") as f:
                data = f.read()
                file_hash = hashlib.md5(data).hexdigest()

                if file_hash in hashes:
                    hashes[file_hash].append(file)
                else:
                    hashes[file_hash] = [file]

    print (f"Following files were identified as duplicates:")
    for file_hash, file_list in hashes.items():
        if len(file_list) > 1:
            print(f"\nHash: {file_hash}")
            for file in file_list:
                print(f"  {file}")

cwd = Path.cwd()
search_dir = cwd.absolute() / "foto"
search_for_duplicates(search_dir)
