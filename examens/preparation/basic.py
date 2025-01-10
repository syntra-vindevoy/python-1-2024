def main():
    li= [x*3 for x in range(1,10)]
    print(li)
    print(f"{15 in li}")
    li.insert(1,7)
    print(li)




if __name__ == "__main__":
    main()