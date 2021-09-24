import numpy as np


file_path = '/home/jerry/PycharmProjects/kitti_work/dataAnnotation/kitti_train.txt'

# bounding box x0,y0,x1,y1
# width = x1-x0
# height = y1-y0
def txt2boxes(file_path):

    f = open(file_path, 'r')
    pre_boxes = []
    for line in f:

        bboxs = line.split(' ')[1:]
        for bbox in bboxs:
            bbox_num = bbox.split(',')
            #print(bbox_num)
            width = int(bbox_num[2]) - int(bbox_num[0])
            height = int(bbox_num[3]) - int(bbox_num[1])
            pre_boxes.append([width,height])
            #print(pre_boxes)
    f.close()
    return pre_boxes





preboxes  = txt2boxes(file_path)
print(len(preboxes))

