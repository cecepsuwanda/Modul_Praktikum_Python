def faktorial(n: int) -> int:
    if n == 0:
        return 1
    return n * faktorial(n - 1)

def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def main() -> None:
    # 3! = 3 * 2!
    # 2! = 2 * 1!
    # 1! = 1 * 0!
    # 0! = 1
    n = int(input("Masukkan n : "))
    print(faktorial(n))
    

if __name__ == "__main__":
    main()

 # 1 
 # 2
 # 3
 # 4   