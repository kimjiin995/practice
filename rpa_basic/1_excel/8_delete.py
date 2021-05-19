from openpyxl import load_workbook

wb = load_workbook("sample2.xlsx")

ws = wb.active

# ws.delete_rows(4, 2) # 3, 4번 학생 row 사라짐
# wb.save("sample2_delete_rows.xlsx")

ws.delete_cols(2, 3) # 영어, 수학 column 사라짐
wb.save("sample2_delete_cols.xlsx")