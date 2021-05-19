from openpyxl import load_workbook

wb = load_workbook("sample_formula.xlsx", data_only=True) #
ws = wb.active

# none이 나오는 이유는 evaluate 되지 않았기 때문에
for row in ws.values:
    for cell in row:
        print(cell)