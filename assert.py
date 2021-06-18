def divisor(num):
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    x = True
    while x == True:
        num = int(input("Ingresa un número: "))
        # assert num.isnumeric(), "Debes ingresar un número"
        assert num > 0, "Debes ingresar un número positivo"
        print(divisor(num))
        print("Terminó el programa")
        x = False
        
if __name__=="__main__":
    run()