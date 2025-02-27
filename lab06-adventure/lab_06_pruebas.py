import random


class Habitacion:
    def __init__(self, descripcion="", norte=None, sur=None, este=None, oeste=None, objeto=None, enemigo=None):
        """
        Constructor para la clase Habitacion.
        :param descripcion: Descripción de la habitación (str).
        :param norte: Índice de la habitación al norte (int o None).
        :param sur: Índice de la habitación al sur (int o None).
        :param este: Índice de la habitación al este (int o None).
        :param oeste: Índice de la habitación al oeste (int o None).
        :param objeto: Objeto en la habitación (str o None).
        :param enemigo: Enemigo en la habitación (str o None).
        """
        self.descripcion = descripcion
        self.norte = norte
        self.sur = sur
        self.este = este
        self.oeste = oeste
        self.objeto = objeto
        self.enemigo = enemigo

    def __str__(self):
        """
        Representación amigable de la habitación.
        """
        return (f"Descripción: {self.descripcion}\n"
                f"Norte: {self.norte}, Sur: {self.sur}, Este: {self.este}, Oeste: {self.oeste}\n"
                f"Objeto: {self.objeto}, Enemigo: {self.enemigo}\n")


def combate(player, dragon):
    """
    Función para iniciar el combate contra el dragón.
    :param player: Diccionario con atributos del jugador.
    :param dragon: Diccionario con atributos del dragón.
    """
    print("\n¡Un dragón aparece! ¡Prepárate para luchar!")

    while dragon["vida"] > 0 and player["vida"] > 0:
        print(f"\nTu vida: {player['vida']}")
        print(f"Vida del dragón: {dragon['vida']}")
        accion = input("¿Qué deseas hacer? (atacar, defender, magia, huir): ").strip().lower()

        if accion == "atacar":
            if "espada" in player["inventario"]:
                dano = random.randint(5, 15)
                print(f"Atacas al dragón con la espada e infliges {dano} puntos de daño.")
                dragon["vida"] -= dano
            else:
                print("¡No tienes una espada para atacar!")

        elif accion == "defender":
            if "escudo" in player["inventario"]:
                print("Te defiendes con el escudo. El daño del dragón se reducirá.")
                dragon["ataque_reducido"] = True
            else:
                print("¡No tienes un escudo para defenderte!")

        elif accion == "magia":
            if "hechizo" in player["inventario"]:
                print("Lanzas un hechizo e infliges 8 puntos de daño al dragón.")
                dragon["vida"] -= 8
            else:
                print("¡No tienes un hechizo para lanzar magia!")

        elif accion == "huir":
            print("¡Huyes del combate! El dragón te observa mientras escapas.")
            break

        else:
            print("Acción no válida. Intenta de nuevo.")

        # Ataque del dragón si no está muerto
        if dragon["vida"] > 0 and accion != "huir":
            dano_dragon = random.randint(10, 20)
            if dragon.pop("ataque_reducido", False):
                dano_dragon //= 2
            print(f"El dragón te ataca e inflige {dano_dragon} puntos de daño.")
            player["vida"] -= dano_dragon

    if player["vida"] <= 0:
        print("\nEl dragón te ha derrotado. Game over.")
        exit()
    elif dragon["vida"] <= 0:
        print("\n¡Has derrotado al dragón! ¡Felicidades!")
        exit()


def main():
    """
    Función principal: crea las habitaciones, objetos e inicia la exploración del juego.
    """
    lista_habitaciones = []

    # Creación de habitaciones con objetos y enemigos
    lista_habitaciones.append(
        Habitacion("Estás en una habitación luminosa y soleada. Hay puertas al norte y al este.", norte=1, sur=None,
                   este=2, oeste=None))
    lista_habitaciones.append(
        Habitacion("Te encuentras en una biblioteca llena de libros antiguos. Puedes ir al norte o al oeste.", norte=4,
                   sur=0, este=None, oeste=3, objeto="hechizo"))
    lista_habitaciones.append(
        Habitacion("Esta es una torre fría y ventosa. Puedes ir al norte o regresar al oeste.", norte=5, sur=None,
                   este=None, oeste=0, objeto="espada"))
    lista_habitaciones.append(
        Habitacion("Es un calabozo oscuro y húmedo. Hacia el este hay una salida.", norte=None, sur=None, este=1,
                   oeste=6, enemigo="dragón"))
    lista_habitaciones.append(
        Habitacion("Te encuentras en un salón amplio con una chimenea encendida. Puedes ir al sur o al este.",
                   norte=None, sur=1, este=5, oeste=None, objeto="escudo"))
    lista_habitaciones.append(
        Habitacion("Este es un jardín con flores coloridas. Puedes ir al sur o al oeste.", norte=None, sur=2, este=7,
                   oeste=4))
    lista_habitaciones.append(
        Habitacion("Un comedor decorado con candelabros antiguos. Puedes ir al este.", norte=None, sur=None, este=3,
                   oeste=8))
    lista_habitaciones.append(
        Habitacion("Una habitación secreta con un cofre dorado. Regresa al oeste.", norte=None, sur=None, este=None,
                   oeste=5))
    lista_habitaciones.append(
        Habitacion("Un largo pasillo lleno de retratos. Al sur puedes salir al comedor.", norte=None, sur=6, este=None,
                   oeste=None))

    # Inicializar variables del jugador
    jugador = {
        "vida": 100,
        "inventario": []
    }

    # Inicializar variables del dragón
    dragon = {
        "vida": 100,
        "ataque_reducido": False
    }

    # Inicializar el juego
    current_room = 0
    done = False

    while not done:
        print("\n")
        print(lista_habitaciones[current_room].descripcion)

        # Revisar si hay un objeto en la sala
        if lista_habitaciones[current_room].objeto:
            objeto = lista_habitaciones[current_room].objeto
            print(f"¡Encuentras un {objeto}!")
            recoger = input(f"¿Quieres recoger el {objeto}? (si/no): ").strip().lower()
            if recoger == "si":
                jugador["inventario"].append(objeto)
                print(f"Has recogido el {objeto}.")
                lista_habitaciones[current_room].objeto = None

        # Revisar si hay un enemigo en la sala
        if lista_habitaciones[current_room].enemigo == "dragón":
            combate(jugador, dragon)

        # Preguntar qué hacer
        accion = input(
            "¿Qué deseas hacer? (n: Norte, s: Sur, e: Este, o: Oeste, salir: Terminar el juego): ").strip().lower()

        if accion in ["n", "north", "norte"]:
            next_room = lista_habitaciones[current_room].norte
        elif accion in ["s", "south", "sur"]:
            next_room = lista_habitaciones[current_room].sur
        elif accion in ["e", "east", "este"]:
            next_room = lista_habitaciones[current_room].este
        elif accion in ["o", "west", "oeste"]:
            next_room = lista_habitaciones[current_room].oeste
        elif accion == "salir":
            print("¡Gracias por jugar! Hasta pronto.")
            done = True
            continue
        else:
            print("Acción no válida. Intenta de nuevo.")
            continue

        # Validar si puede moverse a la siguiente sala
        if next_room is not None:
            current_room = next_room
        else:
            print("No puedes ir por ese camino.")


if __name__ == "__main__":
    main()

