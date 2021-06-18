def divisor(num):
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    x = True
    while x == True:
        try:
            num = int(input("Ingresa un número: "))
            if num < 0:
                raise ValueError("No se reciben negativos")
                break
            print(divisor(num))
            print("Terminó el programa")
            x = False
        except ValueError:
            print("Ingresa un número entero positivo")

if __name__=="__main__":
    run()

