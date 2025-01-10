"""
 Write a Python function that rotates a list by `n` positions. For example:
     - Input: `lst = [1, 2, 3, 4, 5], n = 2`
     - Output: `[4, 5, 1, 2, 3]` (if rotated to the right).
   - Write a program that splits a list into two halves and swaps them. For example:
     - Input: `[1, 2, 3, 4, 5, 6]`
     - Output: `[4, 5, 6, 1, 2, 3]`

"""
def main():
    lst = [1, 2, 3, 4, 5]
    print(lst)
    n=2
    lst = lst[n+1:]+lst[:n+1]
    print(lst)

    lst = [1, 2, 3, 4, 5, 6]
    print(lst)
    middle=len(lst)//2
    lis1=lst[:middle]
    lis2=lst[middle:]

    lst=lis2+lis1
    print(lst)



if __name__ == "__main__":
    main()