# Ejercicio de verificación de paréntesis: 
# Escribe una función que tome una cadena que contiene paréntesis, corchetes y llaves, y verifique si los paréntesis 
# están balanceados. Es decir, que cada paréntesis abierto tenga su correspondiente paréntesis cerrado en el orden correcto.
# Utiliza una pila para llevar un seguimiento de los paréntesis abiertos y cierra el último 
# paréntesis abierto si se encuentra un paréntesis cerrado.

def check_parentheses (equation):
    open_brackets = [] 
    inverse_pair_brackets = {')': '(', ']': '[', '}': '{'}  
    for char in equation:
        if char in '([{':
            open_brackets.append(char) 
            continue
        has_not_open_bracket = open_brackets[-1] != inverse_pair_brackets.get(char)
        if char in ')]}' and (len(open_brackets) == 0 or has_not_open_bracket):
            return False
        if char in ')]}':
            open_brackets.pop()
    return len(open_brackets) == 0  
equation = input("Ingresa una ecuación: ")
print(check_parentheses(equation))
