from statistics import LinearRegression

import pandas as pd

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from numpy import mean
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data = pd.read_csv('weight-height.csv')

x = data[["Weight"]]
y = data[["Height"]]


plt.scatter(x, y, color='red')
plt.xlabel('Weight')
plt.ylabel('Height')
plt.show()


md = LinearRegression()
md.fit(x, y)
prd_y = md.predict(x)
plt.scatter(x, y, color='red', label='Actual data')
plt.plot(x, prd_y, color='blue', label='predicted data')
plt.xlabel('Weight')
plt.ylabel('Height')
plt.title('Linear Regression of Height and Weight')
plt.show()



rmse = np.sqrt(mean_squared_error(y, prd_y))
print("Root Mean Square Error = ", rmse)

r2 = r2_score(y, prd_y)
print("R2 Score = ", r2)








