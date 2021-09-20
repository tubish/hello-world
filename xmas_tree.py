tree_height = int(input('How tall is the tree ?:'))
i = 1
while i <= tree_height:
    print(' ' * (tree_height - i), '#' * (i + (i - 1)))
    i += 1
else:
    print(' ' * (tree_height - 1), '#')