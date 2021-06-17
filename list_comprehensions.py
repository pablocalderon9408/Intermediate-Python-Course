def run():

    # square = []
    # for i in range(1,101):
    #     if i % 3 == 0:
    #         continue
    #     else:
    #         square.append(i**2)  

    square = [i**2 for i in range(1,101) if i % 3 != 0]
    print(square)
    
if __name__ == '__main__':
    run()






    