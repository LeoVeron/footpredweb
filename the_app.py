import streamlit as st
import datetime
import requests
import numpy as np
import pandas as pd

st.markdown("""

    # Boire ou choisir il me faut un taxi :taxi:

""")
st.write('')
st.write('')

st.markdown("""
    - T'es ou **mec**?
""")

row1_space1, row1_1, row1_space2, row1_2, row1_space3 = st.beta_columns((.1, 1, .1, 1, .1))

with row1_1:

	# PU lon ----------------------------------------------------------------
	pickup_longitude = st.number_input('Insert a pickup_longitude',value=-73)
	
with row1_2:
	# st.write('The current pickup_longitude is ', pickup_longitude)
	# PU lat ----------------------------------------------------------------
	pickup_latitude = st.number_input('Insert a pickup_latitude',value=43)
	

st.write('')
st.write('')
st.markdown("""
    - Tu vas ou **mec**?
""")

row2_space1, row2_1, row2_space2, row2_2, row2_space3 = st.beta_columns((.1, 1, .1, 1, .1))
with row2_1:
	# st.write('The current pickup_latitude is ', pickup_latitude)
	# DO lat ----------------------------------------------------------------
	dropoff_longitude = st.number_input('Insert a dropoff_longitude',value=-74)

with row2_2:
	# st.write('The current dropoff_longitude is ', dropoff_longitude)
	# DO lat ----------------------------------------------------------------
	dropoff_latitude = st.number_input('Insert a dropoff_latitude',value=42)

# st.write('The current dropoff_latitude is ', dropoff_latitude)




df = pd.DataFrame(
    {
        'lat':[pickup_latitude,dropoff_latitude],
        'lon':[pickup_longitude,dropoff_longitude]
    }
)


st.write('')
st.write('')
st.markdown("""
    - T'es combien dans ta tete **mec**?
""")

np_passenger = st.radio('', [1,2,3,4, 10, 1000])
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)


'''
## Combien ça va te couter **mec**?
'''
	


url = 'http://taxifare.lewagon.ai/predict_fare/'

input_data= {
        "dropoff_latitude":dropoff_latitude, 
        "dropoff_longitude":dropoff_longitude, 
        "key":"2015-01-27 13:08:24.0000002", 
        "passenger_count":np_passenger, 
        "pickup_datetime":"2015-01-27 13:08:24 UTC", 
        "pickup_latitude":pickup_latitude,
        "pickup_longitude":pickup_longitude}

#url ='http://taxifare.lewagon.ai/predict_fare/?key=2012-10-06%2012:10:20.0000001&pickup_datetime=2012-10-06%2012:10:20%20UTC&pickup_longitude=40.7614327&pickup_latitude=-73.9798156&dropoff_longitude=40.6513111&dropoff_latitude=-73.8803331&passenger_count=2'
response = requests.get(url,params=input_data)
price = round(response.json()['prediction'],0)

nb_86 = int(price/1.2)

if st.button('Calculer le prix!'):
	
	st.write(f"Le prix est fixé à {nb_86} canettes! N'oublie pas de discuter avec ton chauffeur pour pas qu'il ne s'endorme sur sa biere!")
	
	row3_1, row3_2 = st.beta_columns(2)
	with row3_1:
		st.image('86.png')
	with row3_2	:
		st.write('')
		st.write('')
		st.write('')
		st.write('')
		st.write(f'x{nb_86}')
