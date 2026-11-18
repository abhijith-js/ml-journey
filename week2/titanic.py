import pandas as pd

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url)

df["age"] = df["age"].fillna(df["age"].median())
df = df.drop(columns=["deck"])

print(df.shape)
print(df.groupby(["sex", "pclass"])["survived"].mean())
print(df.groupby("embarked")["survived"].mean())
print(df.groupby("embarked")["sex"].value_counts(normalize=True))
print("----")
print(df['sex'].value_counts())

print("------------------------------------------------------")

# import matplotlib.pyplot as plt

# rate=df.groupby("pclass")["survived"].mean()
# plt.bar(rate.index,rate.values)
# plt.xlabel("Class")
# plt.ylabel("Survival rate")
# plt.title("survival rate bt class")
# plt.show()


import matplotlib.pyplot as plt
rate=df.groupby("sex")['survived'].mean()

plt.bar(rate.index,rate.values)
plt.xlabel("Sex")
plt.ylabel("Survival rate")
plt.title("Survival rate by sex")
plt.show()

print("---------")
print(df.sort_values("fare",ascending=False).head(5))