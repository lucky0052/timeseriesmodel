import joblib
from statsmodels.tsa.statespace.sarimax import SARIMAX
# from sklearn.metrics import mean_absolute_percentage_error
import pandas as pd



data = pd.read_csv('newtrain.csv')
data['date'] = pd.DatetimeIndex(data['date'])
data.set_index('date',inplace=True)

# Load the model from the file
yearly_model = joblib.load('yearly.pkl')
result = yearly_model.fit()


train_size = len(data[data.index.year < 2016])
train, test = data[:train_size], data[train_size:]

start = len(train)
end = len(train) + len(test) - 1

# Predictions for one-year against the test set
pred1 = result.predict(start, end,
                             typ = 'levels').rename("Pred")


def get_prediction(data):
    
  
# Forecast for the next 3 years
    year_forecast = result.predict(start = 36, 
                            end = 36 + data * 12, 
                            type = 'levels').rename('Forecast')
    
    halfyear_forecast = result.predict(start = 36, 
                            end = 36 + data * 6, 
                            type = 'levels').rename('Forecast')

    result_list =  list()
    result_list.append(year_forecast)
    result_list.append(halfyear_forecast)
    return result_list
    


    # Plot the forecast values
    # new_monthly_data.plot(figsize = (12, 5), legend = True);
    # forecast.plot(legend = True)

# def mape_metrics():
#     return 100 - mean_absolute_percentage_error(test,pred1)




