import sys

BOOKS_FILE = "books.txt"

def load_book():
    try:
        books = []
        with open(BOOKS_FILE) as file:
            for line in file:
                line = line.replace("\n", "")
                books.append(line)
        return books
    except FileNotFoundError:
        print("Could not find items file.")
        exit_program()
    except OSError as e:
        print("OSError:", e)
        exit_program()
    except Exception as e:
        print(type(e), e)
        exit_program()

def save_book(book_catalog):
    try:
        with open(BOOKS_FILE, 'w') as file:
            for key, value in book_catalog.items():
                file.write('%s:%s\n' % (key, value))
    except OSError:
        print("OSError occurred when writing file, closing program")
        exit_program()
    except Exception as e:
        print(type(e), e)
        exit_program()

def clear_books(book_catalog):
    choice = input("Are you sure you want to clear all books? (y/n): ")
    if choice == "y":
        book_catalog.clear()
        print("All books were cleared.")
    else:
        print("Books were not cleared.")

def show_book(book_catalog):
    user_book = input("Enter name of the book: ")
    for book in book_catalog:
        if book.lower() == user_book.lower():
            print(f"Author: {book_catalog[book]['author']}\nPublication year: {book_catalog[book]['pubyear']}")
            break
    else:
        print(user_book, "not in book catalog.")

def show_all_books(book_catalog):
    for book in book_catalog:
        print(f"{book}: {book_catalog[book]['author']} {book_catalog[book]['pubyear']}")

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
    print("show_all - Show all books")
    print("add -  Add book")
    print("edit - Edit book")
    print("del -  Delete book")
    print("clear - Delete all books")
    print("save - Save book list")
    print("load - Load book list")
    print("exit - Exit program")

def exit_program():
    print("Exiting program. Bye!")
    sys.exit()

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
    save_book(book_catalog)
    display_menu()
    while True:
        print()
        command = input("Command: ").lower()
        if command == "show":
            show_book(book_catalog)
        elif command == "show_all":
            show_all_books(book_catalog)
        elif command == "add":
            add_edit_book(book_catalog, mode="add")
        elif command == "edit":
            add_edit_book(book_catalog, mode="edit")
        elif command == "del":
            delete_book(book_catalog)
        elif command == "clear":
            clear_books(book_catalog)
        elif command == "save":
            save_book(book_catalog)
        elif command == "load":
            load_book()
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()
