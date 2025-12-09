import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# Load data
@st.cache_data
def load_data():
    df = pd.read_pickle(r"data\cleaned_data.pkl")
    return df


df = load_data()

# Page configuration
st.set_page_config(page_title="Tiger Auto - Car Price Estimator 🐅🚗", layout="wide")
st.title("Tiger Auto - Car Price Estimator 🐅🚗")


# Filters
## Sidebar filters
st.sidebar.header("Filter Cars")

## Car Make filter
all_makes = sorted(df["Make"].dropna().unique())
selected_makes = st.sidebar.multiselect("Select Car Make(s)", all_makes, default=all_makes)

## Filter DataFrame by selected makes
filtered_df = df[df["Make"].isin(selected_makes)]

## Car Model filter (cascading)
all_models = sorted(filtered_df["Model"].dropna().unique())
selected_models = st.sidebar.multiselect("Select Car Model(s)", all_models, default=all_models)
filtered_df = filtered_df[filtered_df["Model"].isin(selected_models)]

## Transmission Type filter
all_transmissions = sorted(filtered_df["Transmission Type"].dropna().unique())
selected_transmissions = st.sidebar.multiselect(
    "Select Transmission Type(s)", all_transmissions, default=all_transmissions
)
filtered_df = filtered_df[filtered_df["Transmission Type"].isin(selected_transmissions)]

## Engine Fuel Type filter
all_fuels = sorted(filtered_df["Engine Fuel Type"].dropna().unique())
selected_fuels = st.sidebar.multiselect("Select Engine Fuel Type(s)", all_fuels, default=all_fuels)
filtered_df = filtered_df[filtered_df["Engine Fuel Type"].isin(selected_fuels)]

## Year filter
min_year, max_year = int(filtered_df["Year"].min()), int(filtered_df["Year"].max())
year_range = st.sidebar.slider("Select Year Range", min_year, max_year, (min_year, max_year))
filtered_df = filtered_df[
    (filtered_df["Year"] >= year_range[0]) & (filtered_df["Year"] <= year_range[1])
]


# 1 Filtered Cars Table
st.subheader("Filtered Cars")
st.dataframe(filtered_df.reset_index(drop=True))


# 2 Popularity by Car Brand
st.subheader("Popularity Score by Car Brand")
pop_data = (
    filtered_df.groupby("Make")["Popularity"].mean().sort_values(ascending=False).reset_index()
)
pop_order = pop_data["Make"]
plt.figure(figsize=(12, 8))  # Widened bars
sns.barplot(
    x="Popularity",
    y="Make",
    data=pop_data,
    palette=sns.color_palette("viridis", len(pop_data)),
    order=pop_order,
)
plt.title("Popularity Score by Car Brand")
plt.xlabel("Popularity Score")
plt.ylabel("Car Brand")
st.pyplot(plt.gcf())
plt.clf()


# 3 MSRP Distribution
st.subheader("MSRP Distribution")
plt.figure(figsize=(12, 6))
msrp_filtered = filtered_df[filtered_df["MSRP"] <= 100000]["MSRP"]
sns.histplot(msrp_filtered, bins=15, kde=False)
plt.xlim(0, 100000)
ticks = np.linspace(0, 100000, 15, dtype=int)
plt.xticks(ticks, [f"${int(t / 1000)}k" for t in ticks], rotation=45)
plt.title("MSRP Distribution")
plt.xlabel("Price (USD)")
plt.ylabel("Count")
st.pyplot(plt.gcf())
plt.clf()


# 4 Price Ranges by Market Category
st.subheader("Price Ranges by Market Category")
cat_clean = filtered_df.copy()
cat_exploded = cat_clean.explode("Market Category")
cat_exploded = cat_exploded[cat_exploded["Market Category"].notna()]

sorted_order = (
    cat_exploded.groupby("Market Category")["MSRP"].median().sort_values(ascending=False).index
)

plt.figure(figsize=(12, 8))
sns.boxplot(
    x="MSRP",
    y="Market Category",
    data=cat_exploded,
    order=sorted_order,
    showfliers=False,
    palette="magma",
)
plt.title("Price Ranges by Market Category")
plt.xlabel("Price (USD)")
plt.ylabel("Market Category")
st.pyplot(plt.gcf())
plt.clf()


# 5Summary Statistics
st.subheader("Summary Statistics for Filtered Cars")
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Number of Cars", len(filtered_df))
col2.metric("Average MSRP", f"${filtered_df['MSRP'].mean():,.0f}")
col3.metric("Average Engine HP", f"{filtered_df['Engine HP'].mean():.1f}")
col4.metric("Average City MPG", f"{filtered_df['city mpg'].mean():.1f}")
col5.metric("Average Highway MPG", f"{filtered_df['highway MPG'].mean():.1f}")


# Top cars by Popularity or Price
st.subheader("Top Cars by Popularity or Price")
top_n = st.slider("Select top N cars", 5, 20, 10)
sort_option = st.radio("Sort by:", ["Popularity", "MSRP"])
top_cars = filtered_df.sort_values(by=sort_option, ascending=False).head(top_n)
st.dataframe(
    top_cars[["Make", "Model", "Year", "MSRP", "Engine HP", "Popularity"]].reset_index(drop=True)
)
