from PIL import Image, ImageFont, ImageDraw

img_path_0 = '/home/jerry/kitti/image_02/data_object_image_2/training/image_2/000000.png'
img_path_1 = '/home/jerry/kitti/image_02/data_object_image_2/training/image_2/000001.png'
real_bbox_0 = [[712.40, 143.00, 810.73, 307.92]]
real_bbox_1 = [[599.41, 156.40, 629.75, 189.25],
               [387.63, 181.54, 423.81, 203.12],
               [676.60, 163.95, 688.98, 193.93]
               #[503.89, 169.71, 590.61, 190.13],
               #[511.35, 174.96, 527.81, 187.45],
               #[532.37, 176.35, 542.68, 185.27],
               #[559.62, 175.83, 575.40, 183.15]
               ]

def draw_orig(img_path,bbox):
    image = Image.open(img_path)
    for box in bbox:
        top, left, bottom, right = box
        draw = ImageDraw.Draw(image)
        draw.rectangle([top, left, bottom, right])
    return image


if __name__ == '__main__':
    image = draw_orig(img_path_1,real_bbox_1)
    image.show()
