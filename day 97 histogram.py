#histogram
import matplotlib.pyplot as plt

production = [4,6,7,29,49,20,48,39,21,21,22,59,39,40,38,33,67,21]
plt.hist(production,bins = 5)
plt.title("Production Records")
plt.xlabel("Production -->")
plt.ylabel("Rec -->")
plt.show()
