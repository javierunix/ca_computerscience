import csv

# This code loads the current book
# shelf data from the csv file
def load_books(filename):
  bookshelf = []
  with open(filename) as file:
      shelf = csv.DictReader(file)
      for book in shelf:
          # we are going to convert authors and titles into lowercase before comparing
          book['author'] = book['author'].lower()
          book['title'] = book['title'].lower()

          bookshelf.append(book)
  return bookshelf