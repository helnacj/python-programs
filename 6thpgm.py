numbers = list(map(int, input("enter the values of the list:").split()))
print("original list:",numbers)
search = int(input("enter the elements to be searched:"))
if search in numbers:
    print("element is found")
else:
    print("element is not found")
old = int(input("enter the elements to be change:"))
new= int(input("enter the new element:"))
if old in numbers:
    index=numbers.index(old)
    numbers[index]=new
    print("updated list:", numbers)
else:
    print("old is not found in the numbers")
even_num=[x for x in numbers  if x % 2 ==0]
print("even numbers:", even_num )
elements=int(input("enter the new element to add:"))
numbers.append(elements)
print("after appending the elements:", numbers)
element=int(input("enter the number to be removed:"))
if element in numbers:
    numbers.remove(element)
    print("after removing the elements:", numbers)
else:
    print("removing elment is not found")
numbers.sort()
print("after sorting:", numbers)
numbers.reverse()
print("after reversing:", numbers)