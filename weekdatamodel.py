# import pandas as pd
# # from prophet import Prophet
# import joblib 


# data = pd.read_csv('train.csv')
# new_data = data.iloc[:,[1,4]]
# new_data['date'] = pd.DatetimeIndex(new_data['date'])
# new_data.set_index('date',inplace=True)



# weekly_data = new_data.resample('W').sum()
# weekly_resampled_data = weekly_data[weekly_data.index.year < 2017]

# wdata = weekly_resampled_data.reset_index()

# # Prepare data in the required format
# model5 = joblib.load('promodel.pkl')

# wdata.rename(columns={"date": "ds", "sales": "y"},inplace=True)

#   # Rename columns to 'ds' and 'y'

# X_train = wdata
# # X_test = wdata.iloc[-3:,:]

# # Create and fit a Prophet model

# def get_weekly(data):

    
#     model5.fit(X_train)

#     # Make future predictions
#     future = model5.make_future_dataframe(periods=data, freq='W')  # Replace 10 with the number of future periods
#     forecast = model5.predict(future)

#     res = pd.DataFrame()
#     res['date'] = forecast.iloc[-data:,0]
#     res['sales'] = forecast.iloc[-data:,-1]
#     res_store = res.set_index('date')
#     return res_store

