import re
# Handy functions for Python
# flatten lists
import itertools
flattenlist = [[1, 2], [3, 4], [5, 6]]
flattenedlist = list(itertools.chain.from_iterable(flattenlist))
print(flattenedlist)
# Output:
# [1, 2, 3, 4, 5, 6]


# Reverse lists
reverselist = [10, 9, 8, 7]
print(reverselist[::-1])
# Output:
# [7, 8, 9, 10]

# Combine lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
for x, y in zip(list1, list2):
    print(x, y)
# Output:
# 1 4
# 2 5
# 3 6

# Negative indexing
negativeindex = [1, 2, 3, 4, 5]
print(negativeindex[-1])
# Output:
# 5

# Most frequent element in a list
frequentlist = [1, 2, 3, 4, 5, 1, 2, 3, 1, 2, 1]
print(max(set(frequentlist), key=frequentlist.count))
# Output:
# 1

# Reverse a string
string = "Hello World"
print(string[::-1])
# Output:
# dlroW olleH

# Split a string into a list
splitstring = "Hello World and Goodbye World"
print(splitstring.split())
# Output:
# ['Hello', 'World', 'and', 'Goodbye', 'World']

# Print multiple values of string
print("Hello"*3, "World"*3)
# Output:
# HelloHelloHello WorldWorldWorld

# Creating a single string from a list
liststring = ["Hello", "World"]
print(" ".join(liststring))
# Output:
# Hello World

# Transpose a matrix
transposematrix = [[1, 2, 3], [4, 5, 6]]
newtransposematrix = list(zip(*transposematrix))
for row in newtransposematrix:
    print(row)
# Output:
# (1, 4)
# (2, 5)
# (3, 6)

# Chaining comparison operators
chainingcomparison = 10
chainingcomparison2 = 20
chainingcomparison3 = 30
print(10 < chainingcomparison < 20)
print(21 < chainingcomparison2 < 30)
print(10 < chainingcomparison3 < 40)
# Output:
# False
# False
# True

# Invert a dictionary
invertdictionary = {"a": 1, "b": 2, "c": 3}
inverteddictionary = {value: key for key, value in invertdictionary.items()}
print(inverteddictionary)
# Output:
# {1: 'a', 2: 'b', 3: 'c'}

# Merge dictionaries
mergedictionary1 = {"a": 1, "b": 2}
mergedictionary2 = {"c": 3, "d": 4}
mergedictionary3 = {"e": 5, "f": 6}
mergedictionary = {**mergedictionary1, **mergedictionary2, **mergedictionary3}
print(mergedictionary)
# Output:
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

# Initialize list with same value
initializelist = [0] * 5
print(initializelist)
# Output:
# [0, 0, 0, 0, 0]

# Swap two variables
swap1 = 10
swap2 = 20
swap1, swap2 = swap2, swap1
print(swap1, swap2)
# Output:
# 20 10

# String concatenation
stringconcatenation = "Hello" "World"
print(stringconcatenation)
# Output:
# HelloWorld

# List intersection difference
listintersection1 = [1, 2, 3, 4, 5]
listintersection2 = [3, 4, 5, 6, 7]
print(set(listintersection1).intersection(listintersection2))
# Output:
# {3, 4, 5}

# Tuple unpacking
tupleunpacking = (1, 2, 3)
a, b, c = tupleunpacking
print(a, b, c)
# Output:
# 1 2 3

# List aliasing
listaliasing = [1, 2, 3, 4, 5]
listaliasing2 = listaliasing
listaliasing2.append(6)
print(listaliasing)
# Output:
# [1, 2, 3, 4, 5, 6]

# Not Or And
print(not True)
print(True or False)
print(True and False)
# Output:
# False
# True
# False

# For Else
for i in range(5):
    print(i)
else:
    print("Done")
# Output:
# 0
# 1
# 2
# 3
# 4
# Done

# F string
fstring = "World"
print(f"Hello {fstring}")
# Output:
# Hello World

# Print end
print("Hello", end=" ")
print("World")
# Output:
# Hello World

# Append to tuple
appendtuple = (1, 2, 3)
appendtuple += (4,)
print(appendtuple)
# Output:
# (1, 2, 3, 4)

# Append to list
appendlist = [1, 2, 3]
appendlist.append(4)
print(appendlist)
# Output:
# [1, 2, 3, 4]

# Ternary operator
ternaryoperator = 10
print("Hello" if ternaryoperator == 10 else "World")
# Output:
# Hello

# Remove duplicates from list
removeduplicates = [1, 2, 3, 1, 2, 3]
print(list(set(removeduplicates)))
# Output:
# [1, 2, 3]

# Underscore place holder
underscoreplaceholder = 10_000_000
print(underscoreplaceholder)
# Output:
# 10000000

# Underscore to ignore value
for _ in range(5):
    print("Hello World")
# Output:
# Hello World
# Hello World
# Hello World
# Hello World
# Hello World

# Set default value
defaultvalue = "Hello world and goodbye world"
defaultvaluecount = {}
for word in defaultvalue.split():
    defaultvaluecount.setdefault(word, 0)
    defaultvaluecount[word] += 1
print(defaultvaluecount)
# Output:
# {'Hello': 1, 'world': 2, 'and': 1, 'goodbye': 1}

# Regex

# re.findall
findall = "Hello 12345 World"
print(re.findall(r'\d+', findall))
# Output:
# ['12345']

# re.sub
sub = "Hello 12345 World"
print(re.sub(r'\d+', '', sub))
# Output:
# Hello  World

# re.search
search = "Hello 12345 World"
print(re.search(r'World', search))
# Output:
# <re.Match object; span=(12, 17), match='World'>

# re.match
match = "Hello 12345 World"
print(re.match(r'Hello', match))
# Output:
# <re.Match object; span=(0, 5), match='Hello'>

# re.fullmatch
fullmatch = "Hello 12345 World"
print(re.fullmatch(r'Hello 12345 World', fullmatch))
# Output:
# <re.Match object; span=(0, 17), match='Hello 12345 World'>

# re.split
split = "Hello 12345 World"
print(re.split(r'\d+', split))
# Output:
# ['Hello ', ' World']

# re.compile
compile_ = "Hello 12345 World"
pattern = re.compile(r'Hello')
print(pattern.match(compile_))
# Output:
# <re.Match object; span=(0, 5), match='Hello'>

# re pipe
heros = re.compile(r"Super(man|woman|human)")

h1 = heros.search("This will find Superman")
h2 = heros.search("This will find Superwoman")
h3 = heros.search("This will find Superhuman")
h4 = heros.search("This will not find Superboy")
print(h1.group())
print(h2.group())
print(h3.group())
print(h4)
# Output:
# Superman
# Superwoman
# Superhuman
# None

# lambda
lambdafunction = lambda x: x + 10
print(lambdafunction(5))
# Output:
# 15

# map
mapfunction = map(lambda x: x + 10, [1, 2, 3, 4, 5])
print(list(mapfunction))
# Output:
# [11, 12, 13, 14, 15]

