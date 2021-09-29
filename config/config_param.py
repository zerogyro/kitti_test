import numpy as np
#
# #----------------------------------------YOLO---------------------------------
num_bbox = 3
anchor_masks = [[6, 7, 8], [3, 4, 5], [0, 1, 2]]
# data_path = '/home/jerry/PycharmProjects/jerry_yolo/2012_train.txt'
# input_shape = (416, 416)
# ignore_thresh = 0.5
# #-------------------------------------VOC-----------------------------------------
num_classes = 3
# anchors = np.array([(10, 13), (16, 30), (33, 23),
#                     (30, 61), (62, 45), (59, 119),
#                     (116, 90), (156, 198), (373, 326)],
#                    np.float32)
#
#
#
#
# #--------------------------------------KITTI--------------------------------------
# # num_classes_kitti = 3
class_names = ['Car', 'Person', 'Cyclist']
data_path_kitti = '/home/jerry/PycharmProjects/kitti_work/dataAnnotation/kitti_train.txt'
# #
anchors = np.array([(27, 23), (32, 30), (55, 38),
                    (76, 52), (81, 65), (138, 44),
                    (116, 115), (190, 114), (309, 174)],
                   np.float32)
# #
#
# #---------------------------------------TRAINING----------------------------------------
valid_rate = 0.1
batch_size = 8
learn_rating = 1e-5
epochs = 50


# iou忽略阈值
ignore_thresh = 0.5
iou_threshold = 0.1

import numpy as np

# input data

data_path = '/home/jerry/PycharmProjects/jerry_yolo/2012_train.txt'
input_shape = (416, 416)

#num_classes = 20

# anchors = np.array([(10, 13), (16, 30), (33, 23),
#                     (30, 61), (62, 45), (59, 119),
#                     (116, 90), (156, 198), (373, 326)],
#                    np.float32)











