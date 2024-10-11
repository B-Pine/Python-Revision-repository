def print_backward(*args, **kwargs):
    end_character = kwargs.pop('end', '\n')
    sep_character = kwargs.pop('sep', ' ')
    for arg in args[:0:-1]:
        print(f"{arg[::-1]}", end=sep_character, **kwargs)
    print(args[0][::-1], end=end_character, *kwargs)


# with open('backwards.txt', 'w') as backward:
#     print_backward("hello", "planets", "please take", "me to earth", end='\n', sep="**")

print("hello", "planets", "please take", "me to earth", end='', sep="\n**\n")
print_backward("hello", "planets", "please take", "me to earth", end='', sep="\n**\n")

