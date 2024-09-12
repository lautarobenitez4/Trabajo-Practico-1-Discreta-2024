conjuntos = [   "resumen de python del profe figueredo", #documento 1
                "la IA me da miedo", #documento 2
                "python es utilizado en la IA", #documento 3
                "tengo mucha inteligencia", #documento 4
                "python se usa en paradigmas 1" ] #documento 5

#Sean tomados como títulos de documentos de una pc, cada documento es un conjunto
#Cada palabra dentro de los titulos de cada documento son tomadas como un subconjunto dentro de la misma

subconjunto_a_buscar = "python" #almaceno la variable que quiero buscar

conjunto_busqueda = set(subconjunto_a_buscar.lower().split()) #separo por palabras y buscamos en minúsculas

coincidencias = set() #inicializa conjunto vacío para poder almacenar las coincidencias encontradas

def procesar_documento(texto): #comparamos documentos con el subconjunto de búsqueda
    return set(texto.lower().split())

#iteracion de documentos y transforma el documento en conjunto de palabras
for i, documento in enumerate(conjuntos): 
    conjunto_documento = procesar_documento(documento)
    interseccion = conjunto_busqueda & conjunto_documento #interseccion entre el conjunto ya separado por palabras y el subconjunto buscado 
    if interseccion:
        coincidencias.add(i + 1) #si hay palabras en común se agrega el indice del documento a las coincidencias
    if conjunto_busqueda.isdisjoint(conjunto_documento):
        print(f"el documento numero {i + 1} no tiene incluida la palabra buscada.") #si no hay palabras en comun se imprime el mensaje escrito
    if conjunto_busqueda.issubset(conjunto_documento):
        print(f"la palabra buscada está dentro del documento numero {i + 1}.") #verificacion 

print("Coincidencias:", coincidencias)