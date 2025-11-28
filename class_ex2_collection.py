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
    

    def searchBook(authur_name,lstBook):
        for i in lstBook:
             if i.author==authur_name:
                  i.display()

book1=book("who will cry when you die","robin sharma",23456,200,10)
book2=book("focus","stephn",909090,120,12)
book3=book("Python","Robin Sharma",23456,200,10)
book4=book("Proramming in c ","Stephn",909090,120,12)

lst_book=[book1,book2,book3,book4,book("django","ste",23232323,230,23)]
book.searchBook(authur_name='Robin Sharma',lstBook=lst_book)
