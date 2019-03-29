# a = [1, 11, 21, 1211, 111221, 

def generateNext(elt):
	# init curr as first element
	curr = elt[0]
	curr_count = 1
	index = 1
	# store our answer as an array
	ans = []
	while index < len(elt):
		# if it's the same, increment current count
		if elt[index] == curr:
			curr_count += 1
		else:
			# update answer
			ans.append(curr_count)
			ans.append(curr)
			# update curr and count
			curr = elt[index]
			curr_count = 1
		index += 1
	# add the last one
	ans.append(curr_count)
	ans.append(curr)
	return ans

# first element of a is [1]
a_elt = [1]
# generate the next 30
for i in range(30):
	a_elt = generateNext(a_elt)

# should be our answer
print(len(a_elt))