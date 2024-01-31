import random
import time
import os
os.system('clear')
 
## Listas de Palabras
archivo = open("/home/javier/Escritorio/spanish.lst")
archivo_read = archivo.read()
archivo_leido = archivo_read.split()
cantidad_letras = 0

dibujo_del_ahorcado = ['''
      +---+
      |   |
      O   |
    ----- |
     /|\  |
     / \  |
    =========''','''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''','''
      +---+
      |   |
      O   |
      |   |
     / \  |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
          |
          |
          |
          |
    =========''']

def ahorcado_dibujo ():
    if vidas == 0:
        print(dibujo_del_ahorcado[0])
    if vidas == 1:
        print(dibujo_del_ahorcado[1])
    if vidas == 2:
        print(dibujo_del_ahorcado[2])
    if vidas == 3:
        print(dibujo_del_ahorcado[3])
    if vidas == 4:
        print(dibujo_del_ahorcado[4])
    if vidas == 5:
        print(dibujo_del_ahorcado[5])

print("|--------------------------------------------------------------------------------------|")
print("|                    BIENVENIDO AL JUEGO DEL AHORCADO                                  |")
print("|--------------------------------------------------------------------------------------|")
time.sleep(1)
print("|     El objetivo del juego es adivinar la palabra secreta letra por letra             |")
print("|                                                                                      |")
time.sleep(1)
print("|          Tienes 5 vidas, pierdes una vida por cada letra que no aciertes             |")
print("|                                                                                      |")
time.sleep(1)
print("|                    >>> Si te quedas sin vidas pierdes <<<                            |")
print("|                                                                                      |")
time.sleep(1)
print("|      Elige el nivel de dificultad: presiona F (fácil), N (normal) o D (dificil)      |")
print("|                                                                                      |")
time.sleep(1)
print("|--------------------------------------------------------------------------------------|")
print("| Nivel fácil = 100 puntos    Nivel normal = 200 puntos    Nivel dificil = 300 puntos  |")
print("|--------------------------------------------------------------------------------------|")
time.sleep(1)
print("|                                                                                      |")
print("|     Por cada vida que pierdas se te descontará un 20 por ciento de la puntuación.    |")
print("|                                                                                      |")
print("|--------------------------------------------------------------------------------------|")
time.sleep(1)
time.sleep(1)
 
nivel_dificultad = input(">>>  Ingrese F (fácil), N (normal) o D (difícil): ")

palabras_secretas_faciles = []
palabras_secretas_normales = []
palabras_secretas_dificiles = []
palabra_secreta = ""

for palabra in archivo_leido:
    if len(palabra) <= 6:
        palabras_secretas_faciles.append(palabra)

for palabra in archivo_leido:
    if len(palabra) > 6 and len(palabra) < 15:
        palabras_secretas_normales.append(palabra)  

for palabra in archivo_leido:
    if len(palabra) >= 15:
        palabras_secretas_dificiles.append(palabra)  

puntaje = 0

while True:
    if nivel_dificultad.upper() == "F":
        os.system('clear')
        print("Excelente, seleccionaste el nivel FÁCIL. Tu puntaje es: 100")
        palabra_secreta = random.choice(palabras_secretas_faciles)
        puntaje = 100 
        break
    elif nivel_dificultad.upper() == "N":
        os.system('clear')
        print("Excelente, seleccionaste el nivel NORMAL. Tu puntaje es 200")
        palabra_secreta = random.choice(palabras_secretas_normales)
        puntaje = 200
        break
    elif nivel_dificultad.upper() == "D":
        os.system('clear')
        print("||Excelente, seleccionaste el nivel DIFÍCIL. Tu puntaje es: 300")
        palabra_secreta = random.choice(palabras_secretas_dificiles)
        puntaje = 300       
        break
 
    else:
        os.system('clear')
        print("Por favor selecciona un nivel de dificultad válido")
        print()
        nivel_dificultad = input("Ingresa F (fácil), N (normal) o D (difícil):")
 
 
 
## Es el numero de veces que se puede eqivocar
vidas = 5
lista_letras_adivinadas = []
 
## Imprimimos la palabra sin letras
ahorcado_dibujo ()
print()
print('_ ' * len(palabra_secreta), "(La palabra tiene", len(palabra_secreta), "letras", ")")
 
while True:
 
    while True:
        print()
        letra_adivinada = input("Adivina una letra:").lower()
        if len(letra_adivinada) > 1 or letra_adivinada.isnumeric():
            os.system('clear')
            print("Eso no es una letra, intenta con una sola letra")
            ahorcado_dibujo ()
            print()
            print('_ ' * len(palabra_secreta), "(La palabra tiene", len(palabra_secreta), "letras", ")")
        else:
            if letra_adivinada.lower() in lista_letras_adivinadas:
                os.system('clear')
                print("Ya habias intentado con esa letra, intenta con otra por favor")
                ahorcado_dibujo ()
                print()
                print('_ ' * len(palabra_secreta), "(La palabra tiene", len(palabra_secreta), "letras", ")")
            else:
                lista_letras_adivinadas.append(letra_adivinada)
 
                if letra_adivinada.lower() in palabra_secreta:
                    os.system('clear')
                    print("Felicidades, adivinaste una letra.", "Tu puntaje es:",(puntaje))
                    (print)
                    ahorcado_dibujo ()
                    break
                else:
                    vidas = vidas-1
                    if "f" in nivel_dificultad:
                        puntaje = puntaje - 20
                    elif "n" in nivel_dificultad:
                        puntaje = puntaje - 40
                    elif "d" in nivel_dificultad:
                         puntaje = puntaje - 60
                    os.system('clear')
                    print("Te equivocaste, te quedan",(vidas),"vidas.","Tu puntaje ahora es:",(puntaje)) 
                    ahorcado_dibujo ()                          
                    break
 
    if vidas==0:
        print()
        print("Te quedaste sin vidas y perdiste. La palabra secreta era: "+ palabra_secreta)
        print()
        print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("|     G A M E   O V E R    |")
        print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print()
        break
 
 
    estatus_actual = ""
 
    letras_faltantes = 0
    for letra in palabra_secreta:
 
 
        if letra in lista_letras_adivinadas:
            estatus_actual = estatus_actual + letra
 
        else:
            estatus_actual = estatus_actual + "_ "
            letras_faltantes = letras_faltantes + 1
    estatus_actual = estatus_actual.upper()
    ## Imprimir palabra con algunas letras
    print()
    print(estatus_actual)
 
 
    if letras_faltantes == 0:
        print()
        print("¡Felicidades, ganaste!. La palabra secreta era: ",(palabra_secreta))
        print()
        print("¡Vamos con otra palabra!")
        palabra_secreta = random.choice(palabras_secretas_faciles)
        lista_letras_adivinadas = []
        time.sleep(7)
        os.system('clear')
        print("Intenta adivinar la siguiente palabra. Tu puntaje es:",(puntaje))
        ahorcado_dibujo ()
        print()
        print('_ ' * len(palabra_secreta), "(La palabra tiene", len(palabra_secreta), "letras", ")")

