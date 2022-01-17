def display_menu():
    print("The Book Catalog program")
    print()
    print("COMMAND MENU")
    print("show - Show book info")
    print("add -  Add book")
    print("edit - Edit book")
    print("del -  Delete book")
    print("exit - Exit program")


def show_book(book_catalog):
    print()
    i = 1
    for key, value in book_catalog.items():
        print(f"{i}. {key}")
        i += 1
    print()
    selected_book = int(input(f"Please select a book (1-{i - 1}): ")) - 1
    selected_book_title = [key for key in book_catalog.keys()][selected_book]
    selected_book_author = book_catalog[selected_book_title]["author"]
    selected_book_year  = book_catalog[selected_book_title]["pubyear"]
    print()
    # print(f"Book Name: {book_catalog[]}")
    print(f"Title: {selected_book_title}")
    print(f"Author: {selected_book_author}")
    print(f"Publication Year: {selected_book_year}")


def add_edit_book(book_catalog, mode):
    pass


def delete_book(book_catalog):
    pass


def main():
    book_catalog = {
        "Moby Dick":
            {"author": "Herman Melville",
             "pubyear": "1851"},
        "The Hobbit":
            {"author": "J. R. R. Tolkien",
             "pubyear": "1937"},
        "Slaughterhouse Five":
            {"author": "Kurt Vonnegut",
             "pubyear": "1969"}
    }
    display_menu()
    while True:
        print()
        command = input("Command: ").lower()
        if command == "show":
            show_book(book_catalog)
        elif command == "add":
            add_edit_book(book_catalog, mode="add")
        elif command == "edit":
            add_edit_book(book_catalog, mode="edit")
        elif command == "del":
            delete_book(book_catalog)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Unknown command. Please try again.")


if __name__ == "__main__":
    main()
