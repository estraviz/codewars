"""8kyu interpreters: HQ9+
"""


def HQ9(code):
    if code == 'H':
        return "Hello World!"
    elif code == 'Q':
        return code
    elif code == '9':
        num = 99
        output = ""
        while(num >= 0):
            var1 = f'{str(num) if num > 0 else "No more"}'
            var2 = "" if num == 1 else "s"
            var3 = num - 1 if num - 1 > 0 else "no more"
            var4 = "" if num - 1 == 1 else "s"
            output += f'{var1} bottle{var2} of beer on the wall, {str(var1).lower()} bottle{var2} of beer.\n'
            if num > 0:
                output += f'Take one down and pass it around, {var3} bottle{var4} of beer on the wall.\n'
            else:
                output += f'Go to the store and buy some more, 99 bottles of beer on the wall.'
            num -= 1
        return output
    return None
