# Predicting Star Sizes with Artificial Intelligence

This web application (https://aistarsizepredictor.streamlit.app/) allows the user to do the following:
1. Generate a synthetic dataset of 'n' number of stars as input.
2. This synthetic dataset will automatically account for the brightness of stars and their respective sizes.
3. The program then uses Artificial Intelligence (specifically, linear regression) to predict the star sizes using the brightness value of the stars.
4. Following this, there is a feature to generate the plot of the predictions in order to tally how well the model performed on this unseen dataset.

## Reasons for using synthetic datasets
1. The purpose of this project is to gain a practical understanding of linear regression using gradient descent.
2. We created a dataset by applying noise to a true output equation, facilitating prediction equation generation.
3. This process demonstrates how gradient descent optimizes weights (coefficients) and bias (intercept).
4. The optimized values of weight and bias are then utilized in a web application.
5. Acts as a bridge or step up to future projects that will involve real astronomical datasets.


# Installation

This project is a Streamlit application for generating and predicting star data using a FastAPI backend.

## Prerequisites

Make sure you have the following installed:

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. **Clone the Repository**:

   Open your terminal and clone the repository:

   ```bash
   git clone https://github.com/yourusername/star-data-prediction-app.git
   cd star-data-prediction-app

2. **Install dependencies**:
   Create a virtual environment (optional but recommended) and install the required packages:

    For windows

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```
    For linux or Mac
   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment:
   For windows
   ```bash
   venv\Scripts\activate
   ```
   For linux or Mac
   ```bash
   source venv/bin/activate
   ```
   
4. Install the requirements:
   For windows
   ```bash
   python -m pip install -r requirements.txt
   ```
   For linux or Mac
   ```bash
   pip install -r requirements.txt
   ```
   
5. Run the backend powered by FastAPI using Uvicorn:
   ```bash
   uvicorn main:app
   ```

6. Run the frontend powered by Streamlit:
   ```bash
   streamlit run frontend.py
   ```



# Tools Used In This Project:
1. FastAPI - To build the API endpoints
2. Streamlit - To build and host the frontend of the web application
3. Render - To host the backend API built using FastAPI
4. NumPy - To create the synthetic dataset for training, validation, testing, and the web application
5. Matplotlib - To visualize the cost vs iterations and in the web application to visualize the regression line
6. Pandas - To read CSV files, create the dataframe, and save dataframes back to CSV

# Acknowledgements
Special thanks to the authors of the libraries used in this project.

# Contact
For questions or support, please reach out to aalaapsesh@gmail.com



   



