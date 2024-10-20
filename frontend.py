import streamlit as st
import requests
import pandas as pd
import io

# Set the page configuration with a star emoji as the favicon
st.set_page_config(
    page_title="Star Data Prediction App",
    page_icon="⭐",  # Star emoji
)

# Add custom CSS to set the background image and footer style
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://i.pinimg.com/control/564x/c9/ed/af/c9edaf9a6b8b69c29631e02a8ba799f6.jpg');  
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: black;
        color: white;
        text-align: center;
        padding: 10px;
        z-index: 1000;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# FastAPI server URL
BASE_URL = "https://star-size-predictor-ne93.onrender.com/"  # Update with your FastAPI server URL if needed

# Streamlit app title
st.title("Star Data Prediction App")

# Step 1: Input number of stars
num_stars = st.number_input("Enter the number of stars:", min_value=1, value=10)

# Initialize session state variables if they don't exist
if 'generated_df' not in st.session_state:
    st.session_state.generated_df = None
if 'predicted_df' not in st.session_state:
    st.session_state.predicted_df = None
if 'plot_image' not in st.session_state:
    st.session_state.plot_image = None

# Step 2: Button to generate dataset and make predictions
if st.button("Generate Dataset and Make Predictions"):
    # Generate data
    generate_response = requests.post(f"{BASE_URL}/generate_data/", params={"num_stars": num_stars})
    
    if generate_response.status_code == 200:
        generated_csv = generate_response.content
        generated_df = pd.read_csv(io.BytesIO(generated_csv))
        
        # Store generated DataFrame in session state
        st.session_state.generated_df = generated_df

        # Step 3: Make predictions
        predict_response = requests.post(f"{BASE_URL}/predict/", files={"file": ("generated_data.csv", generated_csv)})
        
        if predict_response.status_code == 200:
            predicted_csv = predict_response.content
            predicted_df = pd.read_csv(io.BytesIO(predicted_csv))
            
            # Store predicted DataFrame in session state
            st.session_state.predicted_df = predicted_df

# Display generated and predicted datasets if they exist
if st.session_state.generated_df is not None:
    st.subheader("Generated Dataset")
    st.dataframe(st.session_state.generated_df)

if st.session_state.predicted_df is not None:
    st.subheader("Predicted Dataset")
    st.dataframe(st.session_state.predicted_df)

# Display the "Plot Regression Line" button only if both datasets are available
if st.session_state.generated_df is not None and st.session_state.predicted_df is not None:
    if st.button("Plot Regression Line"):
        # Use the predicted CSV for plotting
        plot_response = requests.post(f"{BASE_URL}/plot/", files={"file": ("predicted_data.csv", st.session_state.predicted_df.to_csv(index=False).encode('utf-8'))})

        if plot_response.status_code == 200:
            # Store plot image in session state
            st.session_state.plot_image = plot_response.content
        else:
            st.error("Failed to generate the plot.")

# Display the plot if it exists
if st.session_state.plot_image is not None:
    st.image(st.session_state.plot_image, caption="Regression Line Plot")

# Footer
st.markdown(
    """
    <div class="footer">
        <p>This project is developed by <b>Aalaap Seshanand</b> as part of ML4A Training Program at Spartifical</p>
    </div>
    """,
    unsafe_allow_html=True
)
