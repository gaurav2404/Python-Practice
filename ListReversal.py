
list1 = [1,4,4,4,2,3,4,5,6,3,3,3]
c =[]
# with 1st method
for b in reversed(list1):
	c.append(b);
	# with second method
d = [v for v in reversed(list1)]
print(list1);
print(d);
