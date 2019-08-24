numbers = [9,20,3,44,75,13,675,12,34]
friends =["Pete","Megan","Matt","John","Tim","Chris"]
friends.append("Bob") #append, insert(pos,"name"), and extend commands
friends.insert(0,"Kelly")
friends.remove("Tim")
print(friends)
friends.pop()
print(friends)
print(numbers)
numbers.reverse()
print(numbers)

numbers.pop()
print(numbers)
newNum = numbers.index(75)
#remember "using number in the sentence need to include str(string)"
print("75 is in position " + str(newNum)) 
numbers.sort()
print("After sorted numbers: " + str(numbers))
numbers1 = (sorted(numbers))
print(numbers1)
numbers1.reverse()
print(numbers1)

# reverseNum = numbers.sort()
# reverseNum.reverse()
# print("reverse the sorted numbers :" + str(reverseNum))

