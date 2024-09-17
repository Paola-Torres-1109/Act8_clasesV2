class Informacion:

    def mi_lista(self):
        lista_Nomperros=["boby","Dollar","fany"]
        for x in lista_Nomperros:
            print(x)
    def mi_tupla(self):
        colores=("morado","azul","blanco")
        for y in colores:
            print(y)
    def mi_con(self):
        camaros={"SS","ZL1","LT"}
        for x in camaros:
            print(x)
    def mi_dicc(self):
        thisdict =	{
            "Marca": "Chevrolet",
            "Modelo": "Camaro",
            "Color":  "Plata"
}
        for x, y in thisdict.items():
            print(x, y)
#creando el objeto
datos=Informacion()
print("------Lista------\n**Listado de nombre de perros**")
datos.mi_lista()
print("")
print("------Tupla------\n**Los colores:**")
datos.mi_tupla()
print("")
print("------Conjunto------\n**Modelos de Camaros:**")
datos.mi_con()
print("")
print("------Diccionario------\n**Carrito:**")
datos.mi_dicc()
