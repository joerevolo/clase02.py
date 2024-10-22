#Lista de dispositivos de computo
#La lista es mutable porque su contenido se puede cambiar

dispositivos = ['impresoras', 'escaner', 'camara web','luces']
venta =['2021','2022','2023','2024']
factura = [1200,5000, 6000, 4500]
#tupla
#La tupla es inmutable porque su contenido no se puede cambiar 
servidor = ('SUNAT', '198.23.0.10','Lima', 'admin')
#reemplzar impresoras por ventilador en la lista
dispositivos[0] ='ventilador'

print(dispositivos)
#reemplazar SUNAT por INDECOPI
servidor[0]='INDECOPI'
print(servidor)