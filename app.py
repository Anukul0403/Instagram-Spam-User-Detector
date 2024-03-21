from flask import Flask, render_template,url_for,request
import pandas as pd
import numpy as np
from sklearn import neighbors, metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('project.html')

@app.route('/predict',methods=['POST'])

def predict():
    data = pd.read_csv('train.csv')
    X = data.drop(['fake','nums/length username','fullname words','nums/length fullname','external URL'],axis=1)
    y = data['fake']
    X_train, X_test, y_train, y_test = train_test_split(X,y)
    knn = neighbors.KNeighborsClassifier(n_neighbors=25,weights='uniform')
    knn.fit(X_train,y_train)
    predictions=knn.predict(X_test)
    accuracy = metrics.accuracy_score(y_test,predictions)
    print("Accuracy : ",round(accuracy*100),'%')
    
    if request.method == 'POST':
        link = request.form['link']
        input_data = link.split(",")
        input_data = [int(i) for i in input_data]
        in_data = np.array(input_data)
        in_data_reshaped = in_data.reshape(1,-1)
        sample = knn.predict(in_data_reshaped)
    return render_template('result.html',prediction=sample)
if __name__ =='__main__':
    app.run(debug=True)