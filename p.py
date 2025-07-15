productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
                      '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
                      'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
                     'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
                     'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
                     '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
                     '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
                     'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
                           }

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
              'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
              'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
                 }

#funcion
marca = ['HP','Acer','Asus','Dell']
def stock(marca):
    marca = input("Ingrese marca a consultar: ").strip().capitalize()
    for marca in productos:
        if marca == marca:   
            print(f"El stock es de: {stock}")
            break
        elif marca != marca:
            print("producto no encontrado")
            break

ram_min = []
ram_max = []
def busqueda_ram_precio(ram_min, ram_max):
    try: 
        ram_min = int(input("Ingrese la RAM minima: "))
        ram_max = int(input("Ingrese la RAM maxima: "))
        precio = int(input("Ingrse precio: "))
        if ram_min in productos:
            if ram_max in productos:
                if precio in stock: 
                    for ram_min, ram_max in productos:
                        print({productos})
                elif precio not in stock:
                         print("No hay notebooks que mostrar")
            elif ram_max not in productos:
                     print("No hay notebooks que mostrar")
        elif ram_min not in productos:
                print("No hay notebooks que mostrar")
    except ValueError:
        print("Debe ingresar valores enteros!!")
        return   

modelo = []
def eliminar_producto(modelo):
    while True:    
        modelo = input("Ingrese el modelo a eliminar: ")
        if modelo in productos:
            for modelo in productos:
                productos.pop(modelo)
                print("Producto eliminado!!")
                otro = input("¿Desea eliminar otro producto? ").strip().capitalize()
                if otro == "si":
                    eliminar_producto(modelo)
                elif otro == "no":
                    return (modelo)
        elif modelo not in productos:
            print("Modelo no existente")

#menu 
while True:
    print("***MENU PRINCIPAL***")
    print("1. Stock marca.")
    print("2. Búsqueda por RAM y precio.")
    print("3. Eliminar producto.")
    print("4. Salir.")
    print("holiii")
    opcion = input("Ingrese opcion: ")

    if opcion == "1":
        stock(marca)
    elif opcion == "2":
        busqueda_ram_precio(ram_min, ram_max)
    elif opcion == "3":
        eliminar_producto(modelo)
    elif opcion == "4":
        print("Programa Finalizado")
        break
    



