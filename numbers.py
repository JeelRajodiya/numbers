class G1:

    def convert(self, num_str):

        def graphic_num(no):

            d = {'1': ['▀▀█ ', '  █ ', '  █ ', '▄▄█▄'], '2': ['▀▀▀█', '▄▄▄█', '█   ', '█▄▄▄'],
                 '3': ['▀▀▀█', '▄▄▄█', '   █', '▄▄▄█'], '4': ['█ █ ', '█▄█▄', '  █ ', '  █ '],
                 '5': ['█▀▀▀', '█▄▄▄', '   █', '▄▄▄█'], '6': ['█▀▀▀', '█▄▄▄', '█  █', '█▄▄█'],
                 '7': ['▀▀▀█', '   █', '   █', '   █'], '8': ['█▀▀█', '█▄▄█', '█  █', '█▄▄█'],
                 '9': ['█▀▀█', '█▄▄█', '   █', '▄▄▄█'], '0': ['█▀▀█', '█  █', '█  █', '█▄▄█'], }

            d2 = []
            d1 = ""
            # Adding each number representation to a list
            for n in num_str:
                for i in d[n]:
                    d2.append(i)
            l = len(num_str)

            # Printing Funtion
            for i in range(4):  # rows
                for j in range(l):  # columns
                    d1 += d[num_str[j]][i]+" "
                d1 += "\n"
            return d1

        # Some bug catching
        if num_str.isnumeric():
            print(f"\n{graphic_num(num_str)}\n")
        else:
            # "\u0332" after a character gives it an underline in unicode.
            print(f"\n The string you have entered should o\u0332n\u0332l\u0332y\u0332 have positive numbers,\n Please rerun the program and try again!\n")


if __name__ == "__main__":
    a = G1()
    n = input(f"\nPlease enter the string that you want to convert to Graphics: ")
    a.convert(n)
