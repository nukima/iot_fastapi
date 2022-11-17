import pickle
import pandas as pd

#load model
model = pickle.load(open(file='finalized_model.sav', mode='rb'))

def predict_ppm(data: dict):
    data_df = pd.DataFrame(data, index=[0]).drop('ppm', axis=1)
    prediction = model.predict(data_df)
    return prediction[0]

if __name__ == '__main__':
    data_sample = {'time': 1668357957, 'co': 864.59, 'alcohol': 103.05, 'co2': 543.18, 'toluen': 61.41, 'nh4': 127.87, 'aceton': 47.04, 'ppm': 1747.15, 'temperature': 30.2, 'humidity': 67.0}
    print(predict_ppm(data_sample))