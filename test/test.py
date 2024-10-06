import matplotlib
import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os


matplotlib.use('Agg')

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #f0f2f6;
        }
        .stApp {
            background-color: #f0f2f6;
        }
        .main-title {
            font-family: 'Arial', sans-serif;
            font-size: 32px;
            font-weight: bold;
            color: #4B89DC;
        }
        .plot-section {
            border: 2px solid #4B89DC;
            border-radius: 15px;
            padding: 20px;
            margin: 20px 0;
            background-color: white;
        }
        .plot-section h2 {
            font-size: 22px;
            color: #2A3F54;
            text-align: center;
        }
        .plot-section h2::after {
            content: '';
            display: block;
            width: 50px;
            height: 2px;
            background-color: #4B89DC;
            margin: 10px auto 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Title of the app
st.markdown('<div class="main-title">Group 3 Data Science Activity Part 3</div>', unsafe_allow_html=True)

# Load data
df = pd.read_csv("test/Electronic_sales_Sep2023-Sep2024.csv")

# Display dataframe and its basic info in sections
st.markdown('<div class="plot-section">', unsafe_allow_html=True)
st.write(df)
st.write(df.info())
st.write(df.describe())
st.write("Missing values per column:")
st.write(df.isna().sum())
st.markdown('</div>', unsafe_allow_html=True)

# Violin Plot
st.markdown('<div class="plot-section"><h2>Violin Plot - Perico, Frederick Lemuel</h2>', unsafe_allow_html=True)
def violin_plot():
    plt.figure(figsize=(10, 6))
    sns.violinplot(x='Product Type', y='Total Price', data=df)
    plt.title('Violin Plot of Total Price by Product Type')
    st.pyplot(plt)

violin_plot()
st.markdown('</div>', unsafe_allow_html=True)

# Pie Chart
st.markdown('<div class="plot-section"><h2>Pie Chart - Perico, Frederick Lemuel</h2>', unsafe_allow_html=True)
def pie_chart():
    df['Payment Method1'] = df['Payment Method'].replace({'Paypal': 'PayPal'})
    payment_methods = df['Payment Method1'].value_counts()

    plt.figure(figsize=(6, 6))
    plt.pie(payment_methods, labels=payment_methods.index, autopct='%1.1f%%')
    plt.title('Pie Chart of Payment Methods')
    st.pyplot(plt)

pie_chart()
st.markdown('</div>', unsafe_allow_html=True)

# Scatter Plot
st.markdown('<div class="plot-section"><h2>Scatter Plot - Macabales, Carl Emmanuel M.</h2>', unsafe_allow_html=True)
def scatter_plot():
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Quantity'], df['Total Price'])
    plt.title('Total Price vs Quantity')
    plt.xlabel('Quantity')
    plt.ylabel('Total Price')
    st.pyplot(plt)

scatter_plot()
st.markdown('</div>', unsafe_allow_html=True)

# Histogram
st.markdown('<div class="plot-section"><h2>Histogram - Macabales, Carl Emmanuel M.</h2>', unsafe_allow_html=True)
def histogram():
    plt.figure(figsize=(10, 6))
    plt.hist(df['Total Price'], bins=5, edgecolor='black')
    plt.title('Histogram of Total Price')
    plt.xlabel('Total Price')
    plt.ylabel('Frequency')
    st.pyplot(plt)

histogram()
st.markdown('</div>', unsafe_allow_html=True)

# Bubble Chart
st.markdown('<div class="plot-section"><h2>Bubble Chart - Macatangay, Robin Jairic T.</h2>', unsafe_allow_html=True)
def bubble_chart():
    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        x='Total Price',
        y='Quantity',
        size='Add-on Total',
        hue='Product Type',
        sizes=(50, 300),
        alpha=0.5,
        data=df
    )
    plt.title('Bubble Chart: Total Price vs Quantity (Bubble Size: Add-on Total)')
    plt.xlabel('Total Price')
    plt.ylabel('Quantity')
    plt.legend(title='Product Type', bbox_to_anchor=(1.05, 1), loc='upper left')
    st.pyplot(plt)

bubble_chart()
st.markdown('</div>', unsafe_allow_html=True)

# Box Plot
st.markdown('<div class="plot-section"><h2>Box Plot - Macatangay, Robin Jairic T.</h2>', unsafe_allow_html=True)
def box_plot_payment_method():
    plt.figure(figsize=(10, 6))
    df['Payment Method'] = df['Payment Method'].replace({'Paypal': 'PayPal'})

    sns.boxplot(x='Payment Method', y='Total Price', data=df, hue='Payment Method')
    plt.title('Box Plot: Total Price Distribution by Payment Method')
    plt.xlabel('Payment Method')
    plt.ylabel('Total Price')
    st.pyplot(plt)

box_plot_payment_method()
st.markdown('</div>', unsafe_allow_html=True)

#Bar Graph
st.markdown('<div class="plot-section"><h2>Bar Graph - Aguas, Ynikko Arzee Neo D.</h2>', unsafe_allow_html=True)
def bar_chart():
  price_type = df.groupby('Product Type')['Total Price'].mean()
  colors = ['red', 'orange', 'yellow', 'green', 'blue']

  plt.figure(figsize=(10, 6))
  price_type.plot(kind='bar', color=colors)
  plt.title('Average Price by Product Type')
  plt.xlabel('Product Type')
  plt.ylabel('Total Price')
  plt.xticks(rotation=45)
  st.pyplot(plt)

bar_chart()
st.markdown('</div>', unsafe_allow_html=True)

#Line Graph
st.markdown('<div class="plot-section"><h2>Line Graph - Aguas, Ynikko Arzee Neo D.</h2>', unsafe_allow_html=True)
df ['Purchase Date'] = pd.to_datetime(df['Purchase Date'])


y_axis_column = 'Quantity'


grouped_data = df.groupby('Purchase Date')[y_axis_column].sum()  


plt.plot(grouped_data.index, grouped_data.values, color='red')


plt.title(f'{y_axis_column} Over Time')
plt.xlabel('Purchase Date')
plt.ylabel(y_axis_column)
plt.xticks(rotation=45)
plt.grid(True) 


st.pyplot(plt)
st.markdown('</div>', unsafe_allow_html=True)


