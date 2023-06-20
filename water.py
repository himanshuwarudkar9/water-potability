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
            st.markdown("<p style='color: #333; font-weight: bold;'>The water is Potable.</p>", unsafe_allow_html=True)
            st.markdown("<p style='color: #333;'>This prediction is based on the model's estimation and does not guarantee 100% accuracy. It is recommended to consult with water authorities or experts for further assessment and appropriate action.</p>", unsafe_allow_html=True)
        else:
            
            st.markdown("<p style='color: #333; font-weight: bold;'>The water is Not Potable.</p>", unsafe_allow_html=True)
            
            st.markdown("<p style='color: #333; font-weight: bold;'>Non-potable water refers to water that does not meet the necessary quality standards for safe consumption. It may contain contaminants or impurities that can pose health risks if consumed. It is important to take the following safety precautions.</p>", unsafe_allow_html=True)

           
            st.markdown("<p style='color: #333; font-weight: bold;'>Avoid drinking the water directly from the source.</p>", unsafe_allow_html=True)

          
            st.markdown("<p style='color: #333; font-weight: bold;'>Do not use non-potable water for cooking, preparing food, or making ice cubes.</p>", unsafe_allow_html=True)
            st.markdown("<p style='color: #333; font-weight: bold;'>Use alternative sources of water for drinking, such as bottled water or water from a reliable and certified water treatment system.</p>", unsafe_allow_html=True)
            st.markdown("<p style='color: #333; font-weight: bold;'>Contact your local water authorities or experts for guidance on improving water quality or finding alternative sources of potable water.It is important to prioritize your health and well-being by ensuring access to clean and potable water. Taking necessary precautions and seeking expert advice will help mitigate potential health risks associated with non-potable water </p>", unsafe_allow_html=True)

            
    st.markdown("<h3 style='color: #333; font-weight: bold;'>Disclaimer:</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #333; font-weight: bold;'>This is a prediction model that provides an estimation of water potability based on the input attributes. The predictions are not guaranteed to be 100% accurate and should be used for informational purposes only. It is recommended to consult with water experts, follow local guidelines, and conduct appropriate water testing for accurate assessments of water quality and potability.</h3>", unsafe_allow_html=True)

        

            

if __name__ == "__main__":
    main()
