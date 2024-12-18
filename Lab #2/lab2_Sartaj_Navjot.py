# Name: Sartaj Singh and Navjot Singh
# Date: June 7, 2024
# Modified: June 7, 2024
# Description: This code is a reading list application which allow users to add, list,
# search for books, with stored in csv file.


# Import csv file.
import csv

# A function to add a book in the books.csv file.
def books_added():
    # Ask the user to add the title, author's name, publication year of the book. 
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    year = input("Enter the year of publication: ")
    # Open and add the book details in the books.csv file.
    with open('books.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([title, author, year])
        # Print a message, the book is added succesfully!
    print("Book added successfully!")

# A function to list all the books available in the books.csv file.
def books_list():
    # Open the books.csv file in read mode.
    with open('books.csv', 'r') as file:
        # Create a csv books reader object
        reader = csv.reader(file)
        for row in reader:
            # Print the detail for each book.
            print(row)

# A function to search for a specific book by its title.
def search_books():
    search_title = input("Enter the title of the book to search for: ")
    with open('books.csv', 'r') as file:
        reader = csv.reader(file)
        # loop through each row of csv.file
        for row in reader:
            # Check if the search title matches with existing book's title.
            if search_title == row[0]:
                # If matches, print the details of the book, otherwise print a message.
                print(row)
                break
            else:
                print("Book not found in the list")

# Defining main function to handle the user's choices.
def main():
    # Continuous loop to mantain the menu function.
    while True:
        # Display the menu's option.
        print("Menu:")
        print("1. Add a Book")
        print("2. List all Books")
        print("3. Search for a Book")
        print("4. Quit")
        # Ask the user to enter their choice.
        choice = input("Enter your choice: ")
        # Call the Function according to the user's choice.
        if choice == '1':
            books_added()
        elif choice == '2':
            books_list()
        elif choice == '3':
            search_books()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Choice must be between 1 to 4.")

# Call the main function to start the program.
if __name__ == "__main__":
    main()