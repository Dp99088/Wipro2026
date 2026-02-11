import seaborn as sns
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [25000, 27000, 30000, 28000, 32000, 31000]

plt.figure(figsize=(8,5))
plt.plot(months,sales,marker='o',linestyle='--')

plt.title("Monthly Sales Line Chart")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

plt.figure(figsize=(8,5))
sns.barplot(x=months, y=sales)

plt.title("Monthly Sales Bar Chart")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.grid(True)
plt.show()