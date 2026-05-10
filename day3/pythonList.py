thisList = ["Apple", "Banana", "Cherry", "Katal","Orange","Mango"]
# List Allows multiple Data types while sets and tuple don't
print(len(thisList))

print(thisList[0])
print(thisList[-1])
print(thisList[2:5])
#return all the item except certain index, here cherry is excluded
print(thisList[:2])

if "Apple" in thisList:
    print("apple is here!")
else:
    print("What the fuck is an apple")
