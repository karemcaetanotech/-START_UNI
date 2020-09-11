import abc
import math
from abc import ABCMeta

class AreaCalculavel(metaclass=ABCMeta):
	@abc.abstractmethod
	def area(self):
		pass

class Quadrado(AreaCalculavel):
	def __init__(self, lado):
		self.lado = lado
	def area(self):
		return self.lado * self.lado

class Retangulo(AreaCalculavel):
	def __init__(self, largura, altura):
		self.largura = largura
		self.altura = altura
	def area(self):
		return self.altura * self.largura

class Circulo(AreaCalculavel):
	def __init__(self, r):
		self.r = r
	def area(self):
		return self.r*self.r*math.pi


class Teste():
	def __init__(self, objetos):
		for id, o in enumerate(objetos):
			print(f"area do objeto {id} (tipo: {type(o)}): ", o.area())



Teste([Quadrado(2), Retangulo(3, 4), Circulo(5)])
