print('\n====================================================')

print('           $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
print('           $$$$$$$$$$$$$$$$$$$$$$$$_____$$$$')
print('           $$$$_____$$$$$$$$$$$$$$$_____$$$$')
print('           $$$$_____$$$$$$$$$$$$$$$_____$$$$')
print('           $$$$_____$$____$$$____$$_____$$$$')
print('           $$$$_____$______$______$_____$$$$')
print('           $$$$_____$______$______$_____$$$$')
print('           $$$$_____$____$$$$$$$$$$$$$$$$$$$')
print('           $$$$_____$___$$___________$$$$$$$')
print('           $$$$_____$__$$_______________$$$$')
print('           $$$$__________$$_____________$$$$')
print('           $$$$___________$$___________$$$$$')
print('           $$$$___________$$___________$$$$$')
print('           $$$$___________$$___________$$$$$')
print('           $$$$___________$$___________$$$$$')
print('           $$$$_____________$_________$$$$$$')
print('           $$$$$_____________________$$$$$$$')
print('           $$$$$$___________________$$$$$$$$')
print('           $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')


print('\n╔═══════════════════════════════════════════════════╗')
print('║           ----Piedra Papel o Tijera----           ║')
print('╚═══════════════════════════════════════════════════╝')

import random
# Opciones validas
OPCIONES = ("piedra", "papel", "tijera")

# Funcion para obtener la jugada del computador
def jugada_computador():
    return random.choice(OPCIONES)

# Funcion para determinar el ganador
def ganador(jugada_usuario, jugada_computador):
    if jugada_usuario == jugada_computador:
      return "Empate!😑"

    elif jugada_usuario == "piedra":
        if jugada_computador == "tijera":
          return "Ganaste!!😁"
        else:
          return "Perdiste!😵"

    elif jugada_usuario == "papel":
        if jugada_computador == "piedra":
          return "Ganaste!!😁"
        else:
          return "Perdiste!😵"

    elif jugada_usuario == "tijera":
        if jugada_computador == "papel":
          return "Ganaste!!😁"
        else:
          return "Perdiste!😵"

# Obtiene la jugada del usuario
while True:
    try:
        jugada_usuario = input("\nTu jugada: ")
        if jugada_usuario not in OPCIONES:
            raise ValueError("Entrada invalida: Debe ser piedra, papel o tijera")
        break
    except ValueError as x:
        print(x)

# Obtiene la jugada del computador
jugada_computador = jugada_computador()

# Muestro las jugadas y el resultado

print(f"Computador jugó {jugada_computador}")
print('\n'  ,ganador(jugada_usuario,jugada_computador))
print('\n====================================================')
