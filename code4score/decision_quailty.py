from group_decision_matrix_to_dic import group_dict
from cosine import cosine_similarity
import numpy as np


matrix_Standardization = np.array([[4, 5, 2], [3, 2, 2],[5, 2, 5]])

print(matrix_Standardization)

# i是组别
i = 2
group_mean_dict = {}

while i < 25:
    ls = []
    for key in group_dict:
        if int(key.split('-', 1)[0]) == i:
            ls.append(group_dict[key])
    group_mean_dict[i] = (ls[0]+ls[1]+ls[2])/3

    if i == 12:
        print(group_mean_dict[i])
    i += 1


decision_quailty_dict = {}

for key in group_mean_dict:
    similarity = cosine_similarity(matrix_Standardization, group_mean_dict[key])
    print(similarity)
    decision_quailty_dict[key] = similarity

print(decision_quailty_dict)
