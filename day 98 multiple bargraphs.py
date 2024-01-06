#multiple bar graphs using dataframes
import pandas as pd
import matplotlib.pyplot as plt

c1 = [1900, 1000, 1400, 1800]
c2 = [1600, 2200, 1500, 1600]
c3 = [1900, 2500, 1300, 1800]


years = ['2018','2019','2020','2021']
df = pd.DataFrame({"Years" : years, "Company A" : c1, "Company B" : c2, "Company C" : c3})
df.index = df['Years']
df.plot(kind = 'bar', color = ['magenta', 'pink', 'yellow', 'orange', 'pink'])
plt.title("Sales Record 2018-2021")
plt.xlabel("Sale Year")
plt.ylabel("Sales in Lakhs INR")
plt.show()
                  
