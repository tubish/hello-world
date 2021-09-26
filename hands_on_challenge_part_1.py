# challange 1
"""
my_num = int(input('Enter a number: '))

def divisors(my_num):
    l1 = []
    for record in range(1, my_num):
        if (my_num % record) == 0:
            l1.append(record)
    return l1



print(divisors(my_num))
"""


# # challenge 2
"""
nums = '10,20,30,40,50'
#with function

def turn_into_int(nums):
    l1=[]
    for i in (nums.split(',')):
        l1.append(int(i))
    return l1

print(turn_into_int(nums))


#witout function

nums_list = (nums.split(','))

num1 = [int(i) for i in nums_list]

print(num1)
"""

# challange 3
"""
nums = []
for i in range(1500,3201):
    if i % 7 == 0 and i % 5 != 0:
        nums.append(str(i))

print(nums)
"""

# challange 4

"""
my_str =  input('Enter a sentence here : ')

words_list = my_str.split(' ')

words_reversed = ' '.join(reversed(words_list))
print(words_reversed) 
"""

# challange 5

"""
my_str = input('Enter hyphen-separated sequence of words: ')
my_str_list = sorted(my_str.split('-'))

print('-'.join(my_str_list))
"""

#challange 6

"""
my_str = input('Enter a text: ')

my_str_split = my_str.split()

i = 0
l1 = []
while i < len(my_str_split):
    l1.append(my_str_split[i][::-1])
    i += 1

new_my_str = ' '.join(l1)

print(new_my_str)
"""


#challange 7
"""
# Write a Python program that accepts a hyphen-separated sequence of words as input and prints
# the words in a hyphen-separated sequence after sorting them alphabetically.


string = input("Enter a few words separated by whitespaces: ")
words = string.split()

# reverse the letters in each word
words = [w[::-1] for w in words]

new_str = ' '.join(words)

print(new_str)
"""

#challange 8
"""
words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']


lenght_of = []
i=0
for word in words:
    lenght_of.append(len(word))
    i+=1
print(tuple(zip(words,lenght_of)))


words_and_length = [(w, len(w)) for w in words]

print(words_and_length)
"""

#challange 9
"""
words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']


lenght_of = []
i=0
for word in words:
    lenght_of.append(len(word))
    i+=1
print(dict(zip(words,lenght_of)))

words_and_length = dict()

for w in words:
    words_and_length[w] = len(w)

print(words_and_length)
"""


#challange 10
"""

names = ["Dan", "John", "Diana"]
phones = [11111, 2222, 3333]

result = set(zip(names, phones))

print(result)

"""