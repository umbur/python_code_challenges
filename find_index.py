# Create a function that takes a list and a string as arguments and return the index of the string.
# Example:
# find_index(["hi", "edabit", "fgh", "abc"], "fgh") ➞ 2
# find_index(["Red", "blue", "Blue", "Green"], "blue") ➞ 1

def find_index(lst, txt):
	return lst.index(txt)
print(find_index(["hi", "edabit", "fgh", "abc"], "fgh"))
print(find_index(["Red", "blue", "Blue", "Green"], "blue"))
