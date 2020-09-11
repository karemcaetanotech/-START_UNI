# O modulo datetime do python lida com datas
import datetime


data = input("entre com a data no formato dd/mm/aa: ")

dia, mes, ano =  data.split("/")

data_valida = True

# Uma exceção será disparada se a data tiver invalida, o python irá capturar e explicar o motivo
datetime.datetime(int(ano), int(mes), int(dia))

# Essa linha só será executada se a data tiver valida
if data_valida:
	print("Data válida")
