numbers=[1,2,3,4,5,6,7]
odd=[x for x in numbers if x%2!=0]
print(odd)
my_dict={str(x):x*2 for x in numbers}
print(my_dict)