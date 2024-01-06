#multiple bar graphs using dataframes
import pandas as pd
import matplotlib.pyplot as plt

c1 = [1200, 1600, 2590, 1800,2050]
c2 = [1300, 1700, 2400, 1900, 2100]
c3 = [1450, 1800, 2590, 2000, 2150]


years = ['2018','2019','2020','2021','2022']
df = pd.DataFrame({"Years" : years, "Company A" : c1, "Company B" : c2, "Company C" : c3})
df.index = df['Years']
df.plot(kind = 'bar', color = ['yellow', 'orange', 'red'])
plt.title("Sales Record 2018-2021")
plt.xlabel("Sale Year")
plt.ylabel("Sales in Lakhs INR")
plt.show()
                  
