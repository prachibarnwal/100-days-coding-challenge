#data visualization
import matplotlib.pyplot as plt

c1 = [1900, 2100, 1400, 1800]
c2 = [1600, 2200, 1500, 1700]
years = ["2018", '2019', '2020', '2021']
plt.plot(years, c1, color = 'red', label = 'Company A')
plt.plot(years, c2, color = 'green', label = 'Company B')
plt.legend(loc = 'upper right')
plt.title("Sales Record (2018-2021)")
plt.xlabel("Sales Year")
plt.ylabel("Sales in Lakhs INR")
plt.grid(True)
plt.show()
