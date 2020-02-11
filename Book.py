class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    # Potremmo usare questa funzione...
    # ma meglio di no!
    def compare(self,other_book):
        return self.author < other_book.author