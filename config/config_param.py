import numpy as np

class_names = ['Car', 'Person', 'Cyclist']

anchors = np.array([(27, 23), (32, 30), (55, 38),
                    (76, 52), (81, 65), (138, 44),
                    (116, 115), (190, 114), (309, 174)],
                   np.float32)
