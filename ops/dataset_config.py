# Code for "GTSN: Global Temporal Difference Shift Network"

import os

ROOT_DATASET = './ssd/video/'  # '/data/jilin/'








def resthand(modality):
    filename_categories = 'category.txt'
    if modality == 'RGB':
        root_data = ROOT_DATASET + 'something/v2/lhand4'
        filename_imglist_train = 'something/v2/460.txt'
        filename_imglist_val = 'something/v2/461.txt'
        prefix = '{:06d}.jpg'
    elif modality == 'Flow':
       
        root_data = ROOT_DATASET + '3.17hand/EVM'
        filename_imglist_train = '3.17hand/train.txt'
        filename_imglist_val = '3.17hand/test.txt'
        prefix = '{:06d}.jpg'
    else:
        raise NotImplementedError('no such modality:'+modality)
    return filename_categories, filename_imglist_train, filename_imglist_val, root_data, prefix


def restleg(modality):
    filename_categories = 'category.txt'
    if modality == 'RGB':
        root_data = ROOT_DATASET + 'something/v2/lhand4'
        filename_imglist_train = 'something/v2/460.txt'
        filename_imglist_val = 'something/v2/461.txt'
        prefix = '{:06d}.jpg'
    elif modality == 'Flow':

        root_data = ROOT_DATASET + '3.17leg/EVM'
        filename_imglist_train = '3.17leg/train.txt'
        filename_imglist_val = '3.17leg/test.txt'
        prefix = '{:06d}.jpg'
    else:
        raise NotImplementedError('no such modality:' + modality)
    return filename_categories, filename_imglist_train, filename_imglist_val, root_data, prefix
def restjaw(modality):
    filename_categories = 'category.txt'
    if modality == 'RGB':
        root_data = ROOT_DATASET + 'something/v2/lhand4'
        filename_imglist_train = 'something/v2/460.txt'
        filename_imglist_val = 'something/v2/461.txt'
        prefix = '{:06d}.jpg'
    elif modality == 'Flow':

        root_data = ROOT_DATASET + '3.17jaw/EVM'
        filename_imglist_train = '3.17jaw/train.txt'
        filename_imglist_val = '3.17jaw/test.txt'
        prefix = '{:06d}.jpg'
    else:
        raise NotImplementedError('no such modality:' + modality)
    return filename_categories, filename_imglist_train, filename_imglist_val, root_data, prefix





def return_dataset(dataset, modality):
    dict_single = {'resthand': resthand,
                   'restleg': restleg, 'restjaw': restjaw}
    if dataset in dict_single:
        file_categories, file_imglist_train, file_imglist_val, root_data, prefix = dict_single[dataset](modality)
    else:
        raise ValueError('Unknown dataset '+dataset)

    file_imglist_train = os.path.join(ROOT_DATASET, file_imglist_train)
    file_imglist_val = os.path.join(ROOT_DATASET, file_imglist_val)
    if isinstance(file_categories, str):
        file_categories = os.path.join(ROOT_DATASET, file_categories)
        with open(file_categories) as f:
            lines = f.readlines()
        categories = [item.rstrip() for item in lines]
    else:  # number of categories
        categories = [None] * file_categories
    n_class = len(categories)
    print('{}: {} classes'.format(dataset, n_class))
    return n_class, file_imglist_train, file_imglist_val, root_data, prefix
