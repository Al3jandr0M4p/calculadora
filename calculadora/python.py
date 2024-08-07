import signal
import sys
import time
from colorama import Fore, Style, init

init()

def def_handler(signum, frame):
    print(f'\n\n{Fore.RED}{Style.BRIGHT}Saliendo...{Style.RESET_ALL}\n')
    time.sleep(1)
    sys.exit(1)

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def potencia(a, b):
    return a ** b

def dividir(a, b):
    return a / b

def divicionAvanzada(a, b):
    return a // b

def main():
    signal.signal(signal.SIGINT, def_handler)
    calculos = []

    while True:
        print(f"""{Fore.GREEN}{Style.BRIGHT}
                 ██████╗  █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗ 
                ██╔════╝ ██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝ 
                ██║  ███╗███████║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗
                ██║   ██║██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║
                ╚██████╔╝██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝
                ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
        {Style.RESET_ALL}""")
        
        print('Estas en el sistema de calculo donde puedes (sumar/restar/multiplicar/dividir/divicionAvanzada/potencia/ver_calculos/salir)\nQue quieres hacer ?')
        opcion_calculadora = str(input(': '))
        
        if opcion_calculadora in ['exit', 'salir']:
            signal.raise_signal(signal.SIGINT)
        
        if opcion_calculadora == 'sumar':
            primer_num = int(input('Elige el primer numero a sumar: '))
            second_num = int(input('Elige el segundo numero a sumar: '))
            result = sumar(primer_num, second_num)
            print(result)
            calculos.append(f"Calculos de la operacon matematica:\n{primer_num} + {second_num} = {result}")
            
        elif opcion_calculadora == 'restar':
            primer_num = int(input('Elige el primer numero a restar: '))
            second_num = int(input('Elige el segundo numero a restar: '))
            result = restar(primer_num, second_num)
            print(result)
            calculos.append(f"Calculos de la operacon matematica:\n{primer_num} + {second_num} = {result}")
            
        elif opcion_calculadora == 'multiplicar':
            primer_num = int(input('Elige el primer numero a multiplicar: '))
            second_num = int(input('Elige el segundo numero a multiplicar: '))
            result = multiplicar(primer_num, second_num)
            print(result)
            calculos.append(f"Calculos de la operacon matematica:\n{primer_num} + {second_num} = {result}")
            
        elif opcion_calculadora == 'potencia':
            primer_num = int(input('Elige el primer numero a potenciar: '))
            second_num = int(input('Elige el segundo numero a potenciar: '))
            result = potencia(primer_num, second_num)
            print(result)
            calculos.append(f"Calculos de la operacon matematica:\n{primer_num} + {second_num} = {result}")
            
        elif opcion_calculadora == 'dividir':
            primer_num = int(input('Elige el primer numero a dividir: '))
            second_num = int(input('Elige el segundo numero a dividir: '))
            result = dividir(primer_num, second_num)
            print(result)
            calculos.append(f"Calculos de la operacon matematica:\n{primer_num} + {second_num} = {result}")
        
        elif opcion_calculadora == 'divicionAvanzada':
            primer_num = int(input('Elige el primer numero para la divicionAvanzada: '))
            second_num = int(input('Elige el segundo numero la divicionAvanzada: '))
            result = divicionAvanzada(primer_num, second_num)
            print(result)
            calculos.append(f"Calculos de la operacon matematica:\n{primer_num} + {second_num} = {result}")
        
        elif opcion_calculadora == 'ver_calculos':
            with open('calculos.txt', 'w') as calculos_matematicos:
                for calculo in calculos:
                    calculos_matematicos.write(calculo + "\n")
            print(f"{Fore.GREEN}Los cálculos realizados se han guardado en 'calculos.txt'{Style.RESET_ALL}")

if __name__ == '__main__':
    main()
