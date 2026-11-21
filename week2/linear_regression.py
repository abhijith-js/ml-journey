import numpy as np

from sklearn.linear_model import LinearRegression

# hours=np.array([[1],[2],[3],[4],[5]])
# marks=np.array([25,35,45,55,65])

# model=LinearRegression().fit(hours, marks)
# print(model.coef_,round(model.intercept_))
# print(model.predict([[8]]))


hours=np.array([[1],[2],[3],[4],[5]])
marks=np.array([28,33,47,52,66])
model= LinearRegression().fit(hours, marks)
print(model.coef_, model.intercept_)
print(model.predict([[8]]))