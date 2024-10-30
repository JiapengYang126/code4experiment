# 共识达成程度
from group_decision_matrix_to_dic import group_dict
from cosine import cosine_similarity


# i是组别
i = 2
group_consensus_dict = {}

m = n = l = 3

while i < 25:
    ls = []
    for key in group_dict:
        if int(key.split('-', 1)[0]) == i:
            ls.append(group_dict[key])

    matrix_a = ls[0]
    matrix_b = ls[1]
    matrix_c = ls[2]

    # 计算群体决策平均矩阵
    average_matrix = (ls[0] + ls[1] + ls[2]) / 3

    similarity_1 = cosine_similarity(matrix_a, average_matrix)
    similarity_2 = cosine_similarity(matrix_b, average_matrix)
    similarity_3 = cosine_similarity(matrix_c, average_matrix)


    # 计算平均共识度
    CD = (similarity_1 + similarity_2 + similarity_3) / 3

    print(CD)

    group_consensus_dict[i] = CD

    i += 1


