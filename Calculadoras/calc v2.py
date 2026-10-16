class Calculadora:
    def __init__(self, num1, opera, num2) -> None:
        self.num1 = num1
        self.opera = opera
        self.num2 = num2

    def calcular(self) -> None:
        try:
            if self.opera == '+':
                return self.num1 + self.num2
            elif self.opera == '-':
                return self.num1 - self.num2
            elif self.opera == '*':
                return self.num1 * self.num2
            elif self.opera == '/':
                return self.num1 / self.num2
        except ZeroDivisionError:
            return 'Nao se divide por zero, tente novamente.'
        except TypeError:
            return 'Erro: Certifique-se de que inseriu numeros / operadores validos.'
        
while True:
    try:
        num1:float = float(input('Digite o primeiro numero: '))
        opera:str = input('Digite o operador (+, -, *, /): ')
        num2:float = float(input('Digite o segundo numero: '))
        calc:Calculadora = Calculadora(num1, opera, num2)
        print(calc.calcular())
    except ValueError:
        print('Erro: Certifique-se de que inseriu numeros / operadores validos.')
    continuar:str = input('Deseja continuar? (s/n): ')
    if continuar == 'n':
        break
