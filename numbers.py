def graphic_number(s):
    if (s.isdigit() == False):
        return None
    d = [
        ('0', '█▀▀█', '█  █', '█  █', '█▄▄█'),
        ('1', '▀▀█ ', '  █ ', '  █ ', '▄▄█▄'),
        ('2', '▀▀▀█', '▄▄▄█', '█   ', '█▄▄▄'),
        ('3', '▀▀▀█', '▄▄▄█', '   █', '▄▄▄█'),
        ('4', '█ █ ', '█▄█▄', '  █ ', '  █ '),
        ('5', '█▀▀▀', '█▄▄▄', '   █', '▄▄▄█'),
        ('6', '█▀▀▀', '█▄▄▄', '█  █', '█▄▄█'),
        ('7', '▀▀▀█', '   █', '   █', '   █'),
        ('8', '█▀▀█', '█▄▄█', '█  █', '█▄▄█'),
        ('9', '█▀▀█', '█▄▄█', '   █', '▄▄▄█'),
    ]

    # creating d2
    d2 = []
    for i in s:
        d2.append(d[int(i)])

    # printing d2
    x = 1
    for i in range(4):
        for j in range(len(s)):
            print(d2[j][x], end=' ')
        print()
        x += 1
    return 1

s = input('Enter a number: ')

x = graphic_number(s)
if x == None:
    print('Wrong Input')
