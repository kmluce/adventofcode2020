import fileinput

def find_vals(expenses):

   for i in range(len(expenses)):
      for j in range(i):
         if (expenses[i] + expenses[j]) == 2020 :
             return int(expenses[i] * expenses[j])

   return -1

def get_expenses():
   loopCount = 0
   expenseArray =[]

   for line in fileinput.input():
      expenseArray.append(int(line))

   return(find_vals(expenseArray))


if __name__ == '__main__':
   print("Expense check value is ", get_expenses())