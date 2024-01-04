import pandas as pd
import matplotlib.pyplot as plt
subjects = ["CS", "IP", "IT"]
students = [50, 35, 15]
plt.pie(students, colors = ['pink', 'cyan', 'magenta'], labels = subjects)
plt.title("Students Option for CS/IP/IT")
plt.show()
