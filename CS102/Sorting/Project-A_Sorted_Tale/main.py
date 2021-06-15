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

# print(sorts.bubble_sort(books_list, condition1))
# print(sorts.bubble_sort(books_list, condition2))
# print(sorts.bubble_sort(books_list, condition3))
# print(sorts.bubble_sort(books_list, condition4))

condition1 = "pivot_element[0] > list[i][0]" # select this condition if you want to sort by title in ascending order
condition2 = "pivot_element[0] < list[i][0]" # select this condition if you want to sort by title in descending order
condition3 = "pivot_element[1] > list[i][1]" # select this condition if you want to sort by author in ascending order
condition4 = "pivot_element[1] < list[i][1]" # select this condition if you want to sort by author in descending order

# select this condition if you want to sort by number of characters in title and authors name in ascending order
condition5 = "len(pivot_element[0]) + len(pivot_element[1]) > len(list[i][0]) + len(list[i][1])"
sorts.quicksort(books_list, 0, len(books_list)-1, condition5)
print(books_list)