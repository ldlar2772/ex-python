mai = 0
men = 0 
for i in  range (7):
    x = int(input('-=-=-=-=-=-=-=-=-=-\nqual ano vc nasceu?\n-=-=-=-=-=-=-=-=-=-\n--> '))
    if x <= 2008:
        mai += 1
    else:
        men += 1
print(f'exatamente {mai}, ja sao de maior')
print(f'exatamente {men}, sao de menor')
   