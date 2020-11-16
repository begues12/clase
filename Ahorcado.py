import random

Vidas = 7

Palabras = ['hola','cangrejo','poni','caballo']     #Palabras posibles

Palabra = Palabras[ random.randint(0,len(Palabras) - 1) ]   #Palabra a acertar

LetrasBol = []      #Detector de palabra

Secreta = []        #Palara por guiones
Guion = len(Palabra)    #Numero de letras
x = 0
ganado = False
pedir_letra = True
Ronda = 0

while Guion > x:

    LetrasBol.append(False)
    Secreta.append("-")
    x += 1

#Codigo de juego


i = 0

Error = False


while Vidas != 0:

    if ganado == False:

        Ronda += 1

        print("======================================== " + str(Ronda))

        if pedir_letra == True:

            print(Secreta)
            Pregunta = input("Dime una letra:")

        Error = True

        while i < len(Palabra):

            if Pregunta == Palabra[i]:

                LetrasBol[i] = True
                Secreta[i] = Palabra[i]
                Error = False

            i += 1

        if Error:

            Vidas -= 1

            print("========================================")

            if Vidas == 6:

                print(" | ")

            if Vidas == 5:

                print(" | ")
                print(" O ")

            if Vidas == 4:
                print(" | ")
                print(" O ")
                print(" | ")

            if Vidas == 3:

                print(" | ")
                print(" O ")
                print("(| ")

            if Vidas == 2:

                print(" | ")
                print(" O ")
                print('(|)')

            if Vidas == 1:

                print(" | ")
                print(" O ")
                print('(|)')
                print("/")

            if Vidas == 0:
                print(" | ")
                print(" O ")
                print('(|)')
                print("//")
                print("Perdiste wacho")



            Error = False

        i = 0

        ganado = True

        for Win in LetrasBol:

            if Win == False:

                ganado = False

    else:

        print("Eres il' put* amo")
        break







