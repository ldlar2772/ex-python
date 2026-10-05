l = []

x = input('digite uma palavra: ')
x = list(x)
l.append(x)
print(l)
sem_vogais = [letra for letra in x if l not in 'aeiou']
print(sem_vogais)
