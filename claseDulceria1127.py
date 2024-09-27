class proveedor1127:

    def Diccionario_Sucursales1127(self):
        print("Tabla de sucursales: \n")
        Contenido1 =	{
    "Id-Sucursal -> ": 32456,
    "Nombre -> ": "CandyLand",
    "Direccion -> ": "Calle Roma #4567",
    "Num. telefono -> ": 6564871285,
    "Correo -> ": "Gab@gmail.com",
    "Codigo -> ": 3467,
    "Horario -> ": "10:30 am / 6:00 pm",
}
        print(Contenido1)
        for A,B in Contenido1.items():
            print(A,B)

    def Diccionario_Clientes1127(self):
        print("Tabla de clientes: \n")
        Contenido2 =	{
    "Id-Clientes: -> ": 46789,
    "Nombre completo -> ": "Maria de la Rosa",
    "Edad -> ": 45,
    "Num. telefono -> ": 67689602,
    "Correo -> ": "Mari43@gmail.com",
    "Domicilio -> ": "Calle mora #7862",
    "Forma de pago -> ": "Tarjeta",
}
        print(Contenido2)
        for C,D in Contenido2.items():
            print(C,D)

    def Diccionario_Empleados1127(self):
        print("Tabla de empleados: \n")
        Contenido3 =	{
    "Id-Empleado -> ": 527890,
    "Nombre completo -> ": "Marco el pro",
    "Num. telefono -> ": 6571268066,
    "Curp -> ": "MCRO465PR4532",
    "RFC -> ": "HJ4563HTDV36",
    "Edad -> ": 32,
    "Sexo -> ": "Masculino",
}
        print(Contenido3)
        for E,F in Contenido3.items():
            print(E,F)

    def Diccionario_Producto1127(self):
        print("Tabla de producto: \n")
        Contenido4 =	{
    "Id-Producto -> ": 925412,
    "Tipos-producto -> ": "Paletas",
    "Nombre -> ": "De la rosa",
    "Cantidad -> ": 1562,
    "Sucursal -> ": "CandyLand",
    "Correo -> ": "ProveedorPaletas@gmail.com",
    "Num. telefono -> ": 65734123,
}
        print(Contenido4)
        for G,H in Contenido4.items():
            print(G,H)

objeto = proveedor1127()
print("")
objeto.Diccionario_Sucursales1127()
print("")
objeto.Diccionario_Empleados1127()
print("")
objeto.Diccionario_Clientes1127()
print("")
objeto.Diccionario_Producto1127()
print("")
