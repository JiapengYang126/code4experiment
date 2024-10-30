import numpy as np

from numpy.linalg import norm


def cosine_similarity(matrix1, matrix2):
    """
    计算两个矩阵之间的余弦相似度
    :param matrix1: 第一个矩阵
    :param matrix2: 第二个矩阵
    :return: 余弦相似度矩阵
    """
    # 将两个矩阵展平为向量
    A_flat = matrix1.flatten()
    B_flat = matrix2.flatten()
    # print(A_flat)
    # print(B_flat)
    # 计算余弦相似度
    cosine_similarity = np.dot(A_flat, B_flat) / (norm(A_flat) * norm(B_flat))

    return cosine_similarity



