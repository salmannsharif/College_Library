class Library:
    def __init__(self,list_of_books, library_name):
        self.lend_data={}
        self.list_of_books = list_of_books
        self.library_name = library_name

        for books in self.list_of_books:
            self.lend_data[books] = None

    def display_books(self):
        for index,books in enumerate(self.list_of_books):
            print(f"{index}:{books}")

    def lend_books(self,book,reader):
        if book in self.list_of_books:
            if self.lend_data[book] is None:
                self.lend_data[book]=reader
                print("Book Lend")
            else:
                print(f"Sorry this book is lend by {self.lend_data[book]}")
        else:
            print("You have written the wrong book name ")


    def return_books(self,book,reader):
        if book in self.list_of_books:
            if self.lend_data[book] is not None:
                self.lend_data.pop(book)
            else:
                print("This book is not lend")
        else:
            print("You have written the wrong  book name ")


    def add_books(self,book_name):
        self.list_of_books.append(book_name)
        self.lend_data[book_name] = None

    def delete_books(self,Books_name):
        self.list_of_books.remove(Books_name)
        self.lend_data.pop(Books_name)



def main():
    book_list = ["Sherlock Holmes", "Rich dad poor dad", "7 Habits"]
    library_name = "SALMAN"
    secret_key = 12345
    salman = Library(book_list, library_name)

    print(f"Welcome To {salman.library_name} Library")
    print("Press q-for Quit\nd-for Display\nl- for lend books\ndel-for delete books "
          "\nr-for Return Books\na-for Add Books \n\n")

    Exit = False
    while Exit is not True:
        _input=input("Option: ")
        print("\n")
        if _input=="q":
            Exit=True

        elif _input=="d":
            salman.display_books()

        elif _input=="l":
            _input2=input("Enter YOur Name:")
            _input3=input("Enter the book name ")

            salman.lend_books(_input3,_input2)

        elif _input=="del":
            _input_secret_key=input("Enter the secret key do delete Book:")

            if _input_secret_key==secret_key:
                _input1=input("Enter the books name :")
                salman.delete_books(_input1)

        elif _input=="r":
            _input2 = input("Enter YOur Name:")
            _input3 = input("Enter the book name ")

            salman.return_books(_input3, _input2)

        elif _input=="a":
            _input1=input("Enter the Book Name:")
            salman.add_books(_input1)

if __name__ == '__main__':
    main()




