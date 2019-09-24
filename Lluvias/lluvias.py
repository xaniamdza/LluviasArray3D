import xlrd
from Array3D import Array3D

def main():

    lluvias = Array3D(35,32,12)
    
    for anio in range(1985,2020,1):
        archivo=xlrd.open_workbook(filename=str(anio)+'Precip.xls')
        hoja = archivo.sheet_by_index(0)
        for r in range(2,34):
            for c in range(1,13):
                valor = hoja.cell_value(r,c)
                lluvias.set_item(anio-1985,r-2,c-1,valor)

    year = int(input("Ingresa el año (1985-2019): "))
    year = year-1985

    estado = int(input("Ingresa el estado (1-32): "))
    estado = estado-1

    mes = int(input("Ingresa el mes (1-12): "))
    mes = mes-1

    x = lluvias.get_item(year,estado,mes)
    print(f"El promedio de centimetros cubicos de lluvias fue de: \"{x}\"")

main()    

