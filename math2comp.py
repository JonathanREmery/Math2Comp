def isNumber(c):
	if c == "0" or c == "1" or c == "2" or c == "3" or c == "4" or c == "5" or c == "6" or c == "7" or c == "8" or c == "9":
		return True
	else:
		return False

def isVariable(c):
	alphabet = []
	i = 97
	while i < 123:
		alphabet.append(chr(i))
		i += 1
	if c in alphabet:
		return True
	else:
		return False

def isOpenParentheses(c):
	if c == "(":
		return True
	else:
		return False

def replaceCoeffecient(function):
	i = 0
	while i < len(function)-1:
		if isNumber(function[i]) and (isVariable(function[i+1]) or isOpenParentheses(function[i+1])):
			function = function[:i+1] + "*" + function[i+1:]
		i += 1
	return function

def replaceAbsolute(function):
	while "|" in function:
		a = 0
		while a < len(function):
			if function[a] == "|":
				break
			a += 1
		b = len(function)-1
		while b >= 0:
			if function[b] == "|":
				b += 1
				break
			b -= 1
		function = function[:a] + "abs(" + function[a+1:]
		b += 4
		function = function[:b] + ")" + function[b:]
		function = function[:b-2] + function[b-1:]
	return function

def replaceExponents(function):
	while "^" in function:
		i = 0
		while i < len(function)-1:
			if function[i] == "^":
				break
			i += 1
		function = function[:i-1] + "pow(" + function[i-1:]
		i += 4
		function = function[:i] + ", " + function[i+1:]
		i += 2
		function = function[:i+1] + ")" + function[i+1:]
	return function


def convertToFunction(func):
	func = replaceCoeffecient(func)
	func = replaceAbsolute(func)
	func = replaceExponents(func)
	return "def " + func.split(" = ")[0] + ": return " + func.split(" = ")[1]