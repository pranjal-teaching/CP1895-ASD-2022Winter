def generate_multiplication_table(width: int, height: int):
    table = ""
    width_counter = 1
    height_counter = 1
    max_total = height * width
    max_digits = len(str(max_total))

    for row in range(height):
        for column in range(width):
            total = width_counter * height_counter
            table_format = "{:" + str(max_digits) + "}"
            table += table_format.format(total) + " "
            width_counter += 1
        table += "\n"
        width_counter = 1
        height_counter += 1
    print(table)
    save_table(table)


def save_table(table):
    with open("table.txt", "w") as fileHandler:
        for text in table:
            fileHandler.write(str(text))


def input_width():
    while True:
        try:
            width = int(input("Enter width of table: "))
            if width > 0:
                break
            else:
                print("Width must be greater than zero.")
        except ValueError:
            print("Please enter a valid integer for width.")
    return width


def input_height():
    while True:
        try:
            height = int(input("Enter height of table: "))
            if height > 0:
                break
            else:
                print("Width must be greater than zero.")
        except ValueError:
            print("Please enter a valid integer for height.")
    return height


def main():
    print("Multiplication Table Generator")
    print()
    a = input_width()
    b = input_height()
    print()
    generate_multiplication_table(a, b)


if __name__ == "__main__":
    main()
