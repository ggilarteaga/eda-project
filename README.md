# EDA Project

This repository contains the final project for INSY6500-Modern Tools for Data Analytics and Modeling. The project requires to work with a real-world data set with over 5000 observations and 10 features.
The data set for this project has been obtained from: https://www.kaggle.com/datasets/CooperUnion/cardataset/data
The data set includes car features such as make, model, year, engine type, mileage, price, etc.

The project structure is as follows:

Part 1: The initial part of the project focuses on the first three steps of the EDA workflow outlined in lecture 13a, which include:
	1. Load & Initial Reconnaissance
	2. Data Quality Assessment
	3. Cleaning Decisions
This part is developed in the cleaning notebook 'data_cleaning.ipynb'. Here the data is loaded, understood, explored and cleaned.


Part 2:The second part of the project deals with data exploration and modeling. This part focuses on steps 4 and 5 of the EDA workflow outlined in lecture 13a:
	4. Statistical EDA
	5. Transformation
This part is developed in the exploration notebook, named 'EDA.ipynb'. Here the data is processed to derive conclusions and answer questions.


Part 3: Streamlit is used to create interactive dashboards that enable the user to work with the data. The idea of using streamlit is to create a price estimation tool that uses the data and teh filters applied by the user to deliver information to the user in a nicely displayed attractive format.
This work is developed in the file named app.py

There is a folder named data that stores the data used in this project. It stores two files: 'data.csv', which contains the raw data and cleaned_data.pkl, which contained the data set with cleaned and processed data.


The tools used for this project include:
- python 3.10
- jupyter lab
- Pandas
- Numpy
- matplotlib and seaborn
- streamlit


How to use the stramlit dashboard:
1. Open the dashboard with streamlit by running this line in your terminal: streamlit run app.py
2. Use the filters and sidebars to filter cars based on your preferences
3. The dashboards and tables will update dynamically based on your selections.


