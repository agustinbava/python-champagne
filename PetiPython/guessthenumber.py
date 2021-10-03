from random import randint

while True:

    number = randint(0,51)
    user = 0
    lifes = 1

    user = int(input("Adivina el número entre 0 y 50, tenes 5 intentos: "))

    while number != user and lifes < 5:
          
        if abs(user - number) >= 20:
            user = int(input("CONGELADO.\n Elegí otro numero: "))
            lifes += 1
            
        elif abs(user - number) < 20 and abs(user - number) >= 10:
            user = int(input("FRIO.\n Elegí otro numero: "))  
            lifes += 1 

        elif abs(user - number) < 10 and abs(user - number) >= 5:
            user = int(input("CALIENTE.\n Elegí otro numero: "))
            lifes += 1
            
        elif abs(user - number) < 5:
            user = int(input("MUY CALIENTE.\n Elegí otro numero: ")) 
            lifes += 1   
        
        if lifes == 4 and user < number:
            print("Es tu última oportunidad, una pista: probá con un número MAYOR")

        elif lifes == 4 and user > number:
            print("Es tu última oportunidad, una pista: probá con un número MENOR")    

    if number == user:
        print("\nGANASTE. EL NUMERO ERA {}. JUGUEMOS DE NUEVO:\n".format(number))
    else:
        print("\nPERDISTE. UTILIZASTE {} INTENTOS. EL NUMERO ERA {}".format(lifes,number))    

    