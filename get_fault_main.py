from get_fault_fun import get_mistake
import xlrd

mistake_type = ["框得不准", "漏标", "标签错误", "多标"]
label_dir_path = 'E:\ExpanderaAI\labeldata\\20220207_3(checkDone)\\result'
output_excel = '202202171000.xls'

mistake1, mistake2, mistake3, mistake4 = get_mistake(label_dir_path, mistake_type)

data = xlrd.open_workbook(output_excel)
table = data.sheets()[0]

print(table.name)
