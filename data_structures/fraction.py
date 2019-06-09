class Fraction(object):

	def __init__(self, num, den):

		
		# assert type(num) and type(den) == int

		self.num = num
		self.den = den


	def __str__(self):
		return str(self.num) + '/' + str(self.den)

	def __add__(self, other):
		new_num = self.num*other.den + self.den*other.num
		new_den = self.den*other.den

		common_denom = self.gcd(new_num, new_den)

		return Fraction(new_num/common_denom, new_den/common_denom)

	def __sub__(self,other):

		new_num = self.num*other.den - self.den*other.num
		new_den = self.den*other.den

		common_denom = self.gcd(new_num, new_den)

		return Fraction(new_num/common_denom, new_den/common_denom)

	def __mul__(self,other):

		new_num = self.num*other.num
		new_den = self.den*other.den

		common_denom = self.gcd(new_num, new_den)

		return Fraction(new_num/common_denom, new_den/common_denom)

	def __truediv__(self, other):

		new_num = self.num * other.den
		new_den = self.den * other.num

		common_denom = self.gcd(new_num, new_den)

		return Fraction(new_num/common_denom, new_den/common_denom)

	def __eq__(self, other):

		firstnum = self.num * other.den
		secondnum = self.den * other.num

		return firstnum == secondnum

	def __lt__(self, other):

		new_num1 = self.num*other.den
		new_num2 = other.num*self.den

		return new_num1 < new_num2

	def __le__(self, other):

		new_num1 = self.num*other.den
		new_num2 = other.num*self.den

		return new_num1 <= new_num2

	def __gt__(self,other):

		new_num1 = self.num*other.den
		new_num2 = other.num*self.den

		return new_num1 > new_num2

	def __ge__(self,other):

		new_num1 = self.num*other.den
		new_num2 = other.num*self.den

		return new_num1 >= new_num2

	def __ne__(self, other):

		new_num1 = self.num*other.den
		new_num2 = other.num*self.den

		return new_num1 != new_num2

	def __radd__(self, other):
		if other == 0:
			return self

		else: 
			return self.__add__(other)

	def __rsub__(self, other):
		if other == 0:
			return self

		else: 
			return self.__sub__(other)

	def __rmul__(self, other):
		if other == 0:
			return self

		else: 
			return self.__mul__(other)

	# def __iadd__(self, other): 
	# 	self = self + other 
	# 	return self






	@staticmethod
	def gcd(m, n):
		while m% n != 0:
			oldm = m
			oldn = n 

			m = oldn
			n = oldm % oldn
			print('n: ', n)

		return n






if __name__ == '__main__':
	f1 = Fraction(3, 5)
	f2 = Fraction(3, 10)
	f3 = Fraction(2, 9)
	f4 = sum([f1, f2, f3]) 

	f1 += f3
	print(f1)
	# print(f1==f2)
	# print(f4)