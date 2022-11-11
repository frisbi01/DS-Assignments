# Importing Packages
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import streamlit as st

# We are gonna make a webapp that predicts if you would survive the Titanic
# with a hypothetical profile


# Reading the csv files
# Will change the directory before sending for evaluation
df_train = pd.read_csv('train.csv')
df_test = pd.read_csv('test.csv')

# Preprocessing the data as explained in the notebook

# Filling missing values and changing data types
df_train_2 = df_train.copy()
df_train_2["Age"].fillna(df_train["Age"].median(), inplace=True)
df_train_2["Age"] = df_train_2["Age"].astype("int64")

df_test_2 = df_test.copy()
df_test_2["Age"].fillna(df_test["Age"].median(), inplace=True)
df_test_2["Age"] = df_test_2["Age"].astype("int64")

# Dropping unecessary columns
df_train_2.drop('Cabin', axis=1, inplace=True)
df_train_2.drop('Ticket', axis=1, inplace=True)
df_train_2.drop('Name', axis=1, inplace=True)
df_train_2.drop('PassengerId', axis=1, inplace=True)

df_test_2.drop('Cabin', axis=1, inplace=True)
df_test_2.drop('Ticket', axis=1, inplace=True)
df_test_2.drop('Name', axis=1, inplace=True)

# Filling in some more missing values
df_train_2["Embarked"].fillna("S", inplace = True)

df_test_2["Embarked"].fillna("S", inplace= True)
df_test_2["Fare"].fillna(14.45, inplace=True)

# Changing data types with Label Encoder
le = LabelEncoder()
for x in df_train_2.select_dtypes(["object_"]).columns:
    df_train_2[x] = le.fit_transform(df_train_2[x]).astype("str")

for x in df_test_2.select_dtypes(["object_"]).columns:
    df_test_2[x] = le.fit_transform(df_test_2[x]).astype("str")

# Creating X and y
X_train = df_train_2.drop("Survived" , axis=1)
y_train = df_train_2["Survived"]
X_test = df_test_2.drop("PassengerId", axis=1).copy()



# Run the data through a scaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Headings for our data application
st.title('Titanic - Machine Learning from Disaster')


# We need user inputs so we make a function
def user_report():
    age = st.sidebar.slider('What is your age? :', 5, 80, 30)
    sex = st.sidebar.selectbox('What is your gender? :',['Male', 'Female'])
    if (sex == 'Male'):
        Sex=1
    else:
        Sex=0
    fare = st.sidebar.slider("Fare prince $ : ", 0, 512, 32)
    sibsp = st.sidebar.selectbox("How many siblings and/or spouces are you travelling with?", [0,1,2,3,4,5,6,7,8])
    parch = st.sidebar.selectbox("How many parents and/or children are you travelling with?", [0,1,2,3,4,5,6,7,8])
    pclass = st.sidebar.selectbox("Select your passenger class:",[1,2,3])
    boardloc = st.sidebar.selectbox("Select your boarding location:",["Cherbourg","Queenstown","Southampton"])
    embarked = 3
    if boardloc == "Cherbourg":
        embarked = 0
    elif boardloc == "Queenstown":
        embarked= 1
    else:
        embarked = 2
    user_input = {
        'Pclass': pclass,
        'Sex': Sex,
        'Age': age,
        'SibSp': sibsp,
        'Parch': parch,
        'Fare': fare,
        'Embarked': embarked,
    }
    report_data = pd.DataFrame(user_input , index = [0])
    return report_data

user_data = user_report()

st.header('Your profile')
st.write(user_data)

# Model Training
lr = LogisticRegression()
lr.fit(X_train, y_train)
user_result = lr.predict(user_data)

# Output 
st.subheader('Your survivability report: ')
output = ''
if user_result[0]==0:
    output = 'You did not make it in the end'
else:
    output = 'You were so lucky!'
st.title(output)
st.subheader('Accuracy: ')
score = lr.score(X_train, y_train)
st.write(score)