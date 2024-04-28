import pandas as pd
import matplotlib.pyplot as plt

'''df = pd.read_csv('C:/Users/TEMP.NDOCY.000/Desktop/School Work/Technical Programming/football.csv.csv')
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
missing_values = df.isnull().sum()
print("Missing values: ", missing_values)
duplicate = df.duplicated().sum()
print("Number of duplicate entries: ",duplicate)
plt.show()

days = ["Mon","Tue","Wed","Thur","Fri","Sar","Sun"]
temps = [22,25,23,34,43,23,43]

plt.figure(figsize=(10,5))
plt.plot(days,temps,marker ='o',linestyle = '-',color = 'red')
plt.title('Weekly temperature Trends')
plt.xlabel('Day of the week')
plt.ylabel('Temperature(C)')
plt.grid(True)
plt.show()

df['Jersey Number'] = pd.to_numeric(df['Jersey Number'], errors = 'coerce')
df['Age'] = pd.to_numeric(df['Age'], errors = 'coerce')

plt.scatter(df['Jersey Number'],df['Age'])
plt.title('Jersey Number and Age')
plt.ylabel('Age')
plt.xlabel('Jersey Number')
plt.show()


plt.hist(df['Jersey Number'],df['Age'], bins=20, color='blue', alpha=0.7)
plt.title('Jesery Number and Age')
plt.xlabel('Jersey Number')
plt.ylabel('Age')
plt.show()

plt.bar(df['Jersey Number'],df['Age'],color ='blue',alpha = 0.7)
plt.title('Jersey Number and Age')
plt.xlabel('Jersey Nmuber')
plt.ylabel('Age')
plt.show()

plt.figure(figsize= 7.7)
plt.pie(df['Jersey Number'],df['Age'],autopct='%1.1f%%', startangle=140)
plt.title('Jersey Number and Age')
plt.show()

df['Jersey Number'] = pd.to_numeric(df['Jersey Number'], errors = 'coerce')
plt.figure(figsize=(6,6))
plt.boxplot(df['Jersey Number'],df['Age'],vert=True, patch_artist=True, meanline=True, showmeans=True)
plt.title('Jersey number and Age')
plt.ylabel('Jersey Number')
plt.grid(True)
plt.show()'''


# Load the data
df = pd.read_csv('C:/Users/TEMP.NDOCY.000/Desktop/School Work/Technical Programming/football.csv.csv')

# Basic data exploration
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
missing_values = df.isnull().sum()
print("Missing values: ", missing_values)
duplicate = df.duplicated().sum()
print("Number of duplicate entries: ", duplicate)

# Line Plot
days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sar", "Sun"]
temps = [22, 25, 23, 34, 43, 23, 43]
plt.figure(figsize=(10.5, 5))
plt.plot(days, temps, marker='o', linestyle='-', color='red')
plt.title('Weekly Temperature Trends')
plt.xlabel('Day of the week')
plt.ylabel('Temperature(C)')
plt.grid(True)
plt.show()

# Scatter Plot
df['Jersey Number'] = pd.to_numeric(df['Jersey Number'], errors='coerce')
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
plt.scatter(df['Jersey Number'], df['Age'])
plt.title('Jersey Number and Age')
plt.ylabel('Age')
plt.xlabel('Jersey Number')
plt.show()

# Histogram
plt.hist(df['Jersey Number'], bins=20, color='blue', alpha=0.7)
plt.title('Jesery Number Distribution')
plt.xlabel('Jersey Number')
plt.ylabel('Frequency')
plt.show()

# Bar Plot
plt.bar(df['Jersey Number'], df['Age'], color='blue', alpha=0.7)
plt.title('Jersey Number and Age')
plt.xlabel('Jersey Number')
plt.ylabel('Age')
plt.show()

# Pie Chart
plt.figure(figsize=(7, 7))
plt.pie(df['Jersey Number'].value_counts(), labels=df['Jersey Number'].value_counts().index, autopct='%1.1f%%', startangle=140)
plt.title('Jersey Number Distribution')
plt.show()

# Box Plot
plt.figure(figsize=(6, 8))
plt.boxplot(df['Jersey Number'], vert=False, patch_artist=True, meanline=True, showmeans=True)
plt.title('Jersey Number Distribution')
plt.xlabel('Jersey Number')
plt.grid(True)
plt.show()


