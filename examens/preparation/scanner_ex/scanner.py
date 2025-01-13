"""
scan files for words
"""
import pathlib
from pathlib import Path


def main():
    print("Scanner")
    dict_paras = {}
    word_list = ["def", "class", "if", "for", "while"]
    result = scan_directory(Path(__file__).parent.parent, "py")
    for file in result:
        d = scan_file(file, word_list=["def", "class", "if", "for", "while"])
        for key in d:
            dict_paras[key] = dict_paras.get(key, []) + d[key]
    for key in dict_paras:
        print(key)
        for file, para, index in dict_paras[key]:
            print(f"\t{file} : {para} ({index})")
    with open("summary.txt", "w") as file_s:
        for key in dict_paras:
            file_s.write(f"{key}\n")
            for file, para, index in dict_paras[key]:
                file_s.write(f"\t{file} : {para} ({index})\n")


def scan_directory(dir_path, suffix) -> [pathlib.Path]:
    filenames = []
    for f in Path(dir_path).iterdir():
        if f.is_file() and f.suffix[1:] == suffix:
            filenames.append(f)
        elif f.is_dir():
            filenames.extend(scan_directory(f.resolve(), suffix))
    return filenames


def scan_file(path: Path, word_list: list):
    dict_words = {}
    with open(path, 'r') as file_c:
        content = file_c.read()
        # seperate in para
        paragraphs = [para.strip() for para in content.split("\n\n") if para.strip()]

        # search for words
        for para in paragraphs:
            for word in word_list:
                if word in para:
                    if word not in dict_words:
                        dict_words[word] = [(path, para, para.index(word))]
                    else:
                        dict_words[word].append((path, para, para.index(word)))
                # dict_words[word] = dict_words.get(word, []).append((path, para,para.index(word)))
    return dict_words


def make_summary():
    print("Make summary")


if __name__ == '__main__':
    main()
