import streamlit as st
from st_circular_progress import CircularProgress
import pandas as pd 

c1,c2=st.columns(2)
def change():
    df1 = pd.read_json('data.json', typ='series')
    data_dict = df1.to_dict()
    cp1.update_value(progress=data_dict["HR"])
    cp2.update_value(progress=data_dict["CAL"])
with c1:
    cp1 = CircularProgress(
            value=0,
            label="Heart Rate",
            size="Large",
            key="hr",
        )
    cp1.st_circular_progress()
with c2:
    cp2 = CircularProgress(
            value=0,
            label="Calories",
            size="Large",
            key="cal",
        )
    cp2.st_circular_progress()

hr=st.number_input("Heart Rate:", step=1)
cal=st.number_input("Calories:", step=1)
if hr or cal:
    df = pd.DataFrame([{"HR":hr, "CAL":cal}])
    df.to_json('data.json', orient='records', lines=True)
    change()
st.button("Refresh")


