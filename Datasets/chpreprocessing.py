import pandas
import matplotlib.pyplot as plt
import seaborn as sns

# This is the Clonal Hematopoesis Dataset–there are 1416

x = pandas.read_csv('msk_ch_2020/data_clinical_sample.txt', delimiter='\t', low_memory=False, skiprows=4, index_col='SAMPLE_ID')
# print(x)
x2 = x.loc[x['ONCOTREE_CODE'] == 'IPMN']

# print(x2)
# print(x2[['TMB_NONSYNONYMOUS']].value_counts().to_dict())

directory = x2[['PATIENT_ID']]
# print(directory.to_dict()) # Lookup of patient_id by sample_id

# Now will gather information about mutations

df = pandas.read_csv('msk_ch_2020/data_mutations.txt', low_memory=False, delimiter='\t', skiprows=2)
print(df)
print(df.columns)

# df2 = df.loc[df['Tumor_Sample_Barcode'] in directory]
# print(df2)

print(directory)
values_to_match = {"Tumor_Sample_Barcode": directory.index.to_list()}
print(values_to_match)

mask = pandas.concat([df[col].isin(values) for col, values in values_to_match.items()], axis=1).all(axis=1)
filtered_df = df[mask]

print(filtered_df[['Tumor_Sample_Barcode', 'Codons', 'Hugo_Symbol']])
print(filtered_df[['Hugo_Symbol']].value_counts())

di = filtered_df['Hugo_Symbol'].value_counts().to_dict()
print(di)
# Get the Keys and store them in a list
labels = list(di.keys())

# Get the Values and store them in a list
values = list(di.values())

plt.pie(values, labels=labels)
plt.show()

d2 = { k: v for k, v in di.items() if v >= 5 }
print(d2)
print(len(d2))
print(list(d2.keys()))