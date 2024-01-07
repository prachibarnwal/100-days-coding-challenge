#creating series
import pandas as pd

stu = {"Rohit" : 70, "Kanika" : 88, "Ruhana" : 96, "Shobit" : 65, "Ziyan" : 79}

s = pd.Series(stu)
print(s)
print("*"*45)
print("Size of Series : ",s.size)
print("Number of Bytes Taken : ",s.nbytes)
print("*"*45)
print("Students Having Marks >= 80 : ")
print(s[s >= 80])
print("*"*45)
print("Marks After Deducing 2 From Each : ")
print(s-2)
print("*"*45)
print("Data in Sorted Order of Marks : ")
print(s.sort_values())
