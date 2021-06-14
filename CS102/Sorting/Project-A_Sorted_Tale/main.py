import utils
import sorts

condition1 = "arr[idx][0] > arr[idx + 1][0]" # select this condition if you want to sort by title in ascending order
condition2 = "arr[idx][0] < arr[idx + 1][0]" # select this condition if you want to sort by title in descending order
condition3 = "arr[idx][1] > arr[idx + 1][1]" # select this condition if you want to sort by author in ascending order
condition4 = "arr[idx][1] < arr[idx + 1][1]" # select this condition if you want to sort by author in descending order


bookshelf = utils.load_books('books_small.csv')
books_list = [] # empty_list to store the books
for book in bookshelf:
    # create a list of list (the first element of the sublist is the title, whereas the second is the author)
    books_list.append([book['title'], book['author']])

print(sorts.bubble_sort(books_list, condition4))