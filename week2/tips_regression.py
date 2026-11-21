import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

url="https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df=pd.read_csv(url)
print(df.head())

# sklearn section

x=df[["total_bill"]]
y=df["tip"]
model=LinearRegression().fit(x,y)
print(model.coef_,model.intercept_)


# chart ( under the model )
plt.scatter(df["total_bill"],df["tip"])
plt.plot(df["total_bill"], model.predict(x), color="red")
plt.xlabel("Total bill")
plt.ylabel("Tip")
plt.title("Tip vs total bill")
plt.show()