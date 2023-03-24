### © Ofir Tzafrir
##Exercise 1
#Q1

x1 = 0.0
x2 = 1.0
x3 = 2.212

def my_func(x1, x2, x3):
   if type(x1) == str or type(x2) == str or type(x3) == str:
       return print(None)
   if type(x1) != float or type(x2) != float or type(x3) != float:
       return print('Error: parameters should be float')
   if x1 + x2 + x3 == 0:
       return print('Not a number – denominator equals zero')
    else:
      result = ((x1 + x2 + x3) * (x2 + x3) * x3) / (x1 + x2 + x3)
       print(result)

my_func(x1, x2, x3)

# --------------------------
#Q2

handle = open('text.txt')
lst = []
for i in handle:
    split_1 = i.strip().split()
    for j in split_1:
        lst.append(j)

word = lst[0]
lst = lst[1:]

def revword(string):
    new_lst = reversed(string)
    words = ''.join(new_lst)
    if words == word:
        return True
    else:
        return False

counter = 0
for k in lst:
    string = k.lower()
    if revword(string):
        counter += 1

print(counter+1)