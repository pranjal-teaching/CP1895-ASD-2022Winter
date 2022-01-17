def display_menu():
    print("The Book Catalog program")
    print()
    print("COMMAND MENU")
    print("show - Show book info")
    print("add -  Add book")
    print("edit - Edit book")
    print("del -  Delete book")
    print("exit - Exit program")


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
