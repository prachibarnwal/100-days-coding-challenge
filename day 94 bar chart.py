#data visualization
import matplotlib.pyplot as plt
a = ['CS', 'English', 'Maths', 'Mechanics', 'EVs']
b = [99, 95, 96, 93, 98]
#bar chart
plt.bar(a,b, color = ('purple',  'cyan', 'beige', 'pink', 'orange'))
plt.title("Student's Report")
plt.xlabel("Subject")
plt.ylabel("Marks")
plt.show()
