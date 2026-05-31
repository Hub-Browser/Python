import array as a
arrayy=a.array("i",[1,3,5,3,7,9,3])
print("Original array:",str(arrayy))
print("Occurances of 3:",arrayy.count(3))
arrayy.reverse()
print("Array reversed:",str(arrayy))