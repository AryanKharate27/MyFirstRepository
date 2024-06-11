# 22
# print(2 + 4)
# print(type(2 + 4))  # 'type' to find the type of data type
# print(type(2 / 4))
# print(2 ** 2)  # '**' to find the power of t2 numbers
# print(6 // 2)  # '//' gives int value of division rounded
# print(6 % 2)  # '%' to find the modulo

# 27
# print(bin(5)) #'bin() gives binary number '
# print(int('0b101' ,2 ))   #format to convert binary to number

# type conversion
# str(100)
# print(str(100))
# print(type(str(100)))
# print(int(str(100)))
# print(type(int(str(100))))

# escape sequence
#   #print('it's rainy today') #cant be printed
# print('it\'s rainy today')
# print("\t Hi! it\'s Rainy today \n Use a umbrella")  #\t for tab space and \n for new line

# formatted String
# name= 'jhonny'
# age=  55
# print('Hi! '+name + 'Your age is. '+str(age)+' Years old')
# print(f'HI! {name} your age is {age} years old.')  #USing formatted string

# # Strings
# numbers = '12345678'
# print(numbers)
# print(numbers[0:8:2])  #[Start:Stop:Steepover]
# print(numbers[::-1])   #use '-' to start   numbers from the back of the string

# #Built in functions
# #1 (len)-> finds the length if the string
# print(len('Hellooooo!'))
# a= 'to be or not to be'
# print(a.upper())
# print(a.capitalize())
# print(a.replace('be','me'))

# #Age guessing
# birth_year=int( input('What year were you born'))
# curr_year=int(input('What year is today'))
# age=curr_year-birth_year
# print('Your Age is->'+str(age)+ ' Years')

# # Password Length Checker
# username = input('Enter your Username')
# password = input('Enter your password')
# password_len = len(password)
# hidden_pass = '*' * password_len
# print(f'{username},your password,{hidden_pass},is {password_len} long ')

# #Lists
# amazon_cart=['notebooks','Pens','Scale','Pouch']
# print(amazon_cart[0:4:2]) #[Start:stop:Stepover]
# amazon_cart[0]='Laptop'
# print(amazon_cart)

# #Matrix
# matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(matrix[0][1])

# List Methods            #adding
# basket=[1,2,3,4,5]
# print(len(basket))
# basket.append(100)     #append
# print(basket)
# basket.insert(4,100)   #insert
# print(basket)

# #List Methods              #Removing
# basket=[1,2,3,4,5]
# basket.pop()               #removes last item from the list
# print(basket)              #poping
# basket.pop(0)
# print(basket)              #Removes the first item from the list
# basket.remove(3)           #removes the given value in the bracket from the list
# print(basket)
# basket.clear()             #completly empties the list
# print(basket)

# #List Traversing-1
# letters=['a','b','c','d','e','f']
# print(letters.index('d'))   #find index of the key
# print(letters.index('d', 0 , 7))
# print('f' in letters)        #to find if thee key is in the list or not
# print('j' in letters)
# print('i' in  'Hi my name is aryan')
# print(letters.count('d'))     #counts the no of times a key has repeated

# #List Traversing-2
# num=['1','2','6','5','4','3']
# num.sort()            #sorts the elements in the list{Modifiess the list}
# print(num)            #we can also use 'print(sorted(num))' to display the sorted list without modifiying the actual list
# num.reverse()
# print(num)            #reverses the index of element in the list
# print(num[::-1])      #does not modify the list
# print(list(range(1,100)))      #to print elements in certain range

# #List Unpacking
# a,b,c,*other=[1,2,3,4,5,6,7,8,9]
# print(a)
# print(b)
# print(c)
# print(*other)

# #Dictionary
# dictionary={
#     'a':1,
#     'b':2
# }
# print(dictionary['b'])

# #Dictionary in a list
# my_list=[
#     {
#         'a':[1,2,3],
#         'b':'Hello!',
#         'c': True
#     },
# {
#         'a':[4,5,6],
#         'b':'Bye!',
#         'c': False
#     }
# ]
# print(my_list[0]['a'][1])

# #Dictionary Methods
# user={
#     'basket':[1,2,3],
#     'Greet':'Hello!'
# }
# print(user['basket'])
# print(user.get('basket'))  #To find is the key is avliable in the Dictionary
# print('basket' in user)
# print('Hello!' in user)              #searches the elements only from the keys columns
# print(('Hello!' in user.values()))   #used to find elements from the values section
# print(('Hello!' in user.items()))    #used to find elements from both  values and keys
# user.update({'basket': [1, 2, 3, 4]}) # also adds new element
# print(user)

# #Tuple
# my_tuple=(1,2,3,4,5,5,5)
# print(my_tuple.count(5))
# print(my_tuple.index(5))

# #sets
# my_set={1,2,3,4,5,5,4}
# print(my_set)
# my_set.add(6)
# print(my_set)

# Set Functions
# my_set = {1, 2, 3, 4, 5}
# your_set = {4, 5, 6, 7, 8, 9, 10, 11}
# print(my_set.difference(your_set))         #prints elements unique in set my_set
# your_set.discard(11)
# print(your_set)                            #discards the entered element from the set
# my_set.difference_update(your_set)
# print(my_set)                              #does the same job as difference but modifies the list
# print(my_set.intersection(your_set))
# print(my_set.isdisjoint(your_set))          #tells if there are common elements in the sets
# print(my_set.union(your_set))               #union of two sets
# print(my_set.issubset(your_set))             #tells if the first set is a subset of another
# print(my_set.issuperset(your_set))  # tells if the first set is a superset of another

#####################################################################################################################################################################
# x=int(input("Enter the length of the series:"))
# num1=0
# num2=1
# for i in range(0,x):
#     fibonacci=num1+num2
#     num2=num1
#     num1=fibonacci
#     print(fibonacci)

def my_list(num):
    list=[]
    for i in range(num):
        list.append(i*2)
    print( list)

new_list=my_list(50)





