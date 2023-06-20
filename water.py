import streamlit as st
import pickle

# Load the trained model from the pickle file
model = pickle.load(open('trained_model.pkl', 'rb'))

def predict_potability(ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity):
    # Create a dictionary with the input values
    input_data = {
        'ph': ph,
        'Hardness': hardness,
        'Solids': solids,
        'Chloramines': chloramines,
        'Sulfate': sulfate,
        'Conductivity': conductivity,
        'Organic_carbon': organic_carbon,
        'Trihalomethanes': trihalomethanes,
        'Turbidity': turbidity
    }

    # Convert the input data into a dataframe
    input_df = pd.DataFrame([input_data])

    # Make predictions using the trained model
    predictions = model.predict(input_df)

    return predictions[0]

def main():
    # Set the title and description of the app
    st.title("Water Potability Predictor")
    st.write("Enter the values for various water quality attributes to predict water potability.")

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

