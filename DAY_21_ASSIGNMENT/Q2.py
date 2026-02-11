import pandas as pd
from openpyxl import load_workbook

df = pd.read_excel("sales_data.xlsx", sheet_name="2025")
df["Total"] = df["Quantity"] * df["Price"]
print(df)

df.to_excel("sales_summary.xlsx", index=False)
print("File saved successfully")

wb = load_workbook("sales_data.xlsx")
sheet = wb["2025"]
sheet["D1"] = "Total"

for row in range(2, sheet.max_row + 1):
    quantity = sheet[f"B{row}"].value
    price = sheet[f"C{row}"].value

    sheet[f"D{row}"] = quantity * price

wb.save("sales_summary.xlsx")
print("File saved successfully using OpenPyXL")