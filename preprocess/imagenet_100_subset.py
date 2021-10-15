### script to generate ImageNet-100 dataset
### official split: https://github.com/HobbitLong/CMC/blob/master/imagenet100.txt

import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--imagenet_path', type=str, required=True)
parser.add_argument('--imagenet100_path', type=str, required=True)
args = parser.parse_args()

source_folder = args.imagenet_path #'/path/to/imagenet/'
target_folder = args.imagenet100_path #'/path/to/imagenet-100/'

imagenet_100_list = ['n02869837', 'n01749939', 'n02488291', 'n02107142', 'n13037406', 
                     'n02091831', 'n04517823', 'n04589890', 'n03062245', 'n01773797', 
                     'n01735189', 'n07831146', 'n07753275', 'n03085013', 'n04485082', 
                     'n02105505', 'n01983481', 'n02788148', 'n03530642', 'n04435653', 
                     'n02086910', 'n02859443', 'n13040303', 'n03594734', 'n02085620', 
                     'n02099849', 'n01558993', 'n04493381', 'n02109047', 'n04111531', 
                     'n02877765', 'n04429376', 'n02009229', 'n01978455', 'n02106550', 
                     'n01820546', 'n01692333', 'n07714571', 'n02974003', 'n02114855', 
                     'n03785016', 'n03764736', 'n03775546', 'n02087046', 'n07836838', 
                     'n04099969', 'n04592741', 'n03891251', 'n02701002', 'n03379051', 
                     'n02259212', 'n07715103', 'n03947888', 'n04026417', 'n02326432', 
                     'n03637318', 'n01980166', 'n02113799', 'n02086240', 'n03903868', 
                     'n02483362', 'n04127249', 'n02089973', 'n03017168', 'n02093428', 
                     'n02804414', 'n02396427', 'n04418357', 'n02172182', 'n01729322', 
                     'n02113978', 'n03787032', 'n02089867', 'n02119022', 'n03777754', 
                     'n04238763', 'n02231487', 'n03032252', 'n02138441', 'n02104029', 
                     'n03837869', 'n03494278', 'n04136333', 'n03794056', 'n03492542', 
                     'n02018207', 'n04067472', 'n03930630', 'n03584829', 'n02123045', 
                     'n04229816', 'n02100583', 'n03642806', 'n04336792', 'n03259280', 
                     'n02116738', 'n02108089', 'n03424325', 'n01855672', 'n02090622']


os.makedirs(target_folder, exist_ok=True) 
for mode in ['train', 'val']:
    source_sub_folder = os.path.join(source_folder, mode)
    target_sub_folder = os.path.join(target_folder, mode)
    os.makedirs(target_sub_folder, exist_ok=True) 
    for folder_name in os.listdir(source_sub_folder):
        if folder_name in imagenet_100_list:
            script = 'scp -r %s %s'(os.path.join(source_sub_folder, folder_name), target_sub_folder)
            os.system(script)
