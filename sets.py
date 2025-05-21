#1.Write a Python program to create a set.
'''
s = {10,20,30}
print(s,type(s))
'''

#2.Write a Python program to iterate over sets.
'''
s = {10,"wel",20,30}
for i in s:
    print(i)
'''

#3.Write a Python program to add member(s) to a set.
'''
s = {10,"wel",20,30}
print(s)
s.add("hello")
print(s)
'''

#4.Write a Python program to remove item(s) from a given set.
'''
s = {10,"wel",20,30}
print(s)
s.remove("wel")
print(s)
'''

#5.Write a Python program to remove an item from a set if it is present in the set.
'''
s = {'hello', 'wel', 10, 20, 30}
print(s)
s.discard("wel")
print(s)
'''

#6.Write a Python program to create an intersection of sets.
'''
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1 & s2)
print(s1.intersection(s2))
'''

#7.Write a Python program to create a union of sets.
'''
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1 | s2)
print(s1.union(s2))
'''

#8.Write a Python program to create set difference.
'''
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1 - s2)
print(s2.difference(s1))
'''

#9.Write a Python program to create a symmetric difference.
'''
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1 ^ s2)
print(s2.symmetric_difference(s1))
'''

#10.Write a Python program to check if a set is a subset of another set.
'''
s1 = {10,20,30,40,50}
s2 = {40,50}
print(s2.issubset(s1))
'''

#11.Write a Python program to create a shallow copy of sets.
'''
s = {10, 20, 30}
new = s.copy()
print(new)
'''

#12.Write a Python program to remove all elements from a given set.
'''
s = {80, 20, 70, 10, 60, 30}
print(s)
s.clear()
print(s)
'''

#13.Write a Python program that uses frozensets.
'''
s1 = frozenset({80, 20, 70, 10, 60, 30})
print(s1)
'''

#14.Write a Python program to find the maximum and minimum values in a set.
'''
s = {80, 20, 70, 10, 60, 30}
print(min(s))
print(max(s))
'''

#15.Write a Python program to find the length of a set.
'''
s = {10,20,30,40,50}
print("Length :- ",len(s))
'''

#16.Write a Python program to check if a given value is present in a set or not.
'''
s = {10,20,30,40,50}
if 100 in s:
    print("Present")
else:
    print("Not present")
'''

#17.Write a Python program to check if two given sets have no elements in common.
'''
s1 = {10,20,30,40,50}
s2 = {60,70,80,90}
print(s1.isdisjoint(s2))
'''

#18.Write a Python program to check if a given set is a superset of itself and a superset of another given set.
'''
s1 = {10,20,30,40,50}
s2 = {40,50}
print(s1.issuperset(s2))
'''

#19.Write a Python program to find elements in a given set that are not in another set.
'''
s1 = {10,20,30,40,50}
s2 = {50,60,70,80,90}
print(s1.difference(s2))
print(s2 - s1)
'''

#20.Write a Python program to remove the intersection of a second set with a first set.
'''
s1 = {10,20,30,40,50}
s2 = {50,60,70,80,90}
print(s1.symmetric_difference(s2))
'''

#21.Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings.
#   Use Python set data type.
'''
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
unique = set(words)
print("Unique words:", unique)

freq = {word: words.count(word) for word in unique}
print("Frequency:", freq)
'''

#22.Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.
'''
li = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
target = 35
pairs = set()
for i in li:
    for j in li:
        if i + j == target and i <= j:
            pairs.add((i, j))
print(pairs)
'''

#23.Write a Python program to find the longest common prefix of all strings. Use the Python set.
'''
def logn_word(st):
    if not st:
        return ""
    prefix = st[0]
    for s in st[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""
    return prefix

words = ["flower", "flow", "flight"]
print(logn_word(words))
'''
 
#24.Write a Python program to find the two numbers whose product is maximum among all the pairs in a given list of numbers. Use the Python set.
'''
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]

max_product = None
pair = ()

for i in li:
    for j in li:
        if i != j:
            product = i * j
            if max_product is None or product > max_product:
                max_product = product
                pair = (i, j)

print("Max product pair:", pair, "with product", max_product)
'''

#25.Given two sets of numbers, write a Python program to find the missing numbers in the second set as compared to the first and vice versa. Use the Python set.
'''
s1 = {10,20,30,40,50}
s2 = {50,40,30,20}
for i in s1:
    if(i in s2):
        pass
    else:
        print(i)
'''

#26.Write a Python program to find all the anagrams and group them together from a given list of strings. Use the Python data type.
'''
from collections import defaultdict

li = ['eat', 'cba', 'tae', 'abc', 'xyz']
groups = defaultdict(list)
for word in li:
    key = ''.join(sorted(word))
    groups[key].append(word)

print(list(groups.values()))
'''

#27.Write a Python program to find all the unique combinations of 3 numbers from a given list of numbers, adding up to a target number.
'''
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 12
s = set()
for i in li:
    for j in li:
        new_li = []
        for k in li:
            if((i+j+k) == target):
                new_li.append(i)
                new_li.append(j)
                new_li.append(k)
        if(new_li):
            print(set(new_li),end = ' ')
'''         

#28.Write a Python program to find the third largest number from a given list of numbers.Use the Python set data type.
'''
li = [1, 2, 3, 4, 5, 5, 6, 7, 7, 8, 8, 9, 10]
s = set(li)
li = list(s)
print(li)
li.sort()
print("Third largest number in list are :- ",li[-3])
'''

#29.Write a Python program to remove all duplicates from a given list of strings and return a list of unique strings. Use the Python set data type.
'''
li = ['Python', 'Exercises', 'Practice', 'Solution', 'Exercises']
unique_li = list(dict.fromkeys(li))
print(unique_li)
'''

























            
    































































































