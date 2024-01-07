#creating series
import pandas as pd

stu = {"Rohit" : 90, "Kanika" : 88, "Ruhana" : 96, "Shobit" : 65, "Ziyan" : 99}

s = pd.Series(stu)
print(s)
print("*"*40)
print(s.size)
print(s.nbytes)
print("*"*40)
print(s[s >= 80])
print("*"*40)
print(s-2)
print("*"*40)
print(s.sort_values())
