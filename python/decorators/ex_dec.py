#=====================================================================================================================
#					1. Implementing a generic Temperature Class By hand Coding the Descriptors
#=====================================================================================================================

class Celsius:
	"""The Celsius descriptor class	"""
	def __get__(self,instance,type= None)->object:
		if instance:
			return instance._val - 273.15
		else:
			raise Exception("Instance is None")
	def __set__(self,instance,val)-> None:
		if instance:
				instance._val = val + 273.15
		else:
			raise Exception("Instance is None")

class Farenheit:
	"""The Farenheit descriptor class	"""
	def __get__(self,instance,type=None) ->object:
		if instance:
			return  (instance._val-273.15)*9/5+32
		else:
			raise Exception("Instance is None")
	def __set__(self,instance,val)-> None:
		if instance:
			instance._val = (val - 32 )*5/9 + 273.15
		else:
			raise Exception("Instance is None")


class Kelvin:
	"""The Kelvin descriptor class	"""
	def __get__(self,instance,type=None) ->object:
		if instance:
				return instance._val
		else:
			raise Exception("Instance is None")
	def __set__(self,instance,val)-> None:
		if instance:
			instance._val = val
		else:
			raise Exception("Instance is None")

class Temperature:
	celsius = Celsius()
	kelvin = Kelvin()
	farenheit = Farenheit()
	def __init__(self,val):
		self._val = val

# Demo Code
print("="*30)
t1 = Temperature(273.15)
print(t1.celsius)
t1.celsius = 100
print(t1.farenheit)
print(t1.kelvin)

#=====================================================================================================================
#						2. Creating your own property descriptor Class 
#=====================================================================================================================


class mydec:
	"""This is my own (incomplete (does not have delete) and docs ) implementation of `@property` decorator"""
	def __init__(self,fgetter=None,fsetter=None):
		self.fgetter=fgetter
		self.fsetter=fsetter
	def getter(self,fgetter):
		"""returns a new mydec object with the new fgetter set """
		return type(self)(fgetter,self.fsetter)
	
	def setter(self,fsetter):
		return type(self)(self.fgetter,fsetter)

	#now to make is a Discriptor class

	def __get__(self,instance,type=None):
		"""calls the fgetter to get the value of the property"""
		return self.fgetter(instance)
	def __set__(self,instance,val):
		return self.fsetter(instance,val)
		

class test :
	"""This is a sample class to test my decorator"""
	def __init__(self):
		self._rdonly = 100
		self._hid = 210

	@mydec 
	def rdonly(self):
		return self._rdonly

	@mydec 
	def hid(self):
		return self._hid
		
	@hid.setter
	def hid(self,val):
		self._hid = val

print("="*30)
t1 = test()
print(t1.rdonly)
print(t1.hid)
t1.hid = 10
print(t1.hid)



#=====================================================================================================================
#				3. Implementing the Same Temperature class but using property decorators
#=====================================================================================================================

class Temp:
	"""Kinda making a generic Temperature Class using property decorators"""
	def __init__(self,kelvin):
		self._val = kelvin
	@property			# Same As Saying `celsius = property(celsius)`
	def celsius(self):
		return self._val -273.15
	@celsius.setter		# This calls the setter method of the the `celsius` object(which is an instance of property class ) and thus setting the fsetter

	def celsius(self,val):
		self._val = val+273.15
	@property
	def farenheit(self):
		return (self.celsius)*9/5 + 32
	@farenheit.setter
	def farenheit(self,val):
		self._val =  (self.farenheit-32)*5/9 + 273.15
	@property
	def kelvin(self):
		return self._val
	@kelvin.setter
	def kelvin(self,val):
		self._val = val


#Demo
print("="*30)
t2 = Temp(273.15)
print(t2.celsius)
t2.celsius = 100
print(t2.kelvin)
print(t2.farenheit)
print("="*30)

