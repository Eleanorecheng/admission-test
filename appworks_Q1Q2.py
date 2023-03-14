# Question 1

def find_max(numbers):
	if type(numbers) is list:
		maxNumber = numbers[0]
		for number in numbers:
			if number > maxNumber:
				maxNumber = number
		return maxNumber
	else:
		return -1

def find_position(numbers, target):
	for index in range(len(numbers)):
		value = numbers[index]
		if (target == value):
			return index
	return -1


print(find_max([1, 2, 4, 5])); # should print 5
print(find_max([5, 2, 7, 1, 6])); # should print 7

print(find_position([5, 2, 7, 1, 6], 5)) # should print 0
print(find_position([5, 2, 7, 1, 6], 7)) # should print 2
print(find_position([5, 2, 7, 7, 7, 1, 6], 7)) # should print 2 (the first one)
print(find_position([5, 2, 7, 1, 6], 8)) # should print -1


# Question 2
def count(input):
	test = {}
	for i in input:
		if i in test:
			test[i] += 1
		else:
			test[i] = 1
	return test

input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']
print(count(input1)) # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1}


def group_by_key(input):
	test = {}
	for item in input: 
		key = item['key']
		value = item['value']
		#print(key, value)
		if key in test:
			test[key] += value
		else:
			test[key] = value
	return test

input2 = [
{'key': 'a', 'value': 3},
{'key': 'b', 'value': 1},
{'key': 'c', 'value': 2},
{'key': 'a', 'value': 3},
{'key': 'c', 'value': 5}
]
print(group_by_key(input2)) # should print {‘a’: 6, ‘b’: 1, ‘c’: 7}