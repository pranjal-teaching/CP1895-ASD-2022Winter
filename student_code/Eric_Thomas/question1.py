def generate_table(a, b):
    columns = 1
    while columns <= a:
        rows = 1
        while rows <= b:
            print("%4d" % (columns * rows), end=' ')
            rows += 1
        print()
        columns += 1


def main():
    print("Multiplication Table Generator \n")
    a = int(input("Enter number of rows as an integer: "))
    b = int(input("Enter number of columns as an integer: "))
    generate_table(a, b)


if __name__ == "__main__":
    main()
