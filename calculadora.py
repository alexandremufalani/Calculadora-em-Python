operation = input('''
Por favor, digite a operação matemática que você gostaria de completar:
+ para adição
- para subtração
* para multiplicação
/ para divisão
''')

number_1 = int(input('Digite o primeiro número: '))
number_2 = int(input('Digite o segundo número: '))

if operation == '+':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)

elif operation == '-':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)

elif operation == '*':
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)

elif operation == '/':
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)

else:
    print('Você não digitou um operador válido, por favor, execute o programa novamente.')

... 
# Define again() function to ask user if they want to use the calculator again
def again():

    # Take input from user
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    # If user types Y, run the calculate() function
    if calc_again == 'Y':
        calculate()

    # If user types N, say good-bye to the user and end the program
    elif calc_again == 'N':
        print('See you later.')

    # If user types another key, run the function again
    else:
        again()
def again():
    calc_again = input('''
Você quer calcular de novo?
Por favor, tecle S para SIM ou N para NÃO.
''')

    # Accept 'y' or 'Y' by adding str.upper()
    if calc_again.upper() == 'S':
        calculate()

    # Accept 'n' or 'N' by adding str.upper()
    elif calc_again.upper() == 'N':
        print('See you later.')

    else:
        again()

def calculate():
    operation = input('''
Por favor, digite a operação matemática que você gostaria de completar:
+ para adição
- para subtração
* para multiplicação
/ para divisão
''')

    number_1 = int(input('Digite o primeiro número: '))
    number_2 = int(input('Digite o segundo número: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('Você não digitou um operador válido, por favor, execute o programa novamente.')

    # Add again() function to calculate() function
    again()

def again():
    calc_again = input('''
Você quer calcular de novo?
Por favor, tecle S para SIM ou N para NÃO.
''')

    if calc_again.upper() == 'S':
        calculate()
    elif calc_again.upper() == 'N':
        print('                 Até logo.')
    else:
        again()

calculate()

# Direitos Autorais
print(''
      '')
print(''
      '')
print('  Version 1.0')
print(''
      '')
print('Copyright © 2019 Alexandre Mufalani® Todos os Direitos Reservados')
