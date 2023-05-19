# Ejercicio de verificación de paréntesis: 
# Escribe una función que tome una cadena que contiene paréntesis, corchetes y llaves, y verifique si los paréntesis 
# están balanceados. Es decir, que cada paréntesis abierto tenga su correspondiente paréntesis cerrado en el orden correcto.
# Utiliza una pila para llevar un seguimiento de los paréntesis abiertos y cierra el último 
# paréntesis abierto si se encuentra un paréntesis cerrado.
#tDescriptivo nombre variables
#romper if

def check_parentheses (equations):
    stack = [] #Cola donde vamos a almacenar los parentesis
    peers = {')': '(', ']': '[', '}': '{'}  # Diccionario que contiene los pares de paréntesis, corchetes y llaves
    
    for element in equations:
        if element in '([{':
            stack.append(element)  # Si es un paréntesis abierto, lo agregamos a la pila
        elif element in ')]}':
            if not stack or stack[-1] != peers[element]: # Verificamos si la pila esta vacía, en el caso de que la pila este vacía, verificamos el ultimo elemento de la pila (ultimo parentesis abierto) y
                #si no coincide con los elementos  
                return False  # Si encontramos un paréntesis cerrado y la pila está vacía o el último paréntesis abierto no coincide, retornamos False
            stack.pop()  # Si el paréntesis cerrado coincide con el último paréntesis abierto, lo eliminamos de la pila
    
    return len(stack) == 0  # Si la pila está vacía al final, significa que todos los paréntesis están balanceados

# equations = input("Ingresa una ecuación: ")
# print(check_parentheses(equations))
