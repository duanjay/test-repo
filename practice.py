def excel_practice():
    '''
    操作excel办公自动化
    pip install pandas
    pip install openpyxl
    '''


    import pandas as pd

    # 读入文件
    data = pd.read_excel("text.xlsx")
    # print(data)                              # 打印所有数据
    # print(data["type"])                      # 打印type列
    data["year"] = data['type'].apply(lambda x:x.split('/')[0].strip())
    data["c"] = data['type'].apply(lambda x:x.split('/')[1].strip())
    data["t"] = data['type'].apply(lambda x:x.split('/')[2].strip())
    writer = pd.ExcelWriter('temp.xlsx')            #将数据写到哪
    # data.to_excel(writer,sheet_name="原始数据")

    # 根据年限分割
    # for i in data['year'].unique():                                 # .unique  取唯一值
    #    data[data['year']== i].to_excel(writer,sheet_name = i)       
    # writer.close()

    # 根据类型分割
    # print(data[data['t'].str.contains('科幻')])                      # .contains  包含后面的值

    type_list = set(z for i in data['t'] for z in i.split(' '))
    # type_list.remove('哈哈哈')                                        # 删除元素
    for ty in type_list:
        data[data['t'].str.contains(ty)].to_excel(writer,sheet_name=ty)
    writer.close()


# def 
'''
轻松获取海量小说
'''