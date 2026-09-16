
def fib_recursive(n):
    if n < 2:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def main():
    with open("output/fibonacci.txt", "w") as f:
        for i in range(25):
            f.write(f"{fib_recursive(i)}\n")


if __name__ == "__main__":
    main()
