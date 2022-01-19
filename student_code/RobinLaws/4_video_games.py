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
    title = input("Title: ")
    if title.lower() in book_catalog:
        book = book_catalog[title]
        print(book_catalog)
        print(f"Title:    {title}")
        print(f"Author:   {book['author']}")
        print(f"Pub year: {book['pubyear']}")
    else:
        print(f"{title} is not in catalog.")


def add_edit_book(book_catalog, mode):
    title = input("Title: ")
    if title in book_catalog and mode == "add":
        choice = input(title + " is already in catalog. Would you like to edit? (y/n): ")
        if choice.lower() != "y":
            print("Book has not been edited.")
            return
    elif title not in book_catalog and mode == "edit":
        choice = input(title + "is not in catalog. Would you like to add?")
        if choice.lower != "y":
            print("Book has not been added.")
            return

    author = input("author: ")
    pubyear = input("pubyear: ")
    book = {title: {"author": author, "pubyear": pubyear}}
    book_catalog |= book



def delete_book(book_catalog):
    title = input("Title to delete: ")
    if title in book_catalog:
        del book_catalog[title]
        print(title + " has been removed from catalog.")
    else:
        print(title + " is not in the catalog.")


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

