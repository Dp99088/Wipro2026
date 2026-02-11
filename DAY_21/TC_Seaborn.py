import matplotlib.pyplot as plt
import seaborn as sns

marks=[50,60,70,80,90,65]

sns.set_style("whitegrid")
sns.histplot(marks,bins=5)
plt.title("Marks")
plt.show()