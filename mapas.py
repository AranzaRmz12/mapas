import pandas as pd
import numpy as np
import streamlit as st

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [20.612152, -100.402321],
    columns = ['lat', 'lon']
    )
st.dataframe(map_data)
st.map(map_data)