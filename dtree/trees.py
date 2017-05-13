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
    ret_data_set = []  # 防止对原有的list产生影响
    for vec in data_set:
        if vec[axis] == value:
            reduced_vec = vec[:axis]
            reduced_vec.extend(vec[axis + 1:])
            ret_data_set.append(reduced_vec)

    return ret_data_set


def choose_best_feature_tosplit(data_set):
    num_features = len(data_set[0]) - 1
    base_entropy = calc_shannon_ent(data_set)
    best_info_gain = 0.0
    best_feature = -1
    for i in range(num_features):
        feature_list = [example[i] for example in data_set]
        unique_vals = set(feature_list)
        new_entropy = 0.0
        for value in unique_vals:
            sub_data_set = split_data_set(data_set, i, value)
            prob = len(sub_data_set) / float(len(data_set))
            new_entropy += prob * calc_shannon_ent(sub_data_set)

        info_gain = base_entropy - new_entropy
        if(info_gain) > best_info_gain:
            best_info_gain = info_gain
            best_feature = i

    return best_feature


def major_cnt(class_list):
    class_count = {}
    for vote in class_list:
        if vote not in class_count.keys():
            class_count[vote] = 0

        class_count[vote] += 1

        sorted_class_count = sorted(
            class_count.iteritems, key=operator.itemgetter(1), reverse=True)

        return sorted_class_count[0][0]


def create_tree(data_set, labels):
    class_list = [example[-1] for example in data_set]
    if class_list.count(class_list[0]) == len(class_list):  # 类别完全相同，则停止继续划分
        return class_list[0]

    if len(data_set[0]) == 1:  # 遍历完所有特征时返回出现次数最多的
        return major_cnt(class_list)

    best_feature = choose_best_feature_tosplit(data_set)
    besf_feature_label = labels[best_feature]
    my_tree = {besf_feature_label: {}}
    del(labels[best_feature])
    feature_values = [example[best_feature]
                      for example in data_set]  # 得到列表包含的所有属性值

    unique_vals = set(feature_values)
    for value in unique_vals:
        sub_labels = labels[:]
        my_tree[besf_feature_label][value] = create_tree(
            split_data_set(data_set, best_feature, value), sub_labels)

    return my_tree


def retrieve_trees(i):
    list_of_trees = [{
        'no surfacing': {0: 'no', 1: {'flippers':
                                      {
                                          0: 'no', 1: 'yes'}}}},
                     {
        'no surfacing': {
            0: 'no', 1: {
                'flippers': {
                    0: {'head': {0: 'no', 1: 'yes'}}, 1: 'no'
                }
            }
        }
    }]


def classify(input_tree, feature_labels, test_vec):
    print input_tree
    keys = input_tree.keys()
    first_str = keys[0]
    second_dict = input_tree[first_str]
    feature_index = feature_labels.index(first_str)
    for key in second_dict.keys():
        if test_vec[feature_index] == key:
            if type(second_dict[key]).__name__ == 'dict':
                class_label = classify(
                    second_dict[key], feature_labels, test_vec)
            else:
                class_label = second_dict[key]
    return class_label
