###################################
# REMUS Vector Math module v1.0.0 #
###################################

########### Error codes and notes #############
# -Error 0x000001: Dot Product function cannot process passed arguments. There must only be two arguments, a list and/or a KMVector object.
# -Error 0x000002: Cannot divide integer by Vector object. Try dividing Vector object by integer instead.
# -Error 0x000003: Get angle function cannot process passed arguments. There must only be two arguments, a list and/or a KMVector object.
# -Performing a standard math operator on more than two KMVector objects will work, but can only give you upto two parent vectors if returned by __str__
# -All methods involving angles will retun degrees by default, as opposed to radians.
# - Deprecation Warning, in the future, creating a KMVector object may require you to pass in a list instead of an undifined series of numbers,
#   for example:
#   myVec = KMVector([5, 7, 8]) instead of myVec = KMVector(5, 7, 8). This change will depend on public requests
#### Warning, Documentation does not yet exist for this module ####

## Lisencing Notice ##
# Officially licensed to https://remusmtf.com/ of REMUS by Kudzayi Mberi
# You may use this product for comercial or non-comercial purposes.
# If use is for comecrical purposes. You should include the version number.
# If it is for non-comercial use, you must include this entire header.
# Copyright © 2018 by https://remusmtf.com/

#### Comming to v2.0.0 ####
# =Get magnatuide of vectors
# -Cross/Scalar Product
# -Check if two vectors are perpendicular, parallel or non-parallel/converging

# angle between vec A and B
# a dot b = |a| * |b| * cos(0)
# 1. a dot b
# 2. |a| = sqrt( (n1)^2 + (n2)^2 + (n3)^2 ) = sqrt( u )
# 3. |a| = sqrt( (n1)^2 + (n2)^2 + (n3)^2 ) = sqrt( v )
# example: -66 = sqrt(94) * sqrt(89) * cos(0)

#Personal todo list
# -Try to keep imported module count down to 0
# - Allow input format of (4, 2) as well as "4i + 2j"

import math

class KMVector:

	def __init__(self, *args, isResultantVec = False, resultantParentVectors = False):
		self.Vec = list(args)
		self.isResultantVec = isResultantVec
		self.resultantParentVectors = resultantParentVectors

	def __add__(self, other):
		self.temp = [None] * len(other.Vec)
		for d in range(0, len(other.Vec)):
			self.temp[d] = self.Vec[d] + other.Vec[d]
		return KMVector(*self.temp, isResultantVec = True, resultantParentVectors = "<{}> + <{}>".format(str(self.Vec)[1:-1], str(other.Vec)[1:-1]))

	def __sub__(self, other):
		self.temp = [None] * len(other.Vec)
		for d in range(0, len(other.Vec)):
			self.temp[d] = self.Vec[d] - other.Vec[d]
		return KMVector(*self.temp, isResultantVec = True, resultantParentVectors = "<{}> - <{}>".format(str(self.Vec)[1:-1], str(other.Vec)[1:-1]))

	def __mul__(self, other):
		if type(other) == type(99):
			self.temp = [None] * len(self.Vec)
			for d in range(0, len(self.Vec)):
				self.temp[d] = self.Vec[d] * other
			return KMVector(*self.temp, isResultantVec = True, resultantParentVectors = "<{}> * {}".format(str(self.Vec)[1:-1], other))
		elif type(other) == type(KMVector()):
			self.temp = [None] * len(self.Vec)
			for d in range(0, len(self.Vec)):
				self.temp[d] = self.Vec[d] * other.Vec[d]
			return KMVector(*self.temp, isResultantVec = True, resultantParentVectors = "<{}> * <{}>".format(str(self.Vec)[1:-1], str(other.Vec)[1:-1]))

	def __rmul__(self, other):
		if type(other) == type(99):
			self.temp = [None] * len(self.Vec)
			for d in range(0, len(self.Vec)):
				self.temp[d] = self.Vec[d] * other
			return KMVector(*self.temp, isResultantVec = True, resultantParentVectors = "{} * <{}>".format(other, str(self.Vec)[1:-1]))

	def __truediv__(self, other):
		if type(other) == type(99):
			self.temp = [None] * len(self.Vec)
			for d in range(0, len(self.Vec)):
				self.temp[d] = self.Vec[d] / other
			return KMVector(*self.temp, isResultantVec = True, resultantParentVectors = "<{}> / {}".format(str(self.Vec)[1:-1], other))
		elif type(other) == type(KMVector()):
			self.temp = [None] * len(self.Vec)
			for d in range(0, len(self.Vec)):
				self.temp[d] = self.Vec[d] / other.Vec[d]
			return KMVector(*self.temp, isResultantVec = True, resultantParentVectors = "<{}> / <{}>".format(str(self.Vec)[1:-1], str(other.Vec)[1:-1]))
	
	def __rtruediv__(self, other):
		if type(other) == type(99):
			return "Error code: 0x000002"

	@classmethod
	def dotVec(self, firstList, secondList):
		if type(firstList) == type([99]) and type(secondList) == type([99]):
			self.finTemp = lambda firstList, secondList: sum(map(lambda x, y: x * y, firstList, secondList))
			return self.finTemp(firstList, secondList)
		elif type(firstList) == type([99]) and type(secondList) == type(KMVector()):
			self.finTemp = lambda firstList, secondList: sum(map(lambda x, y: x * y, firstList, secondList))
			return self.finTemp(firstList, secondList.Vec)
		elif type(firstList) == type(KMVector()) and type(secondList) == type([99]):
			self.finTemp = lambda firstList, secondList: sum(map(lambda x, y: x * y, firstList, secondList))
			return self.finTemp(firstList.Vec, secondList)
		elif type(firstList) == type(KMVector()) and type(secondList) == type(KMVector()):
			self.finTemp = lambda firstList, secondList: sum(map(lambda x, y: x * y, firstList, secondList))
			return self.finTemp(firstList.Vec, secondList.Vec)
		else:
			return "Error code: 0x000001"

	@classmethod
	def getAngle(self, firstList, secondList):
		if type(firstList) == type([99]) and type(secondList) == type([99]):
			return (math.degrees(math.acos( (KMVector.dotVec(firstList, secondList))/ (math.sqrt(sum([i ** 2 for i in firstList])) * math.sqrt(sum([i ** 2 for i in secondList]))) )))
		elif type(firstList) == type([99]) and type(secondList) == type(KMVector()):
			return (math.degrees(math.acos( (KMVector.dotVec(firstList, secondList.Vec))/ (math.sqrt(sum([i ** 2 for i in firstList])) * math.sqrt(sum([i ** 2 for i in secondList.Vec]))) )))
		elif type(firstList) == type(KMVector()) and type(secondList) == type([99]):
			return (math.degrees(math.acos( (KMVector.dotVec(firstList.Vec, secondList))/ (math.sqrt(sum([i ** 2 for i in firstList.Vec])) * math.sqrt(sum([i ** 2 for i in secondList]))) )))
		elif type(firstList) == type(KMVector()) and type(secondList) == type(KMVector()):
			return (math.degrees(math.acos( (KMVector.dotVec(firstList.Vec, secondList.Vec))/ (math.sqrt(sum([i ** 2 for i in firstList.Vec])) * math.sqrt(sum([i ** 2 for i in secondList.Vec]))) )))
		else:
			return "Error code: 0x000003"

	def __str__(self):
		return "Vector: <{}>\n Dimensions: {}\n Magnitude: {}\n Is resultant: {}\n Has Parents: {}\n".format((str(self.Vec)[1:-1]),len(self.Vec),"Unknown",self.isResultantVec,self.resultantParentVectors)
