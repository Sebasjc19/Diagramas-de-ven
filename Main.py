import matplotlib.pyplot as plt
from matplotlib_venn import venn2
from matplotlib_venn import venn3



#Primero definimos el ingreso de datos, donde el usuario puede especificar
#cuántos conjuntos quiere ingresar

def ingresar_conjuntos():
    numero_conjuntos = int(input("¿Cuántos conjuntos desea ingresar?"))
    listaConjuntos = []
    for i in numero_conjuntos:
        numero_elementos = int(input("Cuántos elementos desea para el conjunto " + (i + 1)))
        listaConjuntos.append(crear_conjunto(numero_elementos))
    return listaConjuntos


#Esta función se llama para cada conjunto que se vaya a crear
def crear_conjunto(numero_elementos):
    conjunto = []
    for i in range(numero_elementos):
        elemento_conjunto = int(input("Ingrese el elemento " + str(i + 1) + " del conjunto: "))
        conjunto.append(elemento_conjunto)
    return conjunto


def obtener_conjunto_mas_largo(lista:[]):
    conjunto_mas_largo = lista[0]
    for conjunto in lista:
        if len(conjunto) > len(conjunto_mas_largo):
            conjunto_mas_largo = conjunto
    return conjunto_mas_largo


def unir_conjuntos(lista:[]):
    conjunto_union = []
    for conjunto in lista:
        for elemento_conjunto in conjunto:
            if elemento_conjunto not in conjunto_union:
                conjunto_union.append(elemento_conjunto)
    return conjunto_union

def intersectar_conjuntos(lista:[]):
    conjunto_interseccion = []
    conjunto_mas_largo = obtener_conjunto_mas_largo(lista)
    # Se recorre el conjunto más largo para poder verificar todos los elementos
    for elemento_conjunto in conjunto_mas_largo:
        # Declaro una bandera que me compruebe si el elemento está en todos
        # los conjuntos
        esta_en_todos = True

        # Recorro todos los conjuntos
        for conjunto in lista:
            if elemento_conjunto not in conjunto:
                esta_en_todos = False
                break  # En caso de que el elemento no esté en un conjunto

        if esta_en_todos:
            conjunto_interseccion.append(elemento_conjunto)
    return conjunto_interseccion


def hallar_diferencia(conjunto_minuendo, conjunto_sustraendo):
    conjunto_diferencia = conjunto_minuendo.copy()
    for elemento_conjunto in conjunto_sustraendo:
        if elemento_conjunto in conjunto_minuendo:
            conjunto_diferencia.remove(elemento_conjunto)
    return conjunto_diferencia


def hallar_difencia_simetrica(lista:[]):
    conjunto_union = unir_conjuntos(lista)
    conjunto_interseccion = intersectar_conjuntos(lista)
    return hallar_diferencia(conjunto_union, conjunto_interseccion)


def es_subconjunto(subconjunto, lista:[]):
    for conjunto in lista:
        if all(elemento in conjunto for elemento in subconjunto):
            print("El conjunto", subconjunto, "es subconjunto de", conjunto)
        else:
            print("El conjunto", subconjunto, "no es subconjunto de", conjunto)


def es_superconjunto(superconjunto, lista:[]):
    bandera = True
    for conjunto in lista:
        for elemento_conjunto in conjunto:
            if elemento_conjunto not in superconjunto:
                bandera = False
                break
        if bandera:
            print("El conjunto ", superconjunto, "es superconjunto de ", conjunto)
        else:
            print("El conjunto ", superconjunto, "no es superconjunto de ", conjunto)


#-----------Funciones para graficar los conjuntos-------------------------
def graficar_conjuntos(conjuntos:[]):
    if len(conjuntos) == 2:
        graficar_dos_conjuntos(set(conjuntos[0]), set(conjuntos[1]))
    elif len(conjuntos) == 3:
        graficar_tres_conjuntos(set(conjuntos[0]), set(conjuntos[1]), set(conjuntos[2]))
    else:
        print("son más de cuatro conjuntos")


def graficar_dos_conjuntos(conjunto1, conjunto2):
    # Crear el diagrama de Venn
    venn_diagram = venn2([conjunto1, conjunto2], set_labels=('Conjunto 1', 'Conjunto 2'))

    # Personalizar el diagrama (opcional)
    for label_id in ['10', '01', '11']:
        label = venn_diagram.get_label_by_id(label_id)
        if label is not None:
            if label_id == '10':
                label.set_text('\n'.join(map(str, conjunto1 - conjunto2)))
            elif label_id == '01':
                label.set_text('\n'.join(map(str, conjunto2 - conjunto1)))
            elif label_id == '11':
                label.set_text('\n'.join(map(str, conjunto1.intersection(conjunto2))))

    # Mostrar el diagrama
    plt.title("Diagrama de Venn de dos conjuntos")
    plt.show()


def graficar_tres_conjuntos(conjunto1, conjunto2, conjunto3):
    # Crear el diagrama de Venn
    venn_diagram = venn3([conjunto1, conjunto2, conjunto3], set_labels=('Conjunto 1', 'Conjunto 2', 'Conjunto 3'))

    # Personalizar el diagrama (opcional)
    for label_id in ['100', '010', '001', '110', '101', '011', '111']:
        label = venn_diagram.get_label_by_id(label_id)
        if label is not None:
            if label_id == '100':
                label.set_text('\n'.join(map(str, conjunto1 - conjunto2 - conjunto3)))
            elif label_id == '010':
                label.set_text('\n'.join(map(str, conjunto2 - conjunto1 - conjunto3)))
            elif label_id == '001':
                label.set_text('\n'.join(map(str, conjunto3 - conjunto1 - conjunto2)))
            elif label_id == '110':
                label.set_text('\n'.join(map(str, conjunto1.intersection(conjunto2) - conjunto3)))
            elif label_id == '101':
                label.set_text('\n'.join(map(str, conjunto1.intersection(conjunto3) - conjunto2)))
            elif label_id == '011':
                label.set_text('\n'.join(map(str, conjunto2.intersection(conjunto3) - conjunto1)))
            elif label_id == '111':
                label.set_text('\n'.join(map(str, conjunto1.intersection(conjunto2).intersection(conjunto3))))

    # Mostrar el diagrama
    plt.title("Diagrama de Venn de tres conjuntos")
    plt.show()

#----------------------------------Utils----------------------------------

def obtener_seleccion(lista, seleccion):
    indices = [int(i) for i in seleccion.split(",")]
    sublistas_seleccionadas = []
    for i in range(len(indices)):
        sublistas_seleccionadas.append(lista[indices[i]-1])
    return sublistas_seleccionadas

#------------------Menu---------------------------------------------------
def menu():
    cantidad_conjuntos: int = 0
    bandera: bool = True
    while bandera:
        cantidad_conjuntos = int(input("Bienvenid@, cuántos conjuntos desea ingresar? "))
        if 0 > cantidad_conjuntos > 4:
            print("Debe tener al menos 1 conjunto y debe ser menor a 4!")
        else:
            bandera = False

    conjuntos = []
    for i in range(cantidad_conjuntos):
        print(i)
        cantidad_elementos_conjunto: int = int(input("Ingrese la cantidad de conjuntos del cojunto "+str(i+1)+": "))
        conjunto = []
        for j in range(cantidad_elementos_conjunto):
            conjunto.append(input("Ingrese el elemento "+str(j+1)+" del conjunto "+str(i+1)+": "))
        conjuntos.append(conjunto)

    while True:
        opcion: int = int(input("Que desea realizar? \n 1. Unión de conjunto\n2. Intersección de conjuntos\n3. Diferencia de conjuntos\n4. Diferencia simétrica \n5.Subconjunto \n6.Superconjunto\n7.Graficar conjuntos: "))
        if opcion == 1:
            seleccion_conjuntos=input("Seleccione los coniuntos que se quieren unir seguido de una coma\nPor ejemplo: ' 1,2,3,4 ' ")
            lista_nueva = obtener_seleccion(conjuntos, seleccion_conjuntos)
            print("Union: ",unir_conjuntos(lista_nueva))
        if opcion == 2:
            seleccion_conjuntos = input("Seleccione los coniuntos que se quieren intersectar seguido de una coma\nPor ejemplo: ' 1,2,3,4 ' ")
            lista_nueva = obtener_seleccion(conjuntos, seleccion_conjuntos)
            print("Intersección: ",intersectar_conjuntos(lista_nueva))
        if opcion == 3:
            seleccion_conjuntos = input(
                "Seleccione los coniuntos que se quieren restar seguido de una coma, TENGA EN CUENTA EL ORDEN\nPor ejemplo: ' 1,2 = 1-2 ' ")
            lista_nueva = obtener_seleccion(conjuntos, seleccion_conjuntos)
            print("Diferencia: ",hallar_diferencia(lista_nueva[0],lista_nueva[1]))
        if opcion == 4:
            seleccion_conjuntos = input(
                "Seleccione los coniuntos que se quieren intersectar seguido de una coma\nPor ejemplo: ' 1,2,3,4 ' ")
            lista_nueva = obtener_seleccion(conjuntos, seleccion_conjuntos)
            print("Diferencia simetrica: ",hallar_difencia_simetrica(lista_nueva))
        if opcion == 5:
            seleccion_conjuntos = input(
                "Seleccione primero el subconjunto seguido de otro conjunto\nPor ejemplo: ' 1,2,3,4 ' ")
            lista_nueva = obtener_seleccion(conjuntos, seleccion_conjuntos)
            lista_sin_conjunto_0 = lista_nueva.copy()
            lista_sin_conjunto_0.pop(0)
            es_subconjunto(lista_nueva[0],lista_sin_conjunto_0)
        if opcion == 6:
            seleccion_conjuntos = input(
                "Seleccione primero el superconjunto seguido de otro conjunto\nPor ejemplo: ' 1,2,3,4 ' ")
            lista_nueva = obtener_seleccion(conjuntos, seleccion_conjuntos)
            lista_sin_conjunto_0 = lista_nueva.copy()
            lista_sin_conjunto_0.pop(0)
            es_superconjunto(lista_nueva[0], lista_sin_conjunto_0)
        if opcion == 7:
            if len(conjuntos) > 0 and len(conjuntos) < 4:
                graficar_conjuntos(conjuntos)
            else:
                print("No se puede graficar mas de 3 conjuntos por limitaciones de la libreria matplotlib_venn")


def prueba():
    conjunto_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    conjunto_b = [2, 4, 6, 8, 10]
    conjunto_c = [1, 2, 3, 20]

    print("Unión", unir_conjuntos([conjunto_a, conjunto_b]))
    print("Intersección", intersectar_conjuntos([conjunto_a, conjunto_b]))
    print("Diferencia", hallar_diferencia(conjunto_a, conjunto_b))
    print("Diferencia simétrica", hallar_difencia_simetrica([conjunto_a, conjunto_b]))
    es_subconjunto(conjunto_a, conjunto_b, conjunto_c)
    es_superconjunto(conjunto_a, conjunto_b, conjunto_c)

    graficar_conjuntos(conjunto_a, conjunto_b)
    graficar_conjuntos(conjunto_a, conjunto_b, conjunto_c)


if __name__ == "__main__":
    menu()
