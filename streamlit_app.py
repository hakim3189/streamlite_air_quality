# Library numpy untuk 
import numpy as np
# Library pandas untuk 
import pandas as pd
# Library matplotlib untuk 
import matplotlib.pyplot as plt
# Library seabord untuk 
import seaborn as sn

sns.set(style='dark')

Data_Aotizhongxin = pd.read_csv("PRSA_Data_Aotizhongxin_20130301-20170228.csv")
Data_Changping = pd.read_csv("PRSA_Data_Changping_20130301-20170228.csv")
Data_Dingling = pd.read_csv("PRSA_Data_Dingling_20130301-20170228.csv")
Data_Dongsi = pd.read_csv("PRSA_Data_Dongsi_20130301-20170228.csv")
Data_Guanyuan = pd.read_csv("PRSA_Data_Guanyuan_20130301-20170228.csv")
Data_Gucheng = pd.read_csv("PRSA_Data_Gucheng_20130301-20170228.csv")
Data_Huairou = pd.read_csv("PRSA_Data_Huairou_20130301-20170228.csv")
Data_Nongzhanguan = pd.read_csv("PRSA_Data_Nongzhanguan_20130301-20170228.csv")
Data_Shunyi = pd.read_csv("PRSA_Data_Shunyi_20130301-20170228.csv")
Data_Tiantan = pd.read_csv("PRSA_Data_Tiantan_20130301-20170228.csv")
Data_Wanliu = pd.read_csv("PRSA_Data_Wanliu_20130301-20170228.csv")
Data_Wanshouxigong = pd.read_csv("PRSA_Data_Wanshouxigong_20130301-20170228.csv")
Data_combine = pd.concat([Data_Aotizhongxin,Data_Changping,Data_Dingling,Data_Dongsi,Data_Guanyuan,Data_Gucheng,Data_Huairou,Data_Nongzhanguan,Data_Shunyi,Data_Tiantan,Data_Wanliu,Data_Wanshouxigong])

with st.sidebar:
    station = st.selectbox(
        label="Station",
        options=(Data_combine["station"].unique())
    )
    
    year = st.selectbox(
        label="Year",
        options=(Data_combine["year"].unique())
    )
    
    month = st.selectbox(
        label="Month",
        options=np.sort(Data_combine["month"].unique())
    )
    
    day = st.selectbox(
        label="Day",
        options=(Data_combine["day"].unique())
    )

selected_data = Data_combine[(Data_combine["station"] == station) & (Data_combine["year"] == year)& (Data_combine["month"] == month)& (Data_combine["day"] == day)]


st.header('Hourly Trend Weather Indicator :sparkles:')
#st.subheader('Daily Orders')

col1, col2 = st.columns(2)

with col1:

    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
        selected_data["hour"],
        selected_data["WSPM"],
        marker='o', 
        linewidth=5,
        color="Red"
    )
    ax.set_title("WSPM Trend", loc="center", fontsize=25)
    ax.tick_params(axis='y', labelsize=15)
    ax.tick_params(axis='x', labelsize=15)
    ax.set_ylabel("WSPM")
    ax.set_xlabel("Hour")
    st.pyplot(fig)


with col2:
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
        selected_data["hour"],
        selected_data["RAIN"],
        marker='o', 
        linewidth=5,
        color="Red"
    )
    ax.set_title("RAIN Trend", loc="center", fontsize=25)
    ax.tick_params(axis='y', labelsize=15)
    ax.tick_params(axis='x', labelsize=15)
    ax.set_ylabel("RAIN")
    ax.set_xlabel("Hour")
    st.pyplot(fig)
    
col1, col2 = st.columns(2,gap="small")


with col1:

    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
        selected_data["hour"],
        selected_data["NO2"],
        marker='o', 
        linewidth=5,
        color="Red"
    )
    ax.set_title("NO2 Trend", loc="center", fontsize=25)
    ax.tick_params(axis='y', labelsize=15)
    ax.tick_params(axis='x', labelsize=15)
    ax.set_ylabel("NO2")
    ax.set_xlabel("Hour")
    st.pyplot(fig)

with col2:

    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
        selected_data["hour"],
        selected_data["CO"],
        marker='o', 
        linewidth=5,
        color="Red"
    )
    ax.set_title("CO Trend", loc="center", fontsize=25)
    ax.tick_params(axis='y', labelsize=15)
    ax.tick_params(axis='x', labelsize=15)
    ax.set_ylabel("CO")
    ax.set_xlabel("Hour")
    st.pyplot(fig)

col1, col2 = st.columns(2,gap="small")

with col1:

    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
        selected_data["hour"],
        selected_data["O3"],
        marker='o', 
        linewidth=5,
        color="Red"
    )
    ax.set_title("O3 Trend", loc="center", fontsize=25)
    ax.tick_params(axis='y', labelsize=15)
    ax.tick_params(axis='x', labelsize=15)
    ax.set_ylabel("O3")
    ax.set_xlabel("Hour")
    st.pyplot(fig)
    
with col2:

    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
        selected_data["hour"],
        selected_data["SO2"],
        marker='o', 
        linewidth=5,
        color="Red"
    )
    ax.set_title("SO2 Trend", loc="center", fontsize=25)
    ax.tick_params(axis='y', labelsize=15)
    ax.tick_params(axis='x', labelsize=15)
    ax.set_ylabel("SO2")
    ax.set_xlabel("Hour")
    st.pyplot(fig)
