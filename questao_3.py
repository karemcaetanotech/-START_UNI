import datetime


data = input("entre com a data no formato dd/mm/aa: ")

dia, mes, ano =  data.split("/")

data_valida = True


datetime.datetime(int(ano), int(mes), int(dia))
if data_valida:
	print("Data válida")
