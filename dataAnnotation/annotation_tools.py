import glob

txt_list = txt_list = glob.glob('/home/jerry/kitti/label_2_try1/*.txt')

def orig_stat(txt_list):
    dic = {}
    for i,item in enumerate(txt_list):
        with open(item) as f:
            for line in f:
                #print(line)
                labeldata = line.strip().split(' ')
                category = labeldata[0]
                if not dic.get(category):
                    dic[category] = 0
                dic[category] +=1

    return dic

def show_category(txt_list):
    category_list = set()
    for i,item in enumerate(txt_list):
        with open(item) as tdf:
            for each_line in tdf:
                labeldata = each_line.strip().split(' ')
                category_list.add(labeldata[0])
    print(category_list)

def merge2str(data_list):
    line_str=''
    for i in range(len(data_list)):
        if i!= (len(data_list)-1):
            line_str=line_str+data_list[i]+' '
        else:
            line_str=line_str+data_list[i]
    line_str=line_str+'\n'
    return line_str

