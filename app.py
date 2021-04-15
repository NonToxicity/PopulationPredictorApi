import flask
from flask import request
import pandas as pd
import pickle

app = flask.Flask(__name__)

@app.route('/',methods = ['GET'])
def home():
    try:
        arg = request.args['arg']
        array = arg.split(",")
        countryname = array[0]
        year = array[1]
        intyear = int(year)
        if(intyear < 1960):
            prediction = calculate(countryname,intyear)
            return prediction
        filename = "" + countryname + ".sav"
        loaded_model = pickle.load(open(filename, 'rb'))
        result = loaded_model.predict([[year]])
        if(int(result[0][0]) < 0):
            return 0
        return str(result[0][0])
    except:
        return str(-1)

def calculate(country,year):
    try:
        df = pd.read_csv('pop.csv')
        df = df.fillna(0) 
        bd=df.loc[df['Country Name']==str(country)]
        bd.drop(['Country Name','Country Code','Indicator Name','Indicator Code'],axis=1,inplace=True)
        bd = bd.T
        pop = bd.iloc[0]
        pop = bd.iloc[0]
        pop = pop.to_numpy()
        intpop = int(pop[0])
        population = intpop
        for i in range(abs(year-1960)):
            population = population - (population*1.5)/100
        return str(int(population))
    except:
        return str(-1)