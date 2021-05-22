import streamlit as st
from joblib import load


def main(): 

    def load_model(file):
        loaded_model = load(file)
        return loaded_model

    st.write("""
    ## Testing Streamlit (checking for change)
    """)
    rf_env = load_model('models/crop_outlook_rfg1.joblib')

    def env_rating(temp, soil_mois, hum):
        result = rf_env.predict([[temp, soil_mois, hum]])
        # print('Environment Rating: ' + str(round(result[0], 2)) + '%')
        return str(round(result[0], 2))

    temp2 = st.number_input('T ', 0, 100)
    soil_mois2 = st.number_input('S', 0, 100)
    hum2 = st.number_input('H ', 0, 100)

    if st.button('Run Model'):
        rating = env_rating(temp2, soil_mois2, hum2)
        print('Rating:', rating)
        st.write(str(rating) + '%')

if __name__ == '__main__':
	main()