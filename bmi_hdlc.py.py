import streamlit as st 

st.title("This is My BMI Calculator")

name=st.text_input('Your Name: ')
gender = st.radio(
    "What's your gender",
    ('Male', 'Female', 'Do not wish to specify'))
age=st.number_input('Please Enter Your Age: ')
address= st.text_input('Your Address: ')
st.write('Select your hobbies:')
option_1 = st.checkbox('Singing')
option_2 = st.checkbox('Dancing')
option_3 = st.checkbox('Reading')
option_4 = st.checkbox('Coding')
option_5 = st.checkbox('Playing sports')
height = st.number_input('Please Enter Your Height in Cms: ',100,300 )
weight = st.number_input('Please Enter Your Weight in Kgs: ' )

check = st.button('Find BMI')
if(check):
    bmi = round(weight/height/height*10000,2)
    st.title(f'Your BMI : {bmi}')
    if(bmi>30):
        st.title('You are Obese.')
    elif(bmi>25):
        st.title('You are Overweight.')
    elif(bmi>18.5):
        st.title('You are Normal Weight.')
    else:
        st.title('You are Underweight.')





