my_str = input('Enter a string in uppercase to hide: ')

#print(my_str)
#print(len(list1))
#print(list1[0])

list1 = []

i=0
while i in range(len(my_str)):
    #print(ord(my_str[i]))
    list1.append(ord(my_str[i]))

    i+=1


list2= [str(n) for n in list1]
print(''.join(list2))

i = 0
list2 = []
while i in range(len(list1)):
    #print(chr(list1[i]))
    list2.append(chr(list1[i]))

    i += 1

#print(list2)

print('Original Message: ' , ''.join(list2))