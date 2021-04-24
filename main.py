# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ''' Перечеление и замена функций, которые, по-моему, не нужны '''
    print('1.zfill():')
    n = 6
    s = 'hii'
    s1 = s.zfill(n)
    s2 = '0' * (n - len(s)) + s
    print(s1)
    print(s2)
    print('2.ljust():')
    print(s.ljust(n), 'world')
    print(s + ' ' * (n - len(s)), "world")
    print('3.isspace()')
    b = '   '
    print(b.isspace())
    b = '9 '
    print(b.isspace())

    ''' Перечеление и демонстрация работы функций, которые, по-моему, нужны '''
    print('1.count (): ')
    s = 'goggggooggoggggoooggoo'
    a = s.count('o')
    print('Количество вхождение "o" в данную строку', a)
    print('2.expandtabs()')
    s = s.expandtabs(2)
    print(s)
    print('3.replace()')
    txt = "hi, my Dear friend! hi hi"

    x = txt.replace("hi", "no")

    print(x)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
