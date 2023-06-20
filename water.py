import streamlit as st
import pickle

# Load the trained model from the pickle file
model = pickle.load(open('water_potability.pkl', 'rb'))

def predict_potability(ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity):
    # Make predictions using the trained model
    attributes = [ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity]
    predictions = model.predict([attributes])

    return predictions[0]

def main():
    st.markdown(
        """
        <style>
        .reportview-container {
            background: url('https://previews.123rf.com/images/antonmedvedev/antonmedvedev2006/antonmedvedev200601242/150104737-lab-proofs-in-modern-scientific-study-facility-potable-water-quality-test-for-bacteria-design.jpg') no-repeat center center fixed;
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    # Set the title and description of the app
    st.markdown("<h1 style='color: #333; font-weight: bold;'>Water Potability Predictor</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #333; font-weight: bold;'>Enter the values for various water quality attributes to predict water potability.</p>", unsafe_allow_html=True)

    # Create input fields for the water quality attributes
    ph = st.number_input("pH", min_value=0.0, max_value=14.0, step=0.1)
    hardness = st.number_input("Hardness", min_value=0.0, step=1.0)
    solids = st.number_input("Solids", min_value=0.0, step=1.0)
    chloramines = st.number_input("Chloramines", min_value=0.0, step=1.0)
    sulfate = st.number_input("Sulfate", min_value=0.0, step=1.0)
    conductivity = st.number_input("Conductivity", min_value=0.0, step=1.0)
    organic_carbon = st.number_input("Organic Carbon", min_value=0.0, step=1.0)
    trihalomethanes = st.number_input("Trihalomethanes", min_value=0.0, step=1.0)
    turbidity = st.number_input("Turbidity", min_value=0.0, step=1.0)

    # Perform water potability prediction when the user clicks the "Predict" button
    if st.button("Predict"):
        result = predict_potability(ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity)
        if result == 1:
            st.write("The water is Potable.")
        else:
            st.write("The water is Not Potable.")

if __name__ == "__main__":
    main()
