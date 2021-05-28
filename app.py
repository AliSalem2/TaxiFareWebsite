import streamlit as st
import requests
from datetime import datetime

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time

>>> d = st.date_input(
...     "When's your birthday",
...     datetime.date(2019, 7, 6))
>>> st.write('Your birthday is:', d)

- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''
"""https://taxifare.lewagon.ai/predict?pickup_datetime=2012-10-06%2012:10:20&pickup_longitude=40.7614327&pickup_latitude=-73.9798156&dropoff_longitude=40.6513111&dropoff_latitude=-73.8803331&passenger_count=2"""


#pickup_datetime = st.text_input('date and time')
#st.write('Your date and time is:', pickup_datetime)

d = st.date_input('date', datetime(2012,6,10))
t = st.time_input('Departure time', datetime(2012,6,10,10,20))



pickup_longitude = st.text_input('pickup longitude')
st.write('Your pickup longitude:', pickup_longitude)

pickup_latitude = st.text_input('pickup latitude')
st.write('Your pickup latitude:', pickup_latitude)

dropoff_longitude = st.text_input('dropoff longitude')
st.write('Your dropoff longitude:', dropoff_longitude)

dropoff_latitude = st.text_input('dropoff latitude')
st.write('Yourdropoff latitude:', dropoff_latitude)

passenger_count = st.text_input('passenger count')
st.write('Your passenger count:', passenger_count)


params = {"pickup_datetime": f'{d} {t}', 
          "pickup_longitude" : pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count}
        
#query= f"?pickup_datetime={pickup_datetime}&pickup_longitude={pickup_longitude}&pickup_latitude={pickup_latitude}&dropoff_longitude={dropoff_longitude}&dropoff_latitude={dropoff_latitude}&passenger_count={passenger_count}"


#url= f'https://taxifare.lewagon.ai/predict{query}'

base_url= f'https://taxifare.lewagon.ai/predict'

response = requests.get(base_url, params= params)
app = response.json()

st.write('prediction:', app['prediction'])



#if url == 'https://taxifare.lewagon.ai/predict':
#st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''