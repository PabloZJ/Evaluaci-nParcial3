import os
os.system("cls")

titulo = f"""{" "*23}{"REGISTRO DE DATOS"}
{"-"*64}
{"|  MARCA":<10}{"|  AÑO":<8}{"| KILOMETRAJE ":<12}{"|  COSTO":<10}{"| IMPUESTO":<11}{"|  TOTAL  |":<10}
{"-"*64}
"""

menu = """
1. Registrar
2. Listar
3. Imprimir
4. Salir

Opción: """


matriz = []
Xmarcas = ["TOYOTA", "FORD", "CHEVROLET"]

def Registrar():
    while True:
        try:
            os.system("cls")
            marca = input("Marca: ").strip().upper()
            año = int(input("Año de fabricación: "))
            kilometraje = int(input("Kilometraje: "))
            costo = int(input("Costo de reparación: "))
            impuesto = round(costo * 0.08)
            total = round(costo+impuesto)
            if marca in Xmarcas and año>0 and kilometraje>0 and costo>0:
                matriz.append([marca,año,kilometraje,costo,impuesto,total])
                input("\nLos datos han sido añadidos con exito :)")
                break
            else:
                input("Error, ingrese de nuevo :(")
        except Exception as x:
            input(f"Excepción: {str(x)}")
#
def ListarTodos():
    salida = titulo
    for row in matriz:
        salida += f"|{row[0]:<9}"
        salida += f"|{row[1]:<7}"
        salida += f"|{row[2]:>13}"
        salida += f"|${row[3]:>8}"
        salida += f"|${row[4]:>9}"
        salida += f"|${row[5]:>8}|"
        salida += f"\n{"-"*64}\n"
    return salida
#
def ListarXmarca(imprimir):
    salida = titulo
    for row in matriz:
        if row[0] == imprimir:
            salida += f"|{row[0]:<9}"
            salida += f"|{row[1]:<7}"
            salida += f"|{row[2]:>13}"
            salida += f"|${row[3]:>8}"
            salida += f"|${row[4]:>9}"
            salida += f"|${row[5]:>8}|"
            salida += f"\n{"-"*64}\n"
    return salida
#
def Imprimir():
    while True:
        try:
            os.system("cls")
            imprimir = input(f"TODOS / {Xmarcas}\n¿Como va a imprimir?: ").upper()
            if imprimir in Xmarcas:
                with open(imprimir+".txt", "w", encoding="utf-8") as archivo:
                    archivo.write((ListarXmarca(imprimir)))
                    input("\nSe ha creado el archivo con exito :)")
                    break
            elif imprimir == "TODOS":
                with open(imprimir+".txt", "w", encoding="utf-8") as archivo:
                    archivo.write(ListarTodos())
                    input("\nSe ha creado el archivo con exito :)")
                    break
            else:
                input("Error al imprimir, vuelva a intentar")
        except Exception as x:
            input(f"Excepción: {str(x)}")
#
while True:
    try:
        os.system("cls")
        opc = int(input(menu))
        if opc == 4:
            break
        elif opc == 1:
            Registrar()
        elif opc == 2:
            print(ListarTodos())
            input()
        elif opc == 3:
            Imprimir()
        elif opc == 5:
            os.system("cls")
            input(titulo)
    except Exception as x:
        input(f"Excepcion: {str(x)}")