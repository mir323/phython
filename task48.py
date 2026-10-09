def main():
    product = 1
    while True:
        num = int(input().strip())
        if num != 0:
            product *= num
        if num == 0:
            print(product)
            return

if __name__ == "__main__":
    main()
