from openpyxl import load_workbook

wb = load_workbook("sample2.xlsx")
ws = wb.active

# ws.insert_rows(5, 2)
# wb.save("sample2_insert_rows.xlsx")

ws.insert_cols(2, 4)
wb.save("sample2_insert_cols.xlsx")
