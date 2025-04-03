from pathlib import Path

list_1 = ["a", "b", "c", "d", "e"]
list_2 = ["b", "d", "f"]

print( list( set(list_1) - set(list_2) ))

print( list( set(list_2) - set(list_1) ))


old_dir = set({path.relative_to("old") for path in Path("old").glob("*.txt")})
new_dir = set({path.relative_to("new") for path in Path("new").glob("*.txt")})

new_files = new_dir - old_dir
deleted_files = old_dir - new_dir
untouched_files = old_dir & new_dir

print("new", new_files)
print("deleted", deleted_files)
print("untouched", untouched_files)

