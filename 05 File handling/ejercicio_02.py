# EXCEL SHEET - PANDAS

import pandas as pd

file = pd.ExcelFile('files/Sales.xlsx')
#print(file.sheet_names)
sheet = file.parse('sales')
#print(sheet)
#print(sheet.Date)
sheet.Amount.sum()
sheet.loc[0]
#print(sheet.loc[0, "Amount"])
sheet.set_index('Customer', inplace=True)
#print(sheet.loc["MMC Inc."])
sheet = sheet.reset_index()
#print(sheet.loc[sheet['Invoice'] == 99])
#print(sheet.loc[sheet['Amount'] > 1800]['Customer'].unique()[0])

for customer in sheet.loc[sheet["Amount"] > 1800]['Customer'].unique():
    print(customer)