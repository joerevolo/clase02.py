'''
Ingrese nombre del empleado, hroas y minutos trabajados y el costo por 
hroa para hallar el importe a pagar.
'''
#ing (integer) entero
#float (flotante) decimal
print('------------------------------------')
print('CALCULO DE HORAS TRABAJADAS')
print('------------------------------------')
xnom=input('ingrese nombre: ')
xhoras = int(input('ingrese horas trabajadas: ')) 
xmin = int(input('ingrese minutos trabajados: ')) 
xcosto = float( input('ingrese el costo por hora: '))
#calcular
total = xcosto * xhoras + (xcosto/60) * xmin
print('R E S U L T A D O S')
print('trabajador: ', xnom)
print('horas trabajadas: ', xhoras)
print('minutos trabajados: ',xmin)
print('el total a pagar es: ', (int(total*100))/100)