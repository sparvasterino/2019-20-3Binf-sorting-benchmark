from Book import Book 
from selection_sort_book import selection_sort

book1 = Book("Canzoniere","Petrarca")
book2 = Book("Divina Commedia","Dante")
book3 = Book("Decamerone","Boccaccio")
book_list = [book1,book2,book3]

print(f"Lista prima: {[x.author for x in book_list]}")

selection_sort(book_list)

print(f"Lista dopo: {[x.author for x in book_list]}")
