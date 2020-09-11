import abc
import math
from abc import ABCMeta

class Pessoa(metaclass=ABCMeta):
	def nome(self):
		return self.__nome__
	def rg(self):
		return self.__rg__

class Funcionario(Pessoa):
	def __init__(self, nome, rg, salario_inicial, percentual):
		self.__nome__ = nome
		self.__rg__ = rg
		self.__salario_inicial__ = salario_inicial
		self.__percentual__ = percentual
		self.__salario_total__ = salario_inicial
	def salario_inicial(self):
		return self.__salario_inicial__
	def percentual(self):
		return self.__percentual__
	def salario_total(self):
		return self.__salario_total__

	def set_salario_inicial(self, salario_inicial):
		self.__salario_inicial__ = salario_inicial
	def set_percentual(self, percentual):
		self.__percentual__ = percentual
	def set_salario_total(self, salario_total):
		self.__salario_total__ = salario_total


class Teste:
	def aumenta_salario(funcionario):
		funcionario.set_salario_total(funcionario.salario_total() * (1 + funcionario.percentual()))
		funcionario.set_percentual(2 * funcionario.percentual())
	def __init__(self):
		# cria funcionario em 2016
		self.funcionario = Funcionario(nome="funcionario", rg="678128", salario_inicial=1000.00, percentual=1.5/100.)
		# realiza aumentos para 2017, 2018, 2019
		for i in range(0, 4):
			Teste.aumenta_salario(self.funcionario)
			#print(f"salario {2016 + i + 1}:", self.funcionario.salario_total())

		print(f"nome: {self.funcionario.nome()} rg: {self.funcionario.rg()} salario 2020: {self.funcionario.salario_total()}")


Teste()
