# Trabajo integrador Semana II - Matemática y Programación I
# Aplicación de lo plasmado en el PDF llevado al código mediante Python
# Se trabaja en base a las expresiones lógicas planteadas sobre los diferentes conjuntos conformados por los DNI generados

# Definición de los conjuntos formados por los dígitos únicos de cada DNI
A = {1, 3, 6, 7, 8, 9}
B = {0, 2, 4, 5, 6, 8, 9}
C = {1, 2, 3, 5, 6}
D = {0, 2, 3, 4, 7, 8}
E = {1, 2, 3, 4, 5}
conjuntos = [A, B, C, D, E]  # Lista que agrupa todos los conjuntos para facilitar su recorrido

print("Operaciones entre conjuntos: ")

# Operaciones entre conjuntos - Se verifica que los resultados coincidan con los planteados en el trabajo práctico

# Unión entre A y B (elementos que están en A, en B o en ambos)
union_AB = A | B
print('A U B: ', union_AB)

# Intersección entre C y D (elementos que están en ambos conjuntos)
interseccion_CD = C & D
print('C n D: ', interseccion_CD)

# Diferencia entre B y C (elementos que están en B pero no en C)
diferencia_BC = B - C
print('B - C: ', diferencia_BC)

# Diferencia simétrica entre D y E (elementos que están en uno solo de los conjuntos, pero no en ambos)
dif_simetrica_DE = D ^ E
print('D Δ E: ', dif_simetrica_DE)

# Evaluación e implementación de las expresiones lógicas planteadas en el trabajo práctico

print("Evaluaciones e implementación de las expresiones lógicas planteadas: ")
print("Expresión lógica 1: Alta diversidad numérica")

# Expresión lógica 1: Todos los conjuntos tienen al menos 5 elementos
if all(len(c) >= 5 for c in conjuntos):
    print('Alta diversidad numérica: Todos los conjuntos tienen al menos 5 elementos')

print("Expresión lógica 2: Grupo impar - Mayoría con cantidad impar")

# Expresión lógica 2: Se calcula cuántos conjuntos tienen cantidad impar de elementos
impares = sum(1 for c in conjuntos if len(c) % 2 != 0)
pares = len(conjuntos) - impares
if impares > pares:
    print('Grupo impar: Hay más conjuntos con cantidad impar de elementos.')

print("Expresión lógica 3: Relación entre pares")

# Expresión lógica 3: Se evalúa si hay pares de conjuntos que comparten al menos 4 elementos
letras = ["A", "B", "C", "D", "E"]  # Identificadores de los conjuntos
for i in range(len(conjuntos)):
    for j in range(i + 1, len(conjuntos)):
        comunes = conjuntos[i] & conjuntos[j]  # Intersección entre dos conjuntos
        if len(comunes) >= 4:
            print(f' {letras[i]} y {letras[j]} están relacionados (comparten: {comunes})')

print("Expresión lógica 4: Grupo con cero dentro de sus elementos")

# Expresión lógica 4: Se verifica si algún conjunto contiene el número 0
if any(0 in c for c in conjuntos):
    print('Hay al menos un grupo con cero dentro de sus elementos')

print("Expresión lógica 5: Dominancia del dígito 3")

# Expresión lógica 5: Se cuenta cuántos conjuntos contienen el dígito 3
apariciones_3 = sum(1 for c in conjuntos if 3 in c)
if apariciones_3 >= 3:
    print('Dominancia del dígito 3: Aparece en: ', apariciones_3, " conjuntos.")

# Lista de DNIs como cadenas de texto, para analizar individualmente cada uno
dnis = ["38161719", "46908852", "32612165", "40802037", "23135244"]

print("Análisis de cada DNI:")

# Se analiza cada DNI para calcular la suma total de sus dígitos y la frecuencia de cada uno (0 a 9)
for i, dni in enumerate(dnis): # enumerate(dnis) devuelve tanto el índice (i) como el valor (dni) de cada elemento en la lista.
    suma = 0  # Inicializa la suma de los dígitos del DNI
    frecuencias = {str(d): 0 for d in range(10)}  # Inicializa el diccionario con claves del 0 al 9

    # Recorre cada dígito del DNI (como texto), lo convierte a número y actualiza suma y frecuencia
    for digito in dni:
        suma += int(digito)
        frecuencias[digito] += 1

    # Muestra los resultados obtenidos para cada DNI
    print(f"DNI {i+1}: {dni}")
    print(f"  ➤ Suma de dígitos: {suma}")
    print(f"  ➤ Frecuencia de cada dígito:")
    for d in range(10):
        print(f"     - {d}: {frecuencias[str(d)]}")
    print()
