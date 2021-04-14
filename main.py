import streamlit as st


st.title('Streamlit 超入門')
st.write('Interactive Widgets')

left_column,right_column=st.beta_columns(2)
button=left_column.button('右カラムに文字を表示')

if button:
    right_column.write('ここは右カラム')

expander1=st.beta_expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2=st.beta_expander('問い合わせ2')
expander3=st.write('問い合わせ3の回答')
