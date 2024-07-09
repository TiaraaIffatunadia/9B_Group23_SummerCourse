import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data
df = pd.read_excel('Data_Timbulan_Sampah_SIPSN_KLHK_2020.xlsx', header=1)

# Filter data for the year 2020
df_2020 = df[df['Tahun'] == 2020]

# Calculate total annual waste generation for each province
total_annual_waste = df_2020.groupby('Provinsi')['Timbulan Sampah Tahunan(ton)'].sum().reset_index()

# Calculate average annual waste generation for each province
average_annual_waste = df_2020.groupby('Provinsi')['Timbulan Sampah Tahunan(ton)'].mean().reset_index()

# Find the province producing the most and least waste in 2020
most_waste_province = total_annual_waste.loc[total_annual_waste['Timbulan Sampah Tahunan(ton)'].idxmax()]
least_waste_province = total_annual_waste.loc[total_annual_waste['Timbulan Sampah Tahunan(ton)'].idxmin()]

# Categorize provinces based on average annual waste generation
average_annual_waste['Category'] = pd.cut(
    average_annual_waste['Timbulan Sampah Tahunan(ton)'],
    bins=[-float('inf'), 100000, 700000, float('inf')],
    labels=['GREEN', 'ORANGE', 'RED']
)

# Print the results
print("Total Annual Waste Generation in 2020:")
print(total_annual_waste)

print("Average Annual Waste Generation in 2020:")
print(average_annual_waste)

print("Province Producing Most Waste in 2020:")
print(most_waste_province)

print("Province Producing Least Waste in 2020:")
print(least_waste_province)

# Total Annual Waste Generation Plot for 2020
plt.figure(figsize=(10, 6))
colors = plt.cm.viridis(np.linspace(0, 1, len(total_annual_waste)))
plt.bar(total_annual_waste['Provinsi'], total_annual_waste['Timbulan Sampah Tahunan(ton)'], color=colors)
plt.xlabel('Province')
plt.ylabel('Total Annual Waste Generation (tons)')
plt.title('Total Annual Waste Generation by Province in 2020')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('static/total_annual_waste.png')
plt.show()

# Average Annual Waste Generation Plot for 2020
plt.figure(figsize=(10, 6))
colors = plt.cm.plasma(np.linspace(0, 1, len(average_annual_waste)))
plt.bar(average_annual_waste['Provinsi'], average_annual_waste['Timbulan Sampah Tahunan(ton)'], color=colors)
plt.xlabel('Province')
plt.ylabel('Average Annual Waste Generation (tons)')
plt.title('Average Annual Waste Generation by Province in 2020')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('static/average_annual_waste.png')
plt.show()

# Categorization Plot for 2020
plt.figure(figsize=(10, 6))
colors = {'GREEN': 'green', 'ORANGE': 'orange', 'RED': 'red'}
plt.bar(average_annual_waste['Provinsi'], average_annual_waste['Timbulan Sampah Tahunan(ton)'], color=average_annual_waste['Category'].map(colors))
plt.xlabel('Province')
plt.ylabel('Average Annual Waste Generation (tons)')
plt.title('Categorization of Average Annual Waste Generation by Province in 2020')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('static/categorized_annual_waste.png')
plt.show()

print(f"Province Producing Most Waste in 2020: {most_waste_province['Provinsi']} with {most_waste_province['Timbulan Sampah Tahunan(ton)']} tons")
print(f"Province Producing Least Waste in 2020: {least_waste_province['Provinsi']} with {least_waste_province['Timbulan Sampah Tahunan(ton)']} tons")

# Flask App Code
from flask import Flask, render_template
import io
import base64

app = Flask(__name__)

# def load_data():
#     df = pd.read_csv('Data_Timbulan_Sampah_SIPSN_KLHK_Aceh_2020.csv')
#     return df

# def create_plots():
#     df = load_data()

#     # Calculate average annual waste generation for each province
#     average_annual_waste_all_years = df.groupby('Provinsi')['Timbulan Sampah Tahunan(ton)'].mean().reset_index()
    
#     # Categorize provinces based on average annual waste generation
#     average_annual_waste_all_years['Category'] = pd.cut(
#         average_annual_waste_all_years['Timbulan Sampah Tahunan(ton)'],
#         bins=[-float('inf'), 100000, 700000, float('inf')],
#         labels=['GREEN', 'ORANGE', 'RED']
#     )
    
    # Count the number of provinces in each category
    # category_counts = average_annual_waste_all_years['Category'].value_counts().sort_index()
    
    # # Create the bar plot for category counts
    # plt.figure(figsize=(10, 6))
    # plt.bar(category_counts.index, category_counts.values, color=['green', 'orange', 'red'])
    # plt.xlabel('Category')
    # plt.ylabel('Number of Provinces')
    # plt.title('Number of Provinces by Average Waste Generation Category (2018-2023)')
    # plt.tight_layout()
    # plt.savefig('static/category_counts.png')
    # plt.close()

    # # Line graph for total annual waste generation
    # total_annual_waste_all_years = df.groupby(['Tahun', 'Provinsi'])['Timbulan Sampah Tahunan(ton)'].sum().unstack()
    # plt.figure(figsize=(14, 8))
    # for province in total_annual_waste_all_years.columns:
    #     plt.plot(total_annual_waste_all_years.index, total_annual_waste_all_years[province], marker='o', label=province)
    # plt.xlabel('Year')
    # plt.ylabel('Total Annual Waste Generation (tons)')
    # plt.title('Total Annual Waste Generation by Province (2018-2023)')
    # plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    # plt.tight_layout()
    # plt.savefig('static/total_annual_waste_all_years.png')
    # plt.close()

    # # Data for 2020
    # df_2020 = df[df['Tahun'] == 2020]
    # total_annual_waste = df_2020.groupby('Provinsi')['Timbulan Sampah Tahunan(ton)'].sum().reset_index()
    # average_annual_waste = df_2020.groupby('Provinsi')['Timbulan Sampah Tahunan(ton)'].mean().reset_index()

    # most_waste_province = total_annual_waste.loc[total_annual_waste['Timbulan Sampah Tahunan(ton)'].idxmax()]
    # least_waste_province = total_annual_waste.loc[total_annual_waste['Timbulan Sampah Tahunan(ton)'].idxmin()]

    # average_annual_waste['Category'] = pd.cut(
    #     average_annual_waste['Timbulan Sampah Tahunan(ton)'],
    #     bins=[-float('inf'), 100000, 700000, float('inf')],
    #     labels=['GREEN', 'ORANGE', 'RED']
    # )

    # # Total Annual Waste Generation Plot for 2020
    # plt.figure(figsize=(10, 6))
    # colors = plt.cm.viridis(np.linspace(0, 1, len(total_annual_waste)))
    # plt.bar(total_annual_waste['Provinsi'], total_annual_waste['Timbulan Sampah Tahunan(ton)'], color=colors)
    # plt.xlabel('Province')
    # plt.ylabel('Total Annual Waste Generation (tons)')
    # plt.title('Total Annual Waste Generation by Province in 2020')
    # plt.xticks(rotation=90)
    # plt.tight_layout()
    # plt.savefig('static/total_annual_waste.png')
    # plt.close()

    # # Average Annual Waste Generation Plot for 2020
    # plt.figure(figsize=(10, 6))
    # colors = plt.cm.plasma(np.linspace(0, 1, len(average_annual_waste)))
    # plt.bar(average_annual_waste['Provinsi'], average_annual_waste['Timbulan Sampah Tahunan(ton)'], color=colors)
    # plt.xlabel('Province')
    # plt.ylabel('Average Annual Waste Generation (tons)')
    # plt.title('Average Annual Waste Generation by Province in 2020')
    # plt.xticks(rotation=90)
    # plt.tight_layout()
    # plt.savefig('static/average_annual_waste.png')
    # plt.close()

    # # Categorization Plot for 2020
    # plt.figure(figsize=(10, 6))
    # colors = {'GREEN': 'green', 'ORANGE': 'orange', 'RED': 'red'}
    # plt.bar(average_annual_waste['Provinsi'], average_annual_waste['Timbulan Sampah Tahunan(ton)'], color=average_annual_waste['Category'].map(colors))
    # plt.xlabel('Province')
    # plt.ylabel('Average Annual Waste Generation (tons)')
    # plt.title('Categorization of Average Annual Waste Generation by Province in 2020')
    # plt.xticks(rotation=90)
    # plt.tight_layout()
    # plt.savefig('static/categorized_annual_waste.png')
    # plt.close()

@app.route('/')
def index():
    return render_template('index.html', 
                           most_waste_province=most_waste_province, 
                           least_waste_province=least_waste_province)

if __name__ == '__main__':
    app.run(debug=True)
