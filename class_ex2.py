class book:
    def __init__(self,title,author,isbn,price,qty):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.price=price
        self.qty=qty

    def display(self):
        print(f"{self.title}-{self.author}-{self.isbn}")

    def calculatePrice(self):
        return self.price*self.qty

book1=book("who will cry when you die","robin sharma",23456,200,10)
book2=book("focus","stephn",909090,120,12)

book1.display()
book2.display()
print("price list")
print(f"{book1.title} total price is {book1.calculatePrice()}")
print(f"{book2.title} total price is {book2.calculatePrice()}")

