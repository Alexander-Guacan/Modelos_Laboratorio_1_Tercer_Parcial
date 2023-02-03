from Input import Input

class SATV:
    """
    Sistema Automatizado de Trafico Vehicular.
    Controla el flujo de trafico entre carreteras que van de una ciudad a otra.

    Attributes:
        carreteras
        indice_carreteras
        costo

    Methods:
        private:
            __calcular_estado_objetivo
            __imprimir_listado_carreteras
            __habilitar_carretera
            
        public:
            calcular_costo_viaje
    """

    def __init__(self) -> None:
        """Constructor por defecto
        """

        # Estado inicial de las carreteras (I: indeterminado, H: habilitada, D: deshabilitada)
        self.__carreteras = {
            "Esmeraldas" : "I",
            "Ibarra" : "I",
            "Quito" : "I",
            "Latacunga" : "I"
        }
        # Listado de las carreteras disponibles
        self.__indice_carreteras = list(self.__carreteras.keys())
        # Costo computacional que incrementa a medida que el sistema debe habilitar una carretera
        self.__costo = 0

    def __calcular_estado_objetivo(self, recorridos: int) -> dict[str, str]:
        """
        Retorna el estado en que se deberan encontrar las carreteras al final del recorrido del vehiculo, segun la carretera
        final a la que desea llegar

        Args:
            recorridos (int): _description_ Numero de carreteras a recorrer

        Returns:
            dict[str, str]: _description_ Estado final esperado de las carretera al finalizar el recorrido
        """

        # Copia del estado inicial de las carreteras
        estado_objetivo = self.__carreteras.copy()

        # Creamos el supuesto de habilitar las carreteras a recorrer
        for i in range(recorridos):
            # Cambiamos el estado de indefinido (I) a habilitado (H)
            estado_objetivo[self.__indice_carreteras[i]] = 'H'

        return estado_objetivo
    
    def __imprimir_listado_carreteras(self) -> None:
        """
        Imprime en pantalla las carreteras disponibles por recorrer
        """
        # Indice de cada carretera
        i = 1
        for carretera in self.__indice_carreteras:
            # Imprime el indice y nombre de cada carretera
            print(f"{i}.- {carretera}")
            # Incrementamos el indice
            i += 1

    def __habilitar_carretera(self, indice: int) -> None:
        """
        Cambia el estado de las carreteras a un estado habilitado (H). Incrementado el costo computacional del sistema

        Args:
            indice (int): _description_ Carretera a habilitar
        """
        print(f"Carretera {self.__indice_carreteras[indice]} habilitada")
        # Cambia el estado de la carretera a habilitado
        self.__carreteras[self.__indice_carreteras[indice]] = 'H'
        # Incrementando el costo computacional
        self.__costo += 1
        print(f"Costo actual: {self.__costo}")
    
    def calcular_costo_viaje(self) -> None:
        """
        Inicia las operaciones del agente inteligente. Habilitando las carreteras que lo requieran y mostrando los resultados de dichos cambios asi como del costo computacional
        """
        # Impresion de carreteras disponibles en el sistema
        self.__imprimir_listado_carreteras()
        # Ingreso por teclado del numero de carreteras a recorrer por el vehiculo
        recorridos = int(Input.string("Numero de carretera destino: ", 1, lambda char: char >= '1' and char <= str(len(self.__indice_carreteras))))
        print(f"Estado objetivo: {self.__calcular_estado_objetivo(recorridos)}")

        # Consulta del estado de cada carretera
        for i in range(recorridos):
            # Consulta si la carretera se encuentra o no habilitada
            esta_habilitada = Input.string(f"Carretera {self.__indice_carreteras[i]} habilitada? (s/n): ", 1, lambda char: char == 's' or char == 'n') == 's'
            
            # Carretera no habilitada
            if not esta_habilitada:
                # Habilitamos la carretera requerida
                self.__habilitar_carretera(i)

        # Impresion por consola del costo computacional y el estado final de las carreteras
        print("\n[RESULTADOS]")
        print(f"\tCosto total: {self.__costo}")
        print(f"\tEstado final: {self.__carreteras}")