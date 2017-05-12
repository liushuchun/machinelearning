# coding: utf-8

from math import log


def calc_shannon_ent(data_set):
    num_entries = len(data_set)
    label_counts = {}
    for vec in data_set:
        current_label = vec[-1]  # 最后一个是label
        if current_label not in label_counts.keys():  # 如果不存在，就初始化这个label，统计所有类别的次数
            label_counts[current_label] = 0
        label_counts[current_label] += 1

    shannon_ent = 0.0
    for key in label_counts:
        prob = float(label_counts[key]) / num_entries
        shannon_ent -= prob * log(prob, 2)

    return shannon_ent


# 殇越高，则数据越混乱
def create_data():
    data_set = [[1, 1, 'yes'],
                [1, 1, 'yes'],
                [1, 0, 'no'],
                [0, 1, 'no'],
                [0, 1, 'no']]

    labels = ['no surfacing', 'flippers']
    return data_set, labels


def split_data_set(data_set, axis, value):
    '''
    data_set:待划分的数据集
    axis:划分的数据集的特征
    value:需要返回的特征值
    '''
    ret_data_set = [] #防止对原有的list产生影响
    for vec in data_set:
        if vec[axis] == value:
            reduced_vec = vec[:axis]
            reduced_vec.extend(vec[axis + 1:])
            ret_data_set.append(reduced_vec)

    return ret_data_set
