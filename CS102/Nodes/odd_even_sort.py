def odd_even_sort(list):
   # flag
   is_sorted = False

   while is_sorted == False:

      is_sorted = True

      for i in range(1, len(list) - 1, 2):

         if list[i] > list[i + 1]:

            list[i], list[i + 1] = list[i + 1], list[i]

            is_sorted = False

      for i in range(0, len(list) - 1, 2):

         if list[i] > list[i + 1]:

            list[i], list[i + 1] = list[i + 1], list[i]
            
            is_sorted = False

   return list

list = [1, 4, 2, 3, 6, 5, 8, 7]

print(odd_even_sort(list))
