import os
import glob
import pandas as pd

paths = []
for root, dirs, files in os.walk("E:/Prayog_IITB"):
    for file in files:
        if file.endswith(".xlsx"):
             print(os.path.join(root, file))
             s = os.path.join(root, file)
             print(s)
             paths.append(s)

all_data = pd.DataFrame()

for f in paths:
    # df = pd.read_excel(f)
    df = pd.concat(pd.read_excel(f, sheet_name=None), ignore_index=True, sort=False)
    all_data = all_data.append(df,ignore_index=True)

print('Final Excel sheet now generated at the same location:')
all_data.to_excel("E:/Prayog_IITB/mergedbro.xlsx", index=False)

