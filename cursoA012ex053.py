palindromo = input('digite uma palavra: ')
palindromo = palindromo.replace(' ', '').lower()
if palindromo == palindromo[::-1]:
    print('é um palindromo')
else:
    print('não é um palindromo')
    