


def main():
    hanoi_tower(3,"A","B","C")


def hanoi_tower(n,src,helper,dest):
    if n == 1:
        print(f"move {src} to {dest}")
        return
    hanoi_tower(n-1,src,dest,helper)
    print(f"move {src} to {dest}")
    hanoi_tower(n-1,helper,src,dest)


if __name__ == '__main__':
    main()
