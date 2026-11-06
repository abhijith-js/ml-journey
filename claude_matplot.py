import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("marks.csv")
df["average"] = df[["maths", "python", "english"]].mean(axis=1)

print(df)

print("--"*25)

plt.xlabel("students")
plt.ylabel('Average marks')
plt.bar(df['name'],df["average"],color='r')
plt.title("Student Average Marks")
plt.axhline(40, color="green") #axhline=horizontal axvline =vertical

plt.show()