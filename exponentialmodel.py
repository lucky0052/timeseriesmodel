# weekly model
import joblib
import joblib
from statsmodels.tsa.statespace.sarimax import SARIMAX
# from sklearn.metrics import mean_absolute_percentage_error
import pandas as pd

model2 = joblib.load('expomodel.pkl')
result2 = model2.fit()

data = pd.read_csv('train.csv')
new_data = data.iloc[:,[1,4]]
new_data['date'] = pd.DatetimeIndex(new_data['date'])
new_data.set_index('date',inplace=True)
weekly_data = new_data.resample('W').sum()
weekly_resampled_data = weekly_data[weekly_data.index.year < 2017]




def week_res(data):    
    # Forecast future sales for the next 4 weeks
    forecast_periods = data
    forecast = result2.forecast(steps=forecast_periods)


    forecast_index = pd.date_range(start=weekly_resampled_data.index[-1] + pd.DateOffset(1), periods=forecast_periods, freq='W')
    # forecast_df = pd.DataFrame({'Date': forecast_index, 'Forecast': forecast})
    # return forecast_df.set_index('Date')
    forecast_df = pd.DataFrame({'Date': forecast_index, 'Forecast': forecast})



    return forecast_df


# print(week_res(2))


