from flask import Flask, render_template, request
import pickle
import warnings
from sklearn.exceptions import InconsistentVersionWarning
import joblib
import numpy as np

warnings.filterwarnings("ignore", category=InconsistentVersionWarning)

app = Flask(__name__)

def prediction(lst):
    filename = r"C:\Users\hashan indeewara\Diabetes\website\model\predictor.pickle"
    with open(filename,'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict([lst])
    return pred_value

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def index():
    pred = -1
    if request.method == 'POST':
        HighBP = request.form['HighBP']
        HighChol = request.form['HighChol']
        CholCheck = request.form['CholCheck']
        BMI = request.form['BMI']
        Smoker = request.form['Smoker']
        Stroke = request.form['Stroke']
        HeartDiseaseorAttack = request.form['HeartDiseaseorAttack']
        PhysActivity = request.form['PhysActivity']
        Fruits = request.form['Fruits']
        Veggies = request.form['Veggies']
        HvyAlcoholConsump = request.form['HvyAlcoholConsump']
        GenHlth = request.form['GenHlth']
        MentHlth = request.form['MentHlth']
        PhysHlth = request.form['PhysHlth']
        DiffWalk = request.form['DiffWalk']
        Sex = request.form['Sex']
        Age = request.form['Age']
        Education = request.form['Education']
        Income = request.form['Income']

        feature_list = []
        # Append NaN if the value is empty or convert to float if not empty
        feature_list.append(float(HighBP))
        feature_list.append(float(HighChol))
        feature_list.append(float(CholCheck))
        feature_list.append(float(BMI))
        feature_list.append(float(Smoker))
        feature_list.append(float(Stroke))
        feature_list.append(float(HeartDiseaseorAttack))
        feature_list.append(float(PhysActivity))
        feature_list.append(float(Fruits))
        feature_list.append(float(Veggies))
        feature_list.append(float(HvyAlcoholConsump))
        feature_list.append(float(GenHlth))
        feature_list.append(float(MentHlth))
        feature_list.append(float(PhysHlth))
        feature_list.append(float(DiffWalk))
        feature_list.append(float(Sex))
        feature_list.append(float(Age))
        feature_list.append(float(Education))
        feature_list.append(float(Income))

        pred = prediction(feature_list)
        pred = pred[0]
        
    return render_template("result.html", pred=pred)

if __name__ == '__main__':
    app.run(debug=True)



# from flask import Flask, render_template, request
# import pickle
# import warnings
# from sklearn.exceptions import InconsistentVersionWarning
# import joblib
# import numpy as np

# warnings.filterwarnings("ignore", category=InconsistentVersionWarning)

# app = Flask(__name__)

# def prediction(lst):
#     filename = 'model/predictor.pickle'
#     with open(filename,'rb') as file:
#         model = pickle.load(file)
#     pred_value = model.predict([lst])
#     return pred_value

# @app.route('/')
# def form():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def index():
#     pred = -1
#     if request.method == 'POST':
#         HighBP = request.form['HighBP']
#         HighChol = request.form['HighChol']
#         CholCheck = request.form['CholCheck']
#         BMI = request.form['BMI']
#         Smoker = request.form['Smoker']
#         Stroke = request.form['Stroke']
#         HeartDiseaseorAttack = request.form['HeartDiseaseorAttack']
#         PhysActivity = request.form['PhysActivity']
#         Fruits = request.form['Fruits']
#         Veggies = request.form['Veggies']
#         HvyAlcoholConsump = request.form['HvyAlcoholConsump']
#         GenHlth = request.form['GenHlth']
#         MentHlth = request.form['MentHlth']
#         PhysHlth = request.form['PhysHlth']
#         DiffWalk = request.form['DiffWalk']
#         Sex = request.form['Sex']
#         Age = request.form['Age']
#         Education = request.form['Education']
#         Income = request.form['Income']

#         feature_list = []
        # feature_list.append(float(HighBP))
        # feature_list.append(float(HighChol))
        # feature_list.append(float(CholCheck))
        # feature_list.append(float(BMI))
        # feature_list.append(float(Smoker))
        # feature_list.append(float(Stroke))
        # feature_list.append(float(HeartDiseaseorAttack))
        # feature_list.append(float(PhysActivity))
        # feature_list.append(float(Fruits))
        # feature_list.append(float(Veggies))
        # feature_list.append(float(HvyAlcoholConsump))
        # feature_list.append(float(GenHlth))
        # feature_list.append(float(MentHlth))
        # feature_list.append(float(PhysHlth))
        # feature_list.append(float(DiffWalk))
        # feature_list.append(float(Sex))
        # feature_list.append(float(Age))
        # feature_list.append(float(Education))
        # feature_list.append(float(Income))

#         pred = prediction(feature_list)
#         pred = pred[0]
        
#     return render_template("result.html", pred=pred)

# if __name__ == '__main__':
#     app.run(debug=True)











