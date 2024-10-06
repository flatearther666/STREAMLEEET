import matplotlib
import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os


matplotlib.use('Agg')

# Title of the app
st.title("Group 3 Data Science Activity 3")
st.markdown('`by AGUAS, ALMANDRES, MACABALES, MACATANGAY, and PERICO`')

# Load data
df = pd.read_csv("test/Electronic_sales_Sep2023-Sep2024.csv")

# Display dataframe and its basic info in sections
st.markdown("### Dataset:")
st.write(df)
st.markdown("### Dataset :green[**(using df.describe())**]:")
st.write(df.describe())
st.markdown("### Dataset :green[**(using df.isna().sum())**]:")
st.write(df.isna().sum())

# Violin Plot
st.markdown('## :blue[**Violin Plot**] - Perico, Frederick Lemuel')
def violin_plot():
    plt.figure(figsize=(10, 6))
    sns.violinplot(x='Product Type', y='Total Price', data=df)
    plt.title('Violin Plot of Total Price by Product Type')
    st.pyplot(plt)

violin_plot()
st.write("* The white in the middle represents the median total price of each product ranging from 2000 to 4000. Take into consideration that the unit price and the quantity of every product affects the total price of every order, the smartphone had the highest total price and the headphones likely had orders only within that range.")

# Pie Chart
st.markdown('## :blue[**Pie Chart**] - Perico, Frederick Lemuel')
def pie_chart():
    df['Payment Method1'] = df['Payment Method'].replace({'Paypal': 'PayPal'})
    payment_methods = df['Payment Method1'].value_counts()

    plt.figure(figsize=(6, 6))
    plt.pie(payment_methods, labels=payment_methods.index, autopct='%1.1f%%')
    plt.title('Pie Chart of Payment Methods')
    st.pyplot(plt)

pie_chart()
st.write("* Credit Cards are the most used payment method at 29.3%, while debit is the least used at 12.4%. PayPal is the second most used payment method at 29% then the Bank transfers at 16.9%. Cash is next to Debit Cards being the least used payment method at 12.5%.")

# Scatter Plot
st.markdown('## :orange[**Scatter Plot**] - Macabales, Carl Emmanuel M.')
def scatter_plot():
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Quantity'], df['Total Price'])
    plt.title('Total Price vs Quantity')
    plt.xlabel('Quantity')
    plt.ylabel('Total Price')
    st.pyplot(plt)

scatter_plot()
st.write("* This scatter plot shows Total Price and Quantity of items purchased. Each point represents an actual transaction, so we can see how a change in quantity impacts the total price.")

# Histogram
st.markdown('## :orange[**Histogram**] - Macabales, Carl Emmanuel M.')
def histogram():
    plt.figure(figsize=(10, 6))
    plt.hist(df['Total Price'], bins=5, edgecolor='black')
    plt.title('Histogram of Total Price')
    plt.xlabel('Total Price')
    plt.ylabel('Frequency')
    st.pyplot(plt)

histogram()
st.write("* The histogram is the distribution of Total Price across all transactions. It makes clear the most commonly occurring price ranges and can be especially useful in the sense of picking out trends and concentrations that occur in the data.")

# Bubble Chart
st.markdown('## :violet[**Bubble Chart**] - Macatangay, Robin Jairic T.')
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
st.write("* From the bubble chart, we can see that there is a positive relationship between **Quantity and Total Price**. However this can vary depending on the **type of product** purchased.")
st.write("* We can also see that customers who purchase products such as **Smartphones and Laptops** are more likely to also purchase add-ons, this is shown through the **size** of the bubbles.")

# Box Plot
st.markdown('## :violet[**Box Plot**] - Macatangay, Robin Jairic T.')
def box_plot_payment_method():
    plt.figure(figsize=(10, 6))
    df['Payment Method'] = df['Payment Method'].replace({'Paypal': 'PayPal'})

    sns.boxplot(x='Payment Method', y='Total Price', data=df, hue='Payment Method')
    plt.title('Box Plot: Total Price Distribution by Payment Method')
    plt.xlabel('Payment Method')
    plt.ylabel('Total Price')
    st.pyplot(plt)

box_plot_payment_method()
st.write("* From the box plot, we can conclude that **Bank Transfer** is predominantly used for larger payments and purchases, while **Cash** is primarily utilized for lower-value transactions.")

#Bar Graph
st.markdown('## :red[**Bar Graph**] - Aguas, Ynikko Arzee Neo D.')
def bar_chart(df):
  price_type = df.groupby('Product Type')['Total Price'].mean()
  colors = ['red', 'orange', 'yellow', 'green', 'blue']

  plt.figure(figsize=(10, 6))
  price_type.plot(kind='bar', color=colors)
  plt.title('Average Price by Product Type')
  plt.xlabel('Product Type')
  plt.ylabel('Total Price')
  plt.xticks(rotation=45)
  st.pyplot(plt)

bar_chart(df)
st.write("* A function named `bar_chart` is defined in this code, and it accepts a DataFrame {df} as input. The DataFrame is grouped according to the 'Product Type' column to determine the mean total price for each type of product. Using Matplotlib, the function generates a figure with predetermined dimensions and sets a list of colors for the chart's bars. After that, it creates a bar chart showing the average costs by kind of product, labels and titles the axes appropriately, and rotates the labels on the x-axis to make them easier to read. Lastly, `plt.show()` is used to display the chart, and `bar_chart(df)} is used to invoke the function.")

#Line Graph
st.markdown("## :red[**Line Graph**] - Aguas, Ynikko Arzee Neo D.")
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
plt.clf()
plt.show()

st.write("* This code snippet handles a DataFrame df by first using `pd.to_datetime()` to convert the 'Purchase Date' column into a datetime format. The y_axis_column is then set to 'Quantity,' and the data is grouped by 'Purchase Date' with the groupby method being used to total the amounts for each date. Matplotlib is used to build a line graph that plots the grouped data's values (quantities) against its index (dates), with the line color set to red. A title, labeled axes, rotated x-axis labels for easier reading, and a grid for better presentation are added to the customized graph. Finally, `plt.show()` is used to display the graph.")


