import utils
import sorts

bookshelf = utils.load_books('books_small.csv')
books_list = [] # empty_list to store the books
for book in bookshelf:
    # create a list of list (the first element of the sublist is the title, whereas the second is the author)
    books_list.append([book['title'], book['author']])

print(sorts.bubble_sort(books_list))

