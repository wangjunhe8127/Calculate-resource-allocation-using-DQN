import numpy as np
import xlrd
people_num = 5
delta_t = 0.5
# 导入excel文件
def load_execl(file_name, sheet_num = 1):
    workBook = xlrd.open_workbook(file_name)
    res = []
    for i in range(sheet_num):
        sheet = workBook.sheet_by_index(i)
        res.append(sheet.col_values(1)[1:])
    return res
def resolution(num):
    res={
        0:[0,0,0,0,0],
        1:[0,0,0,0,1],
        2:[0,0,0,1,0],
        3:[0,0,0,1,1],
        4:[0,0,1,0,0],
        5:[0,0,1,0,1],
        6:[0,0,1,1,0],
        7:[0,0,1,1,1],
        8:[0,1,0,0,0],
        9:[0,1,0,0,1],
        10:[0,1,0,1,0],
        11:[0,1,0,1,1],
        12:[0,1,1,0,0],
        13:[0,1,1,0,1],
        14:[0,1,1,1,0],
        15:[0,1,1,1,1],
        16:[1,0,0,0,0],
        17:[1,0,0,0,1],
        18:[1,0,0,1,0],
        19:[1,0,0,1,1],
        20:[1,0,1,0,0],
        21:[1,0,1,0,1],
        22:[1,0,1,1,0],
        23:[1,0,1,1,1],
        24:[1,1,0,0,0],
        25:[1,1,0,0,1],
        26:[1,1,0,1,0],
        27:[1,1,0,1,1],
        28:[1,1,1,0,0],
        29:[1,1,1,0,1],
        30:[1,1,1,1,0],
        31:[1,1,1,1,1],
    }
    tmp = res[num]
    data = np.array(tmp).reshape(people_num, 1)
    return data
# 测试
if __name__ == '__main__':
    a = load_execl('source/Init_Temperature.xlsx')