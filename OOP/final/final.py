# %%Clases
import time
from datetime import datetime

date_string = datetime.now().strftime("%Y-%m-%d")

class Dorgueria:
    def __init__(self, clientes=[]) -> None:
        self.__clientes = clientes

    def __str__(self):
        pass

    @property
    def clientes(self):
        return self.__clientes

    @clientes.setter
    def clientes(self, clientes):
        try: 
            if isinstance(clientes, list):
                for cliente in clientes:
                    if isinstance(cliente, Cliente):
                        self.__clientes.append(cliente)
                    else:
                        raise ValueError("Cliente inválido")
            else:
                if isinstance(clientes, Cliente):
                    self.__clientes.append(clientes)
                else:
                    raise ValueError("Cliente inválido")
        except ValueError as e:
            print(e)

    # Metodos del negocio
    def simulate_loading():
        loading_str = "Validando venta"
        dots = 0
        start_time = time.time() 
        elapsed_time = 0
        while elapsed_time < 4:
            print(loading_str + "." * dots, end="\r")
            time.sleep(0.5)  
            dots = (dots + 1) % 4  
            elapsed_time = time.time() - start_time 

    def generar_factura(self, cliente):
        return f"""
                    Fecha: {date_string}\n
                    Nombre del cliente: {cliente.nombre}\n
                    Número de cédula: {cliente.cedula}\n
                    Telefono: {cliente.telefono}\n
                    Dirección: {cliente.direccion}\n\n
                    Su compra: {cliente.conteo()}\n

                """

    def realizar_venta(self):
        for cliente in self.__clientes:
            factura = self.generar_factura(cliente)
            print("Medicamentos antes de la venta")
            map(print, cliente.medicamentos)
            for medicamento in cliente.medicamentos:
                medicamento.disminuir_disponibles()
            with open("ventas.txt", "a") as file:
                file.write(factura)
            print(factura)
            self.simulate_loading()
            print("Medicamentos después de la venta")
            map(print, cliente.medicamentos)


class Cliente:
    def __init__(self, cedula, nombre, telefono, direccion, medicamentos = []) -> None:
        self.__cedula = cedula
        self.__nombre = nombre
        self.__telefono = telefono
        self.__direccion = direccion
        self.__medicamentos = medicamentos
        pass
    
    @property
    def cedula(self):
        return self.__cedula

    @cedula.setter
    def cedula(self, cedula):
        try:
            if cedula.isnumeric():
                self.__cedula = cedula
            else:
                raise ValueError("Número de cédula incorrecto")
        except ValueError as e:
            print(e)
    
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        try:
            if nombre.isalpha():
                self.__nombre = nombre
            else:
                raise ValueError("Nombre incorrecto")
        except ValueError as e:
            print(e)
    
    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, telefono):
        try:
            if telefono.isnumeric():
                self.__telefono = telefono
            else:
                raise ValueError("Número de telefono incorrecto")
        except ValueError as e:
            print(e)
    
    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self, direccion):
        try:
            if direccion.isalnum():
                self.__direccion = direccion
            else:
                raise ValueError("Dirección incorrecto")
        except ValueError as e:
            print(e)
    
    @property
    def medicamentos(self):
        return self.__medicamentos

    @medicamentos.setter
    def medicamentos(self, medicamentos):
        try:
            if isinstance(medicamentos, list):
                for medicamento in medicamentos:
                    if isinstance(medicamento, Medicamento):
                        self.__medicamentos.append(medicamento)
                    else:
                        raise ValueError(f"El elemento no es un medicamento válido")
            else:
                if isinstance(medicamentos, Medicamento):
                    self.__medicamentos.append(medicamento)
                else:
                    raise ValueError(f"El elemento no es un medicamento válido")
        except ValueError as e:
            print(e)

    # Método de clase
    def conteo(self):
        conteo = 0
        final = ""
        total_pago = 0
        for medicamento in self.__medicamentos:
            conteo = self.__medicamentos.count(medicamento)
            precio_final = medicamento.get_precio + medicamento.get_impuesto
            final += f"""
                        Medicamento: {medicamento.get_nombre_comercial} ({medicamento.get_nombre_generico}) x{conteo}\n
                        {f'Medicamento de venta restringida, médico quien ordena: {medicamento.info_medico()}. Dosis máxima {medicamento.get_dosis_maxima}\n' if isinstance(medicamento, Restringido) else f'Contraindicaciones: {medicamento.get_contraindicaciones}\n'}
                        Miligramos por dosis: {medicamento.get_gramos}\n
                        Precio: {precio_final}\n\n
                    """
            conteo = 0
            total_pago += (precio_final)
        final += f"\nTotal a pagar: {total_pago}"
        return final
        


class Medicamento:
    def __init__(self, sku, nombre_comercial, nombre_generico, precio, impuesto, gramos, unidades_disponibles) -> None:
        self.__sku = self.set_sku(sku)
        self.__nombre_comercial = self.set_nombre_comercial(nombre_comercial)
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

    # Método de clase
    def disminuir_disponibles(self):
        self.__unidades_disponibles -= 1


class Restringido(Medicamento):
    def __init__(self, sku, nombre_comercial, nombre_generico, precio, impuesto, gramos, unidades_disponibles, medico, dosis_maxima) -> None:
        super().__init__(sku, nombre_comercial, nombre_generico, precio, impuesto, gramos, unidades_disponibles)
        self.__medico = medico
        self.__dosis_maxima = dosis_maxima

    def get_medico(self):
        return self.__medico
    
    def get_dosis_maxima(self):
        return self.__dosis_maxima

    def info_medico(self):
        return f"{self.__medico["nombre"]}, Telefono: {self.__medico["telefono"]}, Especialidad: {self.__medico["especialidad"]}"


class Libre(Medicamento):
    def __init__(self, sku, nombre_comercial, nombre_generico, precio, impuesto, gramos, unidades_disponibles, contraindicaciones) -> None:
        super().__init__(sku, nombre_comercial, nombre_generico, precio, impuesto, gramos, unidades_disponibles)
        self.__contraindicaciones = contraindicaciones

    def get_contraindicaciones(self):
        return self.__contraindicaciones
    

# %%Simulacro de venta
medico1 = {"nombre": "Daniel Londoño", "telefono": "3335578", "especialidad": "Medicina general"}
medico2 = {"nombre": "Ivan Bustillo", "telefono": "3335578", "especialidad": "Oncologia"}
medico3 = {"nombre": "Andredi Pumarejo", "telefono": "3335578", "especialidad": "Medicina interna"}


alprazolam = Restringido(1004729, "Neupax", "Alprazolam", 14000, "16%", 0.25, 7, medico1, "Máximo 10 mg diarios")
ketamina = Restringido(87659, "Ketolar", "Ketamina", 20000, "20%", 50, 20, medico2, "Máximo 50mg/mL")
