import glob
from dataAnnotation import annotation_tools

# clone a second working label directory
txt_list = glob.glob('/home/jerry/kitti/label_2_try1/*.txt')
dic = annotation_tools.orig_stat(txt_list)

# washout files with other classes
# Do not touch after wash done

if __name__ == '__main__':
    for i,item in enumerate(txt_list):
        new_txt=[]
        #print(item)

        with open(item, 'r') as f:
            for line in f:
                labeldata = line.strip().split(' ')
                if labeldata[0] in ['Car', 'Truck', 'Van', 'Tram']:
                    labeldata[0] = 'Car'

                if labeldata[0] in ['Pedestrian','Person_sitting']:
                    labeldata[0] = 'Person'
                if labeldata[0] == 'DontCare':
                    continue
                if labeldata[0] == 'Misc':
                    continue
                #print(labeldata)
                a = annotation_tools.merge2str(labeldata)
                new_txt.append(a)

        with open(item, 'w+') as w_tdf:  # w+delete orig file contents
            for temp in new_txt:
                w_tdf.write(temp)


