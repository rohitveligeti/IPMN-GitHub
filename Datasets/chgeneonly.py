import pandas
import matplotlib.pyplot as plt
import seaborn as sns
from referencegenes import *
from collections import Counter
from sklearn import datasets, manifold
import numpy
# This is the Clonal Hematopoesis Dataset–there are 1416
print(ipmn_genes)

x = pandas.read_csv('msk_ch_2020/data_clinical_sample.txt', delimiter='\t', low_memory=False, skiprows=4, index_col='SAMPLE_ID')
# print(x)
x2 = x.loc[x['ONCOTREE_CODE'] == 'IPMN']

# print(x2)
# print(x2[['TMB_NONSYNONYMOUS']].value_counts().to_dict())

directory = x2[['PATIENT_ID']]
# print(directory.to_dict()) # Lookup of patient_id by sample_id
ipmn_samples = directory.index.values.tolist()

# Now will gather information about mutations

df = pandas.read_csv('msk_ch_2020/data_mutations.txt', low_memory=False, delimiter='\t', skiprows=2)
print(df)
print(df.columns)

df2 = df[['Hugo_Symbol', 'Tumor_Sample_Barcode']]
print(df2)

mask = df2['Tumor_Sample_Barcode'].isin(ipmn_samples)
df3 = df2[mask]
print(df3)

mask = df3['Hugo_Symbol'].isin(ipmn_genes)
df4 = df3[mask]
print(df4)


new_values = {}

for x in ipmn_samples:
    new_values[x] = []

print(new_values)

for index, row in df4.iterrows():

    new_values[row['Tumor_Sample_Barcode']].append(row['Hugo_Symbol'])

print(new_values)

lll = []
for r in new_values.values():
    lll.append(len(r))

xxx = Counter(lll)
print(xxx)

nndict = {}
for i in ipmn_genes:
    nndict[i] = 0

print(nndict)

masterlist = []

for key, value in new_values.items():
    nxdict = nndict.copy()
    for v in value:
        nxdict[v] += 1
    masterlist.append(list(nxdict.values()))

X = numpy.array(masterlist)

print(X)

# We want to get TSNE embedding with 2 dimensions
n_components = 2
tsne = manifold.TSNE(n_components)
tsne_result = tsne.fit_transform(X)
# (1000, 2)
# Two dimensions for each of our images
 
# Plot the result of our TSNE with the label color coded
# A lot of the stuff here is about making the plot look pretty and not TSNE
tsne_result_df = pandas.DataFrame({'tsne_1': tsne_result[:,0], 'tsne_2': tsne_result[:,1]})
fig, ax = plt.subplots(1)
sns.scatterplot(x='tsne_1', y='tsne_2', data=tsne_result_df, ax=ax,s=120)
lim = (tsne_result.min()-5, tsne_result.max()+5)
ax.set_xlim(lim)
ax.set_ylim(lim)
ax.set_aspect('equal')
ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.0)

plt.show()