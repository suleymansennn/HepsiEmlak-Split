import pandas as pd
import streamlit as st


data = st.file_uploader("Choose Data", type="csv")

if data:
    new_df = pd.read_csv(data)

threshold=4999
loop_n = new_df.shape[0] // 4999

for i in range(loop_n+1):
        if i == 0:
            exec(f"formatted_data{i} = new_df.loc[:(i + 1) * threshold]")
        else:

            if loop_n == i:

                exec(f"formatted_data{i} = new_df.loc[(i * threshold) + 1:new_df.shape[0] + 1]")
            else:
                exec(f"formatted_data{i} = new_df.loc[(i * threshold) + 1:(i + 1) * threshold]")

        st.download_button(f"Download formatted data part{i} as CSV", data=eval(f"formatted_data{i}").to_excel("123.xlsx"))
                        
