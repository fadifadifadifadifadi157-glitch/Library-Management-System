class Book:
    def __init__(self,book_id,title,author):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.available=True

    def Borrow(self):
        if self.available:
            self.available=False
            print("Book Borrowed Successfully!")
        else: 
            print("Book is already borrowed!")

    def Return(self):
        if not self.available:
            self.available=True
            print("Book Returned Successfully!")
        else:
            print("Book is already Available!")

    def Display(self):
        print("Book Id:",self.book_id)
        print("Book Title:",self.title)
        print("Auther:",self.author)

        if self.available:
            print("Status: Available")
        else: 
            print("Status: Borrowed")

class Library:
    def __init__(self):
        self.books={}

    def ADD(self):
        id=input("Enter Book id:")
        if id in self.books:
            print("Book already exists!")
            return
        title=input("Enter Book Title:")
        author=input("Enter Author Name:")

        book=Book(id,title,author)
        self.books[id]=book
        print("Book Added Successfully!")

    def search(self):
        id=input("Enter book Id:")

        book=self.books.get(id)

        if book:
            book.Display()
        else:
            print("Book not found!")

    def Book_Borrow(self):
        id = input("Enter book id:")

        book=self.books.get(id)
        if book:
          book.Borrow()
        else:
            print("Book not found")  
                
    def book_Return(self):
        id = input("Enter book id:")
        
        book=self.books.get(id)
        if book:
            book.Return()
        else:
            print("Book not found") 

    def display_all(self):
        if len(self.books) ==0:
            print("No book available!")
        else:
          print("===================Books in Library======================== ")   
          for book in self.books.values():
           
            book.Display()
            print("============================================================")

    def Menu(self):
        while True:
            print("===============Library Management System=====================")
            print("1.Add book")
            print("2.Borrow book")
            print("3.Return book")
            print("4.Search book")
            print("5.Display books")
            print("6.Exit")
            print("=============================================================")
            choice=int(input("Enter your choice:"))

            if choice==1:
                self.ADD()
            elif choice==2:
                self.Book_Borrow()
            elif choice==3:        
                self.book_Return()
            elif choice==4:
                self.search()
            elif choice==5:
                self.display_all()
            elif choice==6:
                print("Thank you!")
            else:
                print("Invalid Choice!")

l1=Library()
l1.Menu()
                

                                