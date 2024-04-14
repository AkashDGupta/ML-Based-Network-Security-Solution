
# Reading CSV data file using PANDAS
import pandas as pd
df = pd.read_csv("C:/Users/akagupta/Desktop/AI-Learning/Step-1-Raw Network Data/Train_Test_Network.csv")
print('#########Pre_Transformation Test Data#########')
print(df.head(5))

# Label encoding of field 'src_ip' for data processing
from sklearn.preprocessing import LabelEncoder
num = LabelEncoder()
df['src_ip'] = num.fit_transform(df['src_ip'])
print('#########POST_Transformation Test Data-src_ip only#########')
print(df.head(5))


# Label encoding of field 'dst_ip', 'proto', 'service' and 'type' for data processing
df['dst_ip'] = num.fit_transform(df['dst_ip'])
df['proto'] = num.fit_transform(df['proto'])
df['service'] = num.fit_transform(df['service'])
df['type'] = num.fit_transform(df['type'])
print('#########POST_Transformation Test Data-After All Label Encoding#########')
print(df.head(5))


# Value of label 'type' assigned as y.  Possible values of y is :- 0- normal , 1- attack
y = df['type'].values


# Value of features assignment as X. All fields except field 'type' assigned as features.
X = df.drop(columns = ['type']).values


# Splitting data into training and testing sets using train_test_split module

from sklearn.model_selection import train_test_split

# Splitted data into 70% training and 30% testing data set
X_train , X_test , y_train , y_test = train_test_split (X, y, test_size =0.3, random_state =1)

# Selecting model DecisionTreeClassifier from list of availble models sklearn for training dataset

from sklearn . tree import DecisionTreeClassifier
model = DecisionTreeClassifier ()

# Trainning the model
model.fit (X_train , y_train)

# Prediction using the testing phase
y_pred = model.predict ( X_test )

# Accuracy Score mesurement using accuracy_score module   
from sklearn.metrics import accuracy_score , confusion_matrix
print('#########Trained Model Accuracy Mesurement#########')
print ("Accuracy", accuracy_score (y_pred , y_test ))

# Confusion Matrix mesurement using confusion_matrix module 
print('#########Confusion Matrix for Trained Model#########')
print ("Confusion Matrix", confusion_matrix (y_pred , y_test ))



