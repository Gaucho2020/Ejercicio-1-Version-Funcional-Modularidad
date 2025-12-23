alineación = 0                  # Variable global iniciada en 0

def adelante(ancho):            #Función para ir adelante
    global alineación
    print(" " * alineación + " —" * ancho + "┐")
    alineación += ancho * 2      # Posición actualizada adelante

def abajo(alto):                 #Función para ir abajo
    global alineación
    for _ in range(alto):
        print(" " * alineación + "|")
    print(" " * alineación + "🐢")

def reinicio():                  # Función para reiniciar la posición a 0
    global alineación
    alineación = 0