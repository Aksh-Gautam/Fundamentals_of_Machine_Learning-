import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
#load dataset
df=sns.load_dataset('titanic')
df.head()
#select required columns
df=df[['pclass','age','sex','fare','survived']]
#check missing values
print('Missing values before cleaning:')
print(df.isnull().sum())
# drop rows containing missing values
df=df.dropna()
print(df.isnull().sum())

# convert male/female to 0/1
df ['sex'] = df['sex'].map({'female': 1, 'male' : 0})
print(df)

#features and target
X = df[['pclass','age','sex','fare']]
y = df['survived']

#split dataset
X_train,X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)

#create model
model = LogisticRegression(max_iter=1000)
#max_iter -maximum no of iterations the model is allowed to perform 
#model= LogosticRegression(max_iter=1000) means the model can take upto 1000 iterations 
#to find a  solution
#why do we use max_iter = 1000 LogisticRegression is trained iteratively the model keeps adjusting 
#its cofficients unitl it converges 

#train model
model.fit(X_train,y_train)

#prediction 
y_pred=model.predict(X_test)

#Accuracy 
print('Accuracy: ', accuracy_score(y_test, y_pred))

#confession matrix
cm=confusion_matrix(y_test,y_pred)

# print heatmap
plt.figure(figsize=(5,4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('predicted')
plt.ylabel('Actual')
plt.title('confusion_matrix')
plt.show()

#predict new passenger
new_p = pd.DataFrame ({
    'pclass': [1],
    'sex':  [1],
    'age':  [25],
    'fare' : [100]
})
new_p = new_p[X.columns]
prediction = model.predict(new_p)
print ('prediction', prediction)

#predict another passenger

new_p = pd.DataFrame({
    'pclass':   [3],
    'sex' : [0],
    'age' : [45],
    'fare': [8]
    })
new_p = new_p[X.columns]
prediction = model.predict(new_p)
print('prediction: ', prediction)

#probabilty of survival (most imp.)
probability = model.predict_proba(new_p)
print('probability: ', probability)