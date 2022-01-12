def generate_multiplication_table(width, height):
    for i in range(1, height+1):
        for j in range(1, width+1):
            print(i*j, end='   ')
        print()


def main():
    while True:
        try:
            a = int(input("Enter value of width: "))
        except ValueError:
            print("Must be an integer")
            continue
        if a < 0:
            print("Must be greater than 0.")
        else:
            break

    while True:
        try:
            b = int(input("Enter value of height: "))
        except ValueError:
            print("Must be an integer")
            continue
        if b < 0:
            print("Must be greater than 0.")
        else:
            break
    generate_multiplication_table(a, b)


if __name__ == '__main__':
    main()