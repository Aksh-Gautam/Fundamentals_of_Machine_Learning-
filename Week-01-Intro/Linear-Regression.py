# import libraries 
import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error,r2_score

#create a dataframe
df = pd.DataFrame({'Hours': [1,2,3,4,5,6,7,8,9,10],
                   'Marks Obtained' : [10,20,30,40,50,60,70,80,90,100]
                   })

#splitting into features and target
x=df[['Hours']] #features are in 2D array by sklearn standards
y=df['Marks Obtained'] #target is in 1D array

#splitting into training and testing data
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

#train the model
model=LinearRegression()
model.fit(x_train,y_train)

#Prediction -- Done on test data
y_pred=model.predict(x_test)
print ('Predicted Marks are: ', y_pred)

#plotting
plt.scatter(x,y,color='cyan')
plt.plot(x,model.predict(x), color='green')
plt.xlabel('Hours')
plt.ylabel('Marks Obtained')
plt.title('Test Score Prediction')
plt.show()

#evaluation
print('Mean Squared Error: ', mean_squared_error(y_test,y_pred))
print ('R2 score:', r2_score(y_test,y_pred))
print('RMSE: ', np.sqrt(mean_squared_error(y_test,y_pred)))