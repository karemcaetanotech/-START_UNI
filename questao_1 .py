import abc
import math
from abc import ABCMeta

# O módulo abc contem o suporte a classe abstrata do python
# aqui é definido somente o metodo area
class AreaCalculavel(metaclass=ABCMeta):
	@abc.abstractmethod
	def area(self):
		pass

# A seguir, sao feitas as definições das classes filhas Quadrado, Retangulo e circulo
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
		    # a funcao type identifica o tipo do objeto, aqui o area implementado na classe filha é chamado
			print(f"area do objeto {id} (tipo: {type(o)}): ", o.area())


#Roda um teste com uma instancia de cada tipo classe filha
Teste([Quadrado(2), Retangulo(3, 4), Circulo(5)])
