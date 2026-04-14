#https://github.com/saadkhan17406-sketch/Python
print ("UIN : 251A053")
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
    'Cases': [100, 150, 120, 200, 250],
    'Deaths': [2, 5, 3, 8, 10]
}

df = pd.DataFrame(data)

df['Date'] = pd.to_datetime(df['Date'])

print("First 2 rows:\n", df.head(2))

df = df.drop_duplicates()
df = df.fillna(0)

print("\nSummary Statistics:\n", df.describe())

plt.plot(df['Date'], df['Cases'], marker='o', color='b', label='New Cases')
plt.title('COVID-19 Cases Trend')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.xticks(rotation=45)  
plt.legend()
plt.tight_layout()  
plt.show()