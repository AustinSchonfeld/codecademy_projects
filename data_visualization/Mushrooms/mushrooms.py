import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# load in the data
df = pd.read_csv("mushrooms.csv")
print(df.head())

# list of all column headers
columns = df.columns.tolist()

x = [1,1,1,1,1,1,1,1]

#creates 23 (imperfect) countplot graphs for each column
for i in range(len(columns)):
    sns.countplot(x = df[columns[i]])
    plt.show()
    plt.savefig(columns[i] + ".png")
    plt.clf()
