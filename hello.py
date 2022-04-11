# este programa serve para escrever tudo o que aprendi sobre python
# usar hastag para escrever comentários que não aparecem no output
# escrever uma linha em branco = print ('')

# declarar uma variável : escrever o nome e se necessário mais do que um nome colocar "_" entre os nomes
name = 'Diana'
second_name = 'Isabel'

# para escrever no output utilizar print 
print ('Hello')

# para mandar a pessoa escrever no output usar input
horas = input('Que horas são?')
print('São ' + horas)
print('')

# juntar strings
print ('Hello' + ' ' + name + ' ' + second_name + ', são ' + horas)
print('')

# capitalize() = 'D'iana ,  upper() = 'DIANA' , lower() = diana
print(name.capitalize()) 
print(name.upper())
print(name.lower())

# strings formating
#output = 'Hello,  { }  { } '.format(name, second_name)
#output = 'Hello,  { 0 }  { 1 } '.format(name, second_name)
output = f'Hello,  {name} {second_name} ' # prefero este último
print(output)
print('')
# work wiht number 
# addition = + , subtration = - , multiplication = * , division = / , exponent = **
n1 = input ('Please write the first number')
n2 = input ('Please write the second number')

soma = (float(n1) + float(n2))
subtração = (float(n1) - float(n2))
multipliação = (float(n1) * float(n2))
divisão = (float(n1) / float(n2))
expoente = (float(n1)**2) #ao quadrado por exemplo

print(soma)
print(subtração)
print(multipliação)
print(divisão)
print(expoente)

# apagar ecrã = command + k 

# dates
from datetime import datetime, timedelta
from re import M
from this import d 

today = datetime.now()
print ('today is ' + str(today))

    #timedelta is used to define a period of time
one_day = timedelta(days=1)
yesterday = today - one_day
print('yesterday was ' + str(yesterday)) 
print('day: ' + str(today.day))
print ('month: ' + str(today.month))
print ('year: ' + str(today.year))

birthday = input ('when is your birday (dd/mm/yyyy)? ')
birthday_date = datetime.strptime(birthday, '%d/%m/%y')

print('Birthday ' + str(birthday_date))

# maior do que > , menor do que < , maior/menor ou igual >= / <=, igual ==, diferente !=

# a comparar strings 'canada' é diferente de CANADA, por isso usamos o .lower() na operação para ficar igual

# if e else (1 ou 2 condições) ,  if e elif (+ de 2 condições) (+ else se for diferente de todas as outras condições)
# if e or se as condições foram quase iguais (exemplo tas taxas no video - dois locais diferentes, taxas iguais)
# if ... in( ... , ... , ... ):

# array tem de ser numerico e tudo do mesmo tipo, lists pode ser qualquer coisa


