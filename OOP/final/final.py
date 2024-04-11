# %%Clases
import time
from datetime import datetime

date_string = datetime.now().strftime("%Y-%m-%d")

class Dorgueria:
    def __init__(self, medicamentos = [], clientes=[]) -> None:
        self.__medicamentos = self.set_medicamentos(medicamentos)
        self.__clientes = clientes

    def __str__(self):
        pass

    # Getters y setters
    def get_medicamentos(self):
        return self.__medicamentos

    def set_medicamentos(self, medicamentos):
        try:
            for medicamento in medicamentos:
                if isinstance(medicamento, Medicamento) or not medicamentos:
                    continue
                else:
                    raise ValueError(f"El elemento: '{medicamento}' no es un medicamento válido")
            return medicamentos
        except ValueError as e:
            print(e)

    def get_clientes(self):
        return self.__clientes
    
    # def set_clientes(self, paciente):
    #     self.__clientes.append(paciente)
    
    # Metodos del negocio
    def simulate_loading():
        loading_str = "Loading"
        dots = 0
        start_time = time.time()  # record the current time
        elapsed_time = 0
        while elapsed_time < 3:
            print(loading_str + "." * dots, end="\r")
            time.sleep(0.5)  # pause for half a second
            dots = (dots + 1) % 4  # cycle through 0, 1, 2, 3 dots
            elapsed_time = time.time() - start_time  # calculate the elapsed time

    def generar_factura(self):
        pass

    def realizar_venta(self):
        pass


class Medicamento:
    def __init__(self, sku, nombre_comercial, nombre_generico, precio, impuesto, gramos, unidades_disponibles) -> None:
        self.__sku = self.set_sku(sku)
        self.__nombre_comercial = self.set_nombre_comervial(nombre_comercial)
        self.__nombre_generico = self.set_nombre_generico(nombre_generico)
        self.__precio = self.set_precio(precio)
        self.__impuesto = self.set_impuesto(impuesto)
        self.__gramos = self.set_gramos(gramos)
        self.__unidades_disponibles = self.set_unidades_disponibles(unidades_disponibles)

    def __str__(self):
        return f""" 
                    Código: {self.__sku}                    
                    Nombre comercial: {self.__nombre_comercial}
                    Nombre genérico: {self.__nombre_generico}
                    Precio: {self.__precio}
                    Impuesto: {self.__impuesto}
                    Gramos: {self.__gramos}
                    Unidades disponibles: {self.__unidades_disponibles}
                """

    # Getters y setters
    def get_sku(self):
        return self.__sku
    
    def set_sku(self, sku):
        try:
            if sku.isalnum():
                return sku
            else:
                raise ValueError("Identificador incorrecto")
        except ValueError as e:
            print(e)

    def get_nombre_comercial(self):
        return self.__nombre_comercial
    
    def set_nombre_comercial(self, nombre_comercial):
        try:
            if nombre_comercial.isalpha():
                return nombre_comercial
            else:
                raise ValueError("Nombre comercial incorrecto")
        except ValueError as e:
            print(e)

    def get_nombre_generico(self):
        return self.__nombre_generico
    
    def set_nombre_generico(self, nombre_generico):
        try:
            if nombre_generico.isalpha():
                return nombre_generico
            else:
                raise ValueError("Nombre generico incorrecto")
        except ValueError as e:
            print(e)

    def get_precio(self):
        return self.__precio
    
    def set_precio(self, precio):
        try:
            return float(precio)
        except ValueError:
            print("Precio incorrecto")

    def get_impuesto(self):
        return self.__impuesto
    
    def set_impuesto(self, impuesto):
        try:
            # impuesto = impuesto.strip("%")
            return float(impuesto.strip("%")) / 100
        except ValueError:
            print("Valor del impuesto incorrecto")

    def get_gramos(self):
        return self.__gramos
    
    def set_gramos(self, gramos):
        try:
            return float(gramos)
        except ValueError:
            print("Cantidad de gramos incorrecta")

    def get_unidades_disponibles(self):
        return self.__unidades_disponibles
    
    def set_unidades_disponibles(self, unidades_disponibles):
        try:
            return int(unidades_disponibles)
        except ValueError:
            print("Numero de unidades disponibles incorrecto")

    def disminuir_disponibles(self):
        self.__unidades_disponibles -= 1


class Restringido(Medicamento):
    def __init__(self, sku, nombre_comercial, nombre_generico, precio, impuesto, gramos, unidades_disponibles, medico, dosis_maxima) -> None:
        super().__init__(sku, nombre_comercial, nombre_generico, precio, impuesto, gramos, unidades_disponibles)
        self.__medico = medico
        self.__dosis_maxima = self.set_dosis_maxima(dosis_maxima)

    def get_medico(self):
        return self.__medico
    
    def get_dosis_maxima(self):
        return self.__dosis_maxima
    
    def set_dosis_maxima(self, dosis_maxima):
        try:
            return float(dosis_maxima)
        except ValueError:
            print("Dosis máxima incorrecta")


class Libre(Medicamento):
    def __init__(self, sku, nombre_comercial, nombre_generico, precio, impuesto, gramos, unidades_disponibles, contraindicaciones) -> None:
        super().__init__(sku, nombre_comercial, nombre_generico, precio, impuesto, gramos, unidades_disponibles)
        self.__contraindicaciones = contraindicaciones

    def get_contraindicaciones(self):
        return self.__contraindicaciones
    

# %%Simulacro de venta
clientes = {
    "cliente1" : {"cedula" : 12345, "nombre": "Carlos Obando", "telefono": "3215476", "direccion": "Calle falsa con privet drive - 85"},
    "cliente2" : {"cedula" : 123456, "nombre": "Jessica Obando", "telefono": "3215476", "direccion": "Calle falsa con privet drive - 85"},
    "cliente3" : {"cedula" : 1234567, "nombre": "Ivan Obando", "telefono": "3215476", "direccion": "Calle falsa con privet drive - 85"}
}