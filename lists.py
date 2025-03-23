list1 = ["Jaya", 2,34.7,55,"Kumbhkar"]
print(list1)

# length of list using len() function 
length = len(list1)
print("Length : ", length )

# type()
print("Type : ",type(list1))

# list() constructor
newList = list(("apple","banana","cherry"))
print("Created new list : ",newList)

# Access List Items

# using positive indexing 
lst  = [1,2,3,4,5]
print("Access elements :",lst[3])

# using negative indexing
print(lst[-4])
print(lst[-2])

# using range of indexes / slicing

thislist = [11,12,13,14,15,16,17,18,19,20]
print("slicing without step size :",thislist[3:7])

thislist = [11,12,13,14,15,16,17,18,19,20]
print("slicing with step size :",thislist[3:7:2])

print(thislist[2:])
print(thislist[:8])
print(thislist[:6:2])
print(thislist[1::3]) 
print(thislist[::])
print(thislist[1::])

# using negative range / slicing

print(thislist[-4:-2])           # doubt
print(thislist[-1:])
print(thislist[:-5])            
print(thislist[1:-3])
print(thislist[-3:2:-1])
print(thislist[-3:2])             # it will return an empty list 

print(thislist[-2:-7:-2])        # doubt
print(thislist[::-1])
print(thislist[:-3:-1])

# check if item exist

thislist1 = ["apple", "banana", "cherry"]
if "banana" in thislist1:
    print("Yes banana is present in list ")


# Change list items
thislist2 = ["apple", "banana", "cherry"]
thislist2[2] = "Coderwin"
print("Changed Value:",thislist2)

#Change a Range of Item Values

thislist2 = ["apple", "banana", "cherry"]
thislist2[1:3] =["watermelon", "mango"]
print(thislist2)

thislist2 = ["apple", "banana", "cherry"]
thislist2[1:3] =["watermelon","mango","grapes","coderwin"]              # doubt
print(thislist2)

thislist2 = ["apple", "banana", "cherry"]
thislist2[1] =["watermelon","mango","grapes"]
print(thislist2)


# Add List Items

# append()
lst1 = ["apple", "banana", "cherry"]
lst1.append("New appended Item")
print(lst1)

# insert()
lst2 = ["apple", "banana", "cherry"]
lst2.insert(1,"New inserted Item")
print(lst2)

#extend()
lst3 = ["apple", "banana", "cherry"]
lst4 = [1,2,3,4,5]
lst3.extend(lst4)
print(lst3)


# Remove list items

# remove()
l1 = ["A","B","C","D","E"]
l1.remove("C")
print(l1)

# pop()
l2 = ["A","B","C","D","E"]
l2.pop()
print(l2)

l2.pop(1)
print(l2)

# del()
l3= ["A","B","C","D","E"]
del l3
# print(l3)

l4= ["A","B","C","D","E"]
del l4[3]
print(l4)

# clear()
l5 = ["A","B","C","D","E"]
l5.clear()
print(l5)

# Loop lists 

# using for loop
thislist3 = ["A","B","C","D","E"]
for i in thislist3:
    print(i)


# using through the index numbers
thislist4 = ["A","B","C","D","E"]
for i in range(len(thislist4)):
    print(i,":",thislist4[i])

# Using while loop
i = 0
while(i<len(thislist4)):
    print(thislist4[i])
    i+=1

# List Comprehension
listVal = ["banana","mango","grapes","cherry","apple"]
newlist1 = [x for x in listVal]
print(newlist1)

newlist2 =[x for x in listVal if x!="apple"]
print(newlist2)

newlist3 =[x if x!="apple" else "Orange" for x in listVal]
print(newlist3)


# copy()
mylist = [1,2,3,4,5]
copiedlist1 = mylist.copy()
print("Copied List 1 :",copiedlist1)

#
copiedlist2 = list(mylist)
print("Copied List 2 :",copiedlist2)

#
copiedlist3 = mylist[:]
print("Copied List 3 :",copiedlist3)

# join 
l1 = [1,2,3]
l2 = ["a","b","c"]

# using "+"
newlst1 = l1 + l2
print(newlst1)

#using append()
l1.append(l2)
print(l1)

# using for loop 

l6 = [11,12,13,14,15]
l7 = ["a1","b1","c1"]
    
for i in l7:
    l6.append(i)

print(l6)

# using extend()
l6.extend(l7)
print(l6)



