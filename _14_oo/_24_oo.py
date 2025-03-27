def f(x:int) -> None:
        print(5/x)



def main():
    f(2)
    f(0)



if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print("Error:", err)