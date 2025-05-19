def leerarchivo (nombre):
    with open (nombre,"r") as file:
        lineas = [linea.strip() for linea in file.readlines()]
    return lineas

def hallar (grupo, x):
    if grupo[x] != x:
        grupo [x] = hallar(grupo,grupo[x])
    return grupo [x]

def union(grupo,tamaño, x, y):
    conjuntoX = hallar (grupo, x)
    conjuntoY = hallar (grupo, y)

    if conjuntoX != conjuntoY:
        if tamaño[conjuntoX] < tamaño[conjuntoY]:
            grupo [conjuntoX] = conjuntoY
            tamaño[conjuntoY] += tamaño[conjuntoX]
        else:
            grupo [conjuntoY] = conjuntoX
            tamaño [conjuntoX] += tamaño[conjuntoY]

def particion (z):
    conjuntoZ = {}

    def resolver (restante, maximo):
        j = (restante, maximo)
        if j in conjuntoZ:
            resultado = conjuntoZ [j]
        elif restante == 0:
            resultado = 1
        elif restante < 0 or maximo == 0:
            resultado = 0
        else:
            forma1 = resolver (restante - maximo, maximo)   
            forma2 = resolver (restante, maximo -1) 
            resultado = (forma1 + forma2) % 1000000007

        conjuntoZ [j]= resultado
        return resultado
    return resolver (z, z)

def ejecutar (nombreAch):
    lineas = leerarchivo(nombreAch)
    indice = 0
    Ncasos = int(lineas[indice])
    indice += 1

    if not (1<=Ncasos<=10):
        print ("el limite debe ser entre 1 y 10")
        return

    resultados = []

    for i in range(Ncasos):
        partes = lineas[indice].split ()
        n = int(partes[0])
        m = int(partes[1])
        indice += 1

        if not (1<= n <=50) or not (1<= m <=100):
            print ("el limite de n debe ser entre 1 y 50 y el de m debe ser entre 1 y 100")
            return

        grupo = [j for j in range(n + 1)]
        tamaño = [1] * (n + 1)

        for i in range (m):
            operaciones = lineas[indice].split ()
            indice += 1

            if operaciones[0] == "union":
                x = int(operaciones[1])
                y = int(operaciones[2])
                union (grupo, tamaño, x, y)
            elif operaciones[0] == "partitions":
                x = int(operaciones[1])
                resultado = particion (tamaño[hallar(grupo, x)])
                resultados.append(resultado)

    for l in resultados:
        print (l)

ejecutar("a.txt")


