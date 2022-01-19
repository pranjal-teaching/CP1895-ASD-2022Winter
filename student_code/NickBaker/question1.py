# Question 1

def generate_multiplication_table(width, height):
    for i in range(1, height+1):
        for j in range(1, width+1):
            print("%d\t" % (i*j), end="")
        print()


def main():
    while True:
        try:
            width = int(input("Enter Width: "))
            break
        except ValueError:
            print("Please enter a valid integer")

    while True:
        try:
            height = int(input("Enter Height: "))
            break
        except ValueError:
            print("Please enter a valid integer")

    generate_multiplication_table(width, height)


if __name__ == "__main__":
    main()
