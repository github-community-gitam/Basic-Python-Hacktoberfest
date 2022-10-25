def add(datatype, *args):
	if datatype =='int':
		answer = 0
	if datatype =='str':
		answer =''
	for x in args:
		answer = answer + x

	print(answer)
add('int', 5, 6)
add('str', 'Hi ', 'Geeks')
