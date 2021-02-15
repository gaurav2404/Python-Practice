def multyply(abc):
	result = 1;
	for v in abc:
		result *= v; 
	return result;

list1 = [1,5,6,3,3,3]
result = multyply(list1);
print(result);