import pandas as pd
import streamlit as st
import openpyxl

data = st.file_uploader("Choose Data", type="xlsx")

if data:
    new_df = pd.read_excel(data)

threshold=3000
loop_n = new_df.shape[0] // 3000

for i in range(loop_n+1):
        if i == 0:
            exec(f"formatted_data{i} = new_df.loc[:(i + 1) * threshold]")
        else:

            if loop_n == i:

                exec(f"formatted_data{i} = new_df.loc[(i * threshold) + 1:new_df.shape[0] + 1]")
            else:
                exec(f"formatted_data{i} = new_df.loc[(i * threshold) + 1:(i + 1) * threshold]")

        st.download_button(f"Download formatted data part{i} as CSV", data=eval(f"formatted_data{i}").to_csv(index=False),
                           file_name=f"formatted_data_part{i}.csv")
