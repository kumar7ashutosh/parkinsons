import streamlit as st,pandas as pd,pickle

with open('log_reg.pkl','rb') as file:
    model=pickle.load(file)
with open('scaler.pkl','rb') as file:
    scaler=pickle.load(file)

st.title('Parkinsons checker')

V1 = st.number_input('Enter the V1')

V2 = st.number_input('Enter the V2')

V3 = st.number_input('Enter the V3')

V4 = st.number_input('Enter the V4')

V5 = st.number_input('Enter the V5')

V6 = st.number_input('Enter the V6')

V7 = st.number_input('Enter the V7')

V8 = st.number_input('Enter the V8')

V9 = st.number_input('Enter the V9')

V10 = st.number_input('Enter the V10')

V11 = st.number_input('Enter the V11')

V12 = st.number_input('Enter the V12')

V13 = st.number_input('Enter the V13')

V14 = st.number_input('Enter the V14')

V15 = st.number_input('Enter the V15')

V16 = st.number_input('Enter the V16')

V17 = st.number_input('Enter the V17')

V18 = st.number_input('Enter the V18')

V19 = st.number_input('Enter the V19')

V20 = st.number_input('Enter the V20')

V21 = st.number_input('Enter the V21')

V22 = st.number_input('Enter the V22')

ip_data=pd.DataFrame([[V1	,V2	,V3	,V4	,V5	,V6	,V7	,V8	,V9	,V10	,V11	,V12	,V13	,V14	,V15	,V16	,V17	,V18	,V19	,V20	,V21	,V22]],columns=[ 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
       'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20',
       'V21', 'V22'])

if st.button('Check :'):

  prediction = model.predict(ip_data)[0]

  if prediction==1:

   st.success('Parkinsons confirmed')

  else:

   st.success('Healthy')