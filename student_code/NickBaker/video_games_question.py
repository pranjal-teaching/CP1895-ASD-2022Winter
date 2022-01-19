def show_book(book_catalog):
    user_book = input("Enter name of the book: ")
    for book in book_catalog:
        if book.lower() == user_book.lower():
            print(f"Author: {book_catalog[book]['author']}\nPublication year: {book_catalog[book]['pubyear']}")
            break
    else:
        print(user_book, "not in book catalog.")


def add_edit_book(book_catalog, mode):
    title = input("Title: ")
    if mode == "edit" and title not in book_catalog:
        print("Title not in catalog")
        raise ValueError('Title not in catalog')
    pub_yr = input("Pub Year: ")
    author = input("Author: ")
    book_catalog[title] = {'author': author, 'pubyear': pub_yr}


def delete_book(book_catalog):
    title = input("Title to delete: ")
    if title in book_catalog:
        del book_catalog[title]
        print(f"{title} has been removed from catalog.")
    else:
        print(f"{title} doesn't exist in the catalog.")


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
