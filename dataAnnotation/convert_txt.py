import os
import glob
import config.config_param as cfg
from dataAnnotation.annotation_tools import show_category, orig_stat

# The goal in the object detection task is to train object detectors for the classes 'Car', 'Pedestrian', and 'Cyclist'
# Reference: https://github.com/bostondiditeam/kitti/tree/master/resources/devkit_object


wd = os.getcwd()

orig_txt_list_path = glob.glob('/home/jerry/kitti/label_2_orig/*.txt')
sorted_orig_txt_list = []
# {'Car': 28742, 'Van': 2914, 'Misc': 973, 'DontCare': 11295, 'Pedestrian': 4487, 'Truck': 1094, 'Cyclist': 1627,
# 'Person_sitting': 222, 'Tram': 511}

txt_list_path = glob.glob('/home/jerry/kitti/label_2_try1/*.txt')
sorted_txt_list = []
# {'Car': 33261, 'Person': 4709, 'Cyclist': 1627}
for item in txt_list_path:
    temp1, temp2 = os.path.splitext(os.path.basename(item))
    sorted_txt_list.append(temp1)
sorted_txt_list.sort()

txt_root_path = '/home/jerry/kitti/label_2_try1/'
img_root_path = '/home/jerry/kitti/image_02/data_object_image_2/training/image_2/'

class_names = cfg.class_names

if __name__ == '__main__':

    # print(sorted_txt_list)
    #
    #
    #
    list_file = open('kitti_train.txt','w',encoding='utf-8')
    print(list_file)



    for filename in sorted_txt_list:
        img_path = os.path.join(img_root_path,filename+'.png')
        txt_path = os.path.join(txt_root_path, filename + '.txt')
        list_file.write(img_path)

        with open(txt_path) as f:

            for line in f:
                a = line.split()

                category = class_names.index(a[0])

                b_box = a[4:8]
                new_line = ' ' + ','.join([str(n) for n in b_box]) + ',' + str(category)
                list_file.write(new_line)
        list_file.write('\n')

    # filename = sorted_txt_list[1]
    # img_path = os.path.join(img_root_path,filename+'.png')
    # print(img_path)
    # txt_path = os.path.join(txt_root_path, filename + '.txt')
    # with open(txt_path) as f:
    #     #new_line = ''
    #
    #     for line in f:
    #         a = line.split()
    #
    #         category = class_names.index(a[0])
    #
    #         b_box = a[4:8]
    #         new_line = ' ' + ','.join([str(n) for n in b_box]) + ',' + str(category)
    #         print(new_line)


