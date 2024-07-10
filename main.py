import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
# Reading File
df = pd.read_csv('./Data/super_store.csv')
# Removing Unnecessary Columns
df.drop(columns="Postal Code", inplace=True)
# Printing Unique Values
print(df["Ship Mode"].unique())
print(df["Segment"].unique())
print(df["Country"].unique())
print(df["Category"].unique())
print(df["Sub-Category"].unique())
print(df["Region"].unique())
# Printing Descriptive Statistics
df.describe()
# Printing Information
df.info()
# Printing Missing Values
df.isna().sum()
#Analyxing Data
#Bar graph
df.groupby("Region")["Sales"].sum().plot.bar()
df.groupby("Region")["Profit"].sum().plot.bar()
df.groupby("Segment")["Sales"].sum().plot.bar()
df.groupby("Segment")["Profit"].sum().plot.bar()
df.groupby("Category")["Sales"].sum().plot.bar()
df.groupby("Category")["Profit"].sum().plot.bar()
df.groupby("State")["Sales"].sum().plot.bar()
df.groupby("State")["Profit"].sum().plot.bar()
#Analyzing Data
#Pie Chart
df.groupby("Region")["Sales"].sum().plot.pie(autopct="%1.0f%%")
df.groupby("Region")["Sales"].sum().plot.pie(autopct="%1.0f%%")
df.groupby("Segment")["Sales"].sum().plot.pie(autopct="%1.0f%%")
df.groupby("Segment")["Profit"].sum().plot.pie(autopct="%1.0f%%")
df.groupby("Category")["Sales"].sum().plot.pie(autopct="%1.0f%%")
df.groupby("Category")["Profit"].sum().plot.pie(autopct="%1.0f%%")
