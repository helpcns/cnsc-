
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


#data =load_iris()



iris=load_iris()
x=iris.data
y=iris.target

#x_train,x_test,y_train,y_test=train_test_split(data.data,data.target,test_size=0.4,random_state=5)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.4,random_state=5)
model=KNeighborsClassifier(n_neighbors=5)
model.fit(x_train,y_train)
y_pred=model.predict(x_test)

print("Acuraccy of KNN\t\t\t\t",accuracy_score(y_pred,y_test))

pd.DataFrame({'actual':y_test,'predction':y_pred,'correct classification':(y_test==y_pred)})

count = 0
for i in range(len(y_pred)):
    if(y_pred[i]!=y_test[i]):
        count=count+1
print(count)











