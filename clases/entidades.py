from .lista_enlazada import LinkedList
import random

class Entidad:
    def __init__(self,
                 saludMax: int = 100,
                 salud: int = 100,
                 posicion: tuple[int, int] = (0, 0),
                 velocidad: int = 10):
        self.__saludMax = saludMax if saludMax > 0 else 100
        self.__salud = salud if saludMax >= salud >= 0 else self.__saludMax
        self.__estados = {
            "sangrado": 0,
            "frío": 0,
            "agotamiento": 0,
            "hambre": 0,
            "sed": 0,
        }
        self.__posicion = posicion
        self.__velocidad = velocidad if velocidad >= 0 else 1
    
    def get_saludMax(self):
        return self.__saludMax

    def get_salud(self):
        return self.__salud
    
    def get_estados(self):
        return self.__estados
    
    def get_posicion(self):
        return self.__posicion
    
    def get_estado(self, estado: str):
        return self.__estados.get(estado)
    
    def get_velocidad(self):
        return self.__velocidad
    
    def set_saludMax(self, nuevaMax: int):
        self.__saludMax = max(1, nuevaMax)
        if self.get_salud() > self.get_saludMax():
            self.__salud = self.__saludMax

    def set_salud(self, nuevaSalud: int):
        self.__salud = max(0, nuevaSalud)
        if self.get_salud() > self.get_saludMax():
            self.__salud = self.__saludMax
    
    def set_velocidad(self, nuevaVelocidad: int):
        self.__velocidad = max(0, nuevaVelocidad)

    def add_estado(self, estadoObjetivo: str, suma: int):
        if estadoObjetivo in self.get_estados():
            self.__estados[estadoObjetivo] = max(0, self.__estados[estadoObjetivo] + suma)
                
    def add_salud(self, suma: int):
        self.__salud = max(0, self.__salud + suma)

    def add_saludMax(self, suma: int):
        self.__saludMax = max(1, self.__saludMax + suma)
        if self.__salud > self.__saludMax: self.__salud = self.__saludMax

    def add_velocidad(self, suma: int):
        self.__velocidad = max(0, self.__velocidad + suma)
    
    def set_posicion(self, nuevaPosicion: tuple[int, int]):
        self.__posicion = nuevaPosicion
        
    def __str__(self):
        return f'''\
___________________________________________________________

Salud: {self.get_salud()} / {self.get_saludMax()}
Estados: {self.estados_lindo()}
Posición: {self.posicion_lindo()}
Velocidad: {self.get_velocidad()}
___________________________________________________________\
        '''

    def __repr__(self):
        return f'''Entidad(
        saludMax= {self.__saludMax},
        salud= {self.__salud},
        estados= {self.__estados},
        posicion= {self.__posicion},
        velocidad= {self.__velocidad}
        )
        '''
    
    def posicion_lindo(self):
        x = self.get_posicion()[0]
        y = self.get_posicion()[1]
        return f"{x} | {y}"
    
    def estados_lindo(self):
        elementos = []
        claves = self.get_estados().keys()
        for clave in claves:
            elementos.append(f"{clave}: {self.get_estados().get(clave)}")
        return " | ".join(elementos)
        
    def actualizar(self):
        sangrado = self.get_estado("sangrado")
        frio = self.get_estado("frío")
        agotamiento = self.get_estado("agotamiento")
        hambre = self.get_estado("hambre")
        sed = self.get_estado("sed")
        if sangrado >= 1:
            self.add_salud(-1)
            self.add_estado("sangrado", -1)
        if frio >= 10:
            self.add_velocidad(-1)
        if sed >= 10 or hambre >= 10:
            self.add_velocidad(-1)
            self.add_salud(-1)
            self.add_estado("agotamiento", 1)
        if agotamiento >= 10:
            self.add_velocidad(-agotamiento)
    
    def __eq__(self, otro: 'Entidad'):
        return self.__velocidad == otro.get_velocidad()
    
    def __lt__(self, otro: 'Entidad'):
        return self.__velocidad < otro.get_velocidad()
    
    def __gt__(self, otro: 'Entidad'):
        return self.__velocidad > otro.get_velocidad()
    
    def __ne__(self, otro: 'Entidad'):
        return self.__velocidad != otro.get_velocidad()
    
    def __le__(self, otro: 'Entidad'):
        return self.__velocidad <= otro.get_velocidad()
    
    def __ge__(self, otro: 'Entidad'):
        return self.__velocidad >= otro.get_velocidad()
    
    def get_icono(self):
        return "+"

class Objeto:
    def __init__(self, nombre: str = "objeto",
                 efectos: dict[str, int] | None = None,
                 peso: int = 1):
        self.__nombre = nombre
        self.__efectos = efectos if efectos else {}
        self.__peso = peso if peso >= 0 else 0

    def __str__(self):
        return f'''\
{self.__nombre} | {self.__peso} kg | {self.auxiliar_efectos()}\
'''
    def auxiliar_efectos(self):
        if not self.__efectos: return ""
        lista = []
        for clave, valor in self.__efectos.items():
            lista.append(f"{clave}: {valor}")
        return " & ".join(lista)
    
    def __repr__(self):
        return f"Objeto Objeto(nombre = {self.__nombre}, efectos = {self.__efectos}, peso = {self.__peso})"
    
    def get_nombre(self):
        return self.__nombre
    
    def get_efectos(self):
        return self.__efectos
    
    def get_peso(self):
        return self.__peso

    def set_nombre(self, nuevoNombre: str):
        self.__nombre = nuevoNombre

    def set_efectos(self, nuevosEfectos: dict[str, int]):
        self.__efectos = nuevosEfectos
    
    def set_peso(self, nuevoPeso: int):
        self.__peso = nuevoPeso if nuevoPeso >= 0 else 0

    def get_icono(self):
        return "+"
    
    def to_dict(self):
        return {
            "nombre": self.get_nombre(),
            "efectos": self.get_efectos(),
            "peso": self.get_peso()
        }

class Inventario(LinkedList):
    def __str__(self):
        if self.get_head() == None: return "Inventario Vacío"
        current = self.get_head()
        product = []
        contador = 1
        while current != None:
            next = current.get_next()
            product.append(f"{contador}- {current.get_data()}")
            contador += 1
            current = next
        bonito = "\n".join(product)
        return bonito + f"\n\nPeso total: {self.peso_total()}"

    def peso_total(self):
        return self.recursiva_de_apoyo(self.get_head())

    def recursiva_de_apoyo(self, actual):
        if actual == None:
            return 0
        else:
            siguiente = actual.get_next()
            objetoActual = actual.get_data()
            return objetoActual.get_peso() + self.recursiva_de_apoyo(siguiente)
        
    def search(self, nombre):
        if nombre is None: return None
        nombre = nombre.strip().lower()
        if self.get_head():
            current = self.get_head()
            while current.get_data().get_nombre().lower().strip() != nombre:
                next = current.get_next()
                if next != None:
                    current = next
                else: return None
            if current.get_data().get_nombre().lower().strip() == nombre:
                return current.get_data()
            
    def to_list(self):
        nodo_actual = self.get_head()
        lista = []
        while nodo_actual != None:
            objeto_actual = nodo_actual.get_data().to_dict()
            lista.append(objeto_actual)
            nodo_actual = nodo_actual.get_next()
        return lista
 
class Jugador(Entidad):
    def __init__(self, saludMax: int = 100,
                 salud: int = 100,
                 posicion: tuple[int, int] = (0,0),
                 velocidad: int = 10,
                 nombre: str = "jugador",
                 inventario: Inventario = None):
        super().__init__(saludMax, salud, posicion, velocidad)
        self.__nombre = nombre
        self.__inventario = inventario if inventario is not None else Inventario()
        self.__letras = {
            "a": 1, "b": 1, "c": 1, "d": 1, "e": 1, "f": 1, "g": 1,
            "h": 1, "i": 1, "j": 1, "k": 1, "l": 1, "m": 1, "n": 1,
            "ñ": 1, "o": 1, "p": 1, "q": 1, "r": 1, "s": 1, "t": 1,
            "u": 1, "v": 1, "w": 1, "x": 1, "y": 1, "z": 1}
        self.__mano = None

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre:str):
        self.__nombre = nombre
    
    def get_inventario(self):
        return self.__inventario
    
    def get_letras(self):
        return self.__letras
    
    def get_mano(self):
        if self.__mano == None: return None
        return self.__mano
    
    def set_mano(self, nombre: str):
        self.__mano = self.__inventario.search(nombre)

    def add_letra(self, letraObjetivo: str, suma: int):
        if letraObjetivo in self.__letras:
            self.__letras[letraObjetivo] += suma
            if self.__letras[letraObjetivo] < 0:
                self.__letras[letraObjetivo] = 0
                
    def __str__(self):
        return f'''\
___________________________________________________________
{self.get_nombre()}

Salud: {self.get_salud()} / {self.get_saludMax()}
Estados: {self.estados_lindo()}
Posición: {self.posicion_lindo()}
Velocidad: {self.get_velocidad()}
Equipado: {self.get_mano()}
___________________________________________________________\
        '''
    
    def __repr__(self):
        return f'''\
        Jugador(nombre = {self.get_nombre()},
        saludMax = {self.get_saludMax()},
        salud = {self.get_salud()},
        estados = {self.get_estados()},
        posicion = {self.get_posicion()},
        velocidad = {self.get_velocidad()},
        inventario = {self.get_inventario()},
        letras = {self.get_letras()},
        mano = {self.get_mano()},
        )\
        '''
    
    def desarmar_diccionarios(self):
        lista = []
        for clave, valor in self.get_estados().items():
            lista.append(f"{clave}: {valor}")
        return " | ".join(lista)
    
    def desarmar_posicion(self):
        x = self.get_posicion()[0]
        y = self.get_posicion()[1]
        return f"{x} | {y}"
    
    def desarmar_inventario(self):
        return self.get_inventario().__str__()

    def atacar(self, inputs: str, puntosEnemigos: str = ""):
        fuerzaDelAtaque = 0
        usadas = []
        for letra in inputs:
            if letra.lower() in self.get_letras().keys() and not letra in puntosEnemigos and not letra in usadas:
                fuerzaDeLetra = self.get_letras()[letra]
                fuerzaDelAtaque += fuerzaDeLetra
                usadas.append(letra)
        return max(0, fuerzaDelAtaque - self.get_estado("agotamiento"))
    
    def recibir_danio(self, cantidad: int, efectos: dict[str, int]):
        self.add_salud(-cantidad)
        for efecto, valor in efectos.items():
            self.add_estado(efecto, valor)

    def dar(self, objeto: Objeto):
        self.__inventario.add(objeto)

    def quitar(self, objeto: str):
        self.__inventario.remove(self.__inventario.search(objeto))

    def usar_objeto(self, objeto: Objeto):
        efectos = objeto.get_efectos()
        estados = self.get_estados()
        for efecto, valor in efectos.items():
            if efecto == "saludMax":
                self.add_saludMax(valor)
            elif efecto == "salud":
                self.add_salud(valor)
            elif efecto == "posicion":
                self.set_posicion(valor)
            elif efecto == "velocidad":
                self.add_velocidad(valor)
            elif efecto == "nombre":
                self.set_nombre(valor)
            elif efecto in estados.keys():
                self.add_estado(efecto, valor)
    
    def letras_bonito(self):
        nuevo_dict = {}
        lista = []
        for letra, valor in self.__letras.items():
            if valor in nuevo_dict.keys():
                nuevo_dict[valor] += letra.upper()
            else: nuevo_dict[valor] = letra.upper()
        for valor, letras in nuevo_dict.items():
            lista.append(f"({" ".join(letras)}): {valor}")
        return " | ".join(lista)

    def get_icono(self):
        return "@"
    
    def to_dict(self):
        return {
            "nombre": self.get_nombre(),
            "saludMax": self.get_saludMax(),
            "salud": self.get_salud(),
            "estados": self.get_estados(),
            "posicion": self.get_posicion(),
            "velocidad": self.get_velocidad(),
            "inventario": self.get_inventario().to_list(),
            "letras": self.get_letras(),
            "mano": self.get_mano().get_nombre() if self.get_mano() != None else None
        }
    
class Enemigo(Entidad):
    def __init__(self, saludMax: int = 100,
                 salud: int = 100,
                 posicion: tuple[int, int] = (0,0),
                 velocidad: int = 10,
                 nombre: str = "enemigo",
                 blindaje: str = "",
                 fuerza: int = 1,
                 efectos: dict[str, int] = {},
                 inmunidades: tuple[str] = (),
                 botin: dict[Objeto, int] | None = None):
        super().__init__(saludMax, salud, posicion, velocidad)
        self.__nombre = nombre
        self.__botin = self.generar_drops(botin)
        self.__blindaje = blindaje
        self.__inmunidades = inmunidades
        self.__fuerza = fuerza
        self.__efectos = efectos

    def get_nombre(self):
        return self.__nombre
    
    def get_blindaje(self):
        return self.__blindaje
    
    def get_botin(self):
        return self.__botin
    
    def get_inmunidades(self):
        return self.__inmunidades
    
    def get_fuerza(self):
        return self.__fuerza
    
    def get_efectos(self):
        return self.__efectos
    
    def set_efectos(self, nuevosEfectos: dict[str, int]):
        self.__efectos = nuevosEfectos
    
    def set_nombre(self, nuevoNombre: str):
        self.__nombre = nuevoNombre
    
    def set_blindaje(self, nuevoBlindaje: str):
        self.__blindaje = nuevoBlindaje
    
    def set_botin(self, nuevoBotin: dict[Objeto, int]):
        self.__botin = self.generar_drops(nuevoBotin)

    def set_inmunidades(self, inmunidades: list[str]):
        self.__inmunidades = inmunidades

    def set_fuerza(self, nuevaFuerza: int):
        self.__fuerza = nuevaFuerza
    
    def add_blindaje(self, letras: str):
        self.__blindaje += letras

    def add_inmunidad(self, inmunidad: str):
        nuevas = list(self.__inmunidades)
        if not inmunidad in self.__inmunidades:
            nuevas.append(inmunidad)
            self.__inmunidades = nuevas

    def add_efecto(self, efectoObjetivo: str, suma: int):
        if efectoObjetivo in self.get_efectos():
            self.__efectos[efectoObjetivo] = max(0, self.__efectos[efectoObjetivo] + suma)

    def add_fuerza(self, suma: int):
        self.__fuerza += suma

    def __str__(self):
        return f'''\
___________________________________________________________
{self.get_nombre()}
    
Salud: {self.get_salud()} / {self.get_saludMax()}
Fuerza: {self.get_fuerza()}
Estados: {self.estados_lindo()}
Posición: {self.posicion_lindo()}
Velocidad: {self.get_velocidad()}
Blindaje: {self.get_blindaje()}
Efectos: {self.auxiliar_efectos()}
Inmunidades: {self.inmunidades_lindo()}
___________________________________________________________\
        '''
    
    def auxiliar_efectos(self):
        if not self.__efectos: return ""
        lista = []
        for clave, valor in self.__efectos.items():
            lista.append(f"{clave}: {valor}")
        return " & ".join(lista)

    def __repr__(self):
        return f'''
        Objeto Enemigo(
        nombre = {self.get_nombre()}
        saludMax = {self.get_saludMax()}
        salud = {self.get_salud()}
        estados = {self.get_estados()}
        posicion = {self.get_posicion()}
        velocidad = {self.get_velocidad()}
        fuerza = {self.get_fuerza()}
        botin = {self.get_botin()}
        efectos = {self.get_efectos()}
        )
        '''
    
    def generar_drops(self, botin):
        if not botin: return {}
        botin_listo = []
        for objeto, probabilidad in botin.items():
            generacion = random.uniform(0, 100) <= probabilidad
            if generacion is True:
                botin_listo.append(objeto)
        return botin_listo

    def inmunidades_lindo(self):
        return " | ".join(self.__inmunidades)

    def recibir_danio(self, cantidad: int, efectos: dict[str, int] = None):
        self.add_salud(-cantidad)
        if efectos is None: return
        for efecto, valor in efectos.items():
            if not efecto in self.__inmunidades:
                self.add_estado(efecto, valor)

    def atacar(self, inputs: str = "abcdefghijklmnñopqrstuvwxyz"):
        fuerzaDelAtaque = 0
        usadas = []
        letras = "abcdefghijklmnñopqrstuvwxyz"
        for letra in inputs:
            if letra in letras and not letra in usadas:
                fuerzaDeLetra = self.get_fuerza()
                fuerzaDelAtaque += fuerzaDeLetra
                usadas.append(letra)
        return max(0, fuerzaDelAtaque - self.get_estado("agotamiento"))

    def get_icono(self):
        return "!"

class Mapa:
    def __init__(self, longitud: int = 1000, latitud: int = 1000):
        self.__centrox = longitud // 2
        self.__centroy = latitud // 2
        self.__longitud = longitud
        self.__latitud = latitud
        self.__dominio = self.generar_porcion()
        self.__entidades = []
    
    def generar_porcion(self):
        porcion = []
        for fila in range(self.__latitud):
            actual = []
            for elemento in range(self.__longitud):
                actual.append("·")
            porcion.append(actual)
        return porcion
    
    def get_coordenada(self, x: int, y: int):
        indice_x = x + self.__centrox
        indice_y = y + self.__centroy
        if 0 <= indice_x < self.__longitud and 0 <= indice_y < self.__latitud:
            return self.__dominio[indice_y][indice_x]
        return None
    
    def set_coordenada(self, x: int, y: int, entidad):
        indice_x = x + self.__centrox
        indice_y = y + self.__centroy
        if hasattr(entidad, "get_icono"):
            if not entidad in self.__entidades: self.__entidades.append(entidad)
        if 0 <= indice_x < self.__longitud and 0 <= indice_y < self.__latitud:
            self.__dominio[indice_y][indice_x] = entidad

    def __str__(self):
        total = []
        for fila in self.__dominio:
            for elemento in fila:
                if hasattr(elemento, "get_icono"):
                    total.append(elemento.get_icono())
                    continue
                total.append(elemento)
        return " ".join(total)
    
    def mover_entidad(self, entidad, inputs):
        for letra in inputs:
            letra = letra.lower()
            x, y = entidad.get_posicion()
            direccion_x, direccion_y = 0, 0
            if letra == "d":
                direccion_x += 1
            elif letra == "w":
                direccion_y += 1
            elif letra == "a":
                direccion_x -= 1
            elif letra == "s":
                direccion_y -= 1
            
            proxima_x = x + direccion_x
            proxima_y = y + direccion_y

            objetivo = self.get_coordenada(proxima_x, proxima_y)
            if hasattr(objetivo, "get_icono") and objetivo.get_icono() == "!":
                return objetivo
            
            self.set_coordenada(x, y, "·")

            entidad.set_posicion((proxima_x, proxima_y))
            entidad.add_estado("agotamiento", 1)
            
            self.set_coordenada(proxima_x, proxima_y, entidad)

    def get_longitud(self):
        return self.__longitud
    
    def get_latitud(self):
        return self.__latitud

class Ventana:
    def __init__(self, mapa: Mapa = Mapa(), alto: int = 13, ancho: int = 71):
        """
        Se recomienda usar numeros impares
        """
        self.__mapa = mapa
        self.__alto = alto
        self.__ancho = ancho
        self.__centrox = ancho // 2
        self.__centroy = alto // 2
    
    def generar_vista(self, x, y):
        total = []
        x_inicio = x - self.__centrox
        for i in range(self.__alto):
            fila_actual = []
            for n in range(self.__ancho):
                elemento_actual = self.__mapa.get_coordenada(x_inicio + n, (y + self.__centroy) - i)
                if not elemento_actual:
                    fila_actual.append(" ")
                elif hasattr(elemento_actual, "get_icono"):
                    fila_actual.append(elemento_actual.get_icono())
                elif isinstance(elemento_actual, str):
                    fila_actual.append(elemento_actual)
            total.append(" ".join(fila_actual))
        return "\n".join(total)