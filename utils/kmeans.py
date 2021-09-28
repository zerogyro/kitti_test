import numpy as np

file_path = '/home/jerry/PycharmProjects/kitti_work/dataAnnotation/kitti_train.txt'


def txt2boxes(file_path):
    """
    bounding box x0,y0,x1,y1
    width = x1-x0
    height = y1-y0
    """
    f = open(file_path, 'r')
    pre_boxes = []
    for line in f:

        bboxs = line.split(' ')[1:]
        for bbox in bboxs:
            bbox_num = bbox.split(',')
            width = int(bbox_num[2]) - int(bbox_num[0])
            height = int(bbox_num[3]) - int(bbox_num[1])
            pre_boxes.append([width, height])
    pre_boxes = np.array(pre_boxes)
    f.close()
    return pre_boxes


def iou(boxes, clusters, k):
    """
    calculate intersection of union from boxes and clusters
    """
    # print(boxes.shape)
    n = boxes.shape[0]

    box_area = boxes[:, 0] * boxes[:, 1]
    box_area = box_area.repeat(k)
    box_area = np.reshape(box_area, (n, k))

    cluster_area = clusters[:, 0] * clusters[:, 1]
    cluster_area = np.tile(cluster_area, [1, n])
    cluster_area = np.reshape(cluster_area, (n, k))

    box_w_matrix = np.reshape(boxes[:, 0].repeat(k), (n, k))
    cluster_w_matrix = np.reshape(np.tile(clusters[:, 0], (1, n)), (n, k))
    min_w_matrix = np.minimum(cluster_w_matrix, box_w_matrix)

    box_h_matrix = np.reshape(boxes[:, 1].repeat(k), (n, k))
    cluster_h_matrix = np.reshape(np.tile(clusters[:, 1], (1, n)), (n, k))
    min_h_matrix = np.minimum(cluster_h_matrix, box_h_matrix)

    inter_area = np.multiply(min_w_matrix, min_h_matrix)
    result = inter_area / (box_area + cluster_area - inter_area)

    return result


def yolo_kmeans(boxes, k=9):
    box_number = boxes.shape[0]
    prev = np.zeros(box_number)

    clusters = boxes[np.random.choice(box_number, k, replace=False)]

    while True:

        distances = 1 - iou(boxes, clusters, k)
        cur = np.argmin(distances, axis=1)

        if (prev == cur).all:
            break
        for i in range(k):
            clusters[i] = np.median(boxes[cur == i], axis=0)

        prev = cur
    return clusters



def avg_iou(boxes,clusters,k):
    accuracy = np.mean([np.max(iou(boxes,clusters,k), axis = 1)])
    return accuracy

if __name__ == '__main__':
    pre_boxes = txt2boxes(file_path)
    # clusters = yolo_kmeans(pre_boxes)
    # accuracy = avg_iou(pre_boxes,clusters,9)

    best_clusters = yolo_kmeans(pre_boxes)
    best_accuracy = avg_iou(pre_boxes, best_clusters, 9)
    for i in range(1000):
        clusters = yolo_kmeans(pre_boxes)
        accuracy = avg_iou(pre_boxes, clusters, 9)
        if accuracy>best_accuracy:
            best_accuracy = accuracy
            best_clusters = clusters
    print(best_clusters,best_accuracy)
    anchors = sorted(best_clusters.tolist(),key = (lambda x: x[0] + x[1]))
    print(anchors)




