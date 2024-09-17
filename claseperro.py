print("Clases version 2 el constructor")

class Perro:
    #funcion constructor
    def __init__(self,color,edad):
        self.color = color
        self.edad =  edad
    # funciones creadas por el usuario
    def muerde(self):
        print("Chale me mordio el perro")
    def chatperro(self,mensaje):
        print(f"Chat perro: {mensaje}")
    def Chatperra(self,mensajep):
        print(f"Chat perra: {mensajep}")
    def datos(self):
        print(f"color: {self.color}\nedad: {self.edad}")
# crear el objeto
chihuas=Perro("negro",2)
#llamadas a funciones
chihuas.datos()
chihuas.muerde()
chihuas.chatperro("Hola Canina")
chihuas.Chatperra("Hola boby")
chihuas.chatperro("Quieres ser gugguu?")
chihuas.Chatperra("grrrr.....")
