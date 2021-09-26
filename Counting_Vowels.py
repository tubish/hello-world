#solution
def vowel_count(my_str):
    """
    This function counts the number of vowels in a string and returns a dictionary.
    """
    vowels = 'aeiou'
    my_str = my_str.lower()  # ignoring the case (we consider only lower-case letters)
    result = dict()
    for record in my_str:
        if record in vowels:
            if record in result.keys():
                result[record] += 1
            else:
                result[record] = 1
    return result



# Tuba#s function

def vowel_count2(my_str):
        l1 = []
        l2 = []
        my_str = my_str.lower()
        vowels = 'aeiou'
        for record in my_str:
            if record in vowels:
                l1.append(my_str.count(record))
                l2.append(record)
        return dict(zip(l2, l1))


r = vowel_count('Awesome')
print(r)    # => {'a': 1, 'e': 2, 'o': 1}


print(vowel_count2('Awesome'))


def counter(my_str):
    vowels = 'aeuoi'
    l1 = []
    l2 = []
    my_str = my_str.lower()
    for record in my_str:
        if record in vowels:
            l1.append(1) #not to count same letters more than once
        else:
            l2.append(1)
    return sum(l1), sum(l2)


print(counter('Beautiful'))


