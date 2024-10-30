import pandas as pd
import numpy as np

# 替换为你的xlsx文件路径
file_path = 'score_matrix.xlsx'

# 如果你知道工作表的名称，也可以指定sheet_name参数
df = pd.read_excel(file_path, sheet_name='群体决策')
# print(df)

# 创建一个空字典来存储结果
group_dict = {}

# 遍历DataFrame的每一行
for group_id, group_data in df.groupby('实验组别'):
    # 初始化一个空列表来存储当前实验组别的所有评分列表
    scores_lists = []
    # 分别提取A、B、C三组的评分并添加到列表中
    for prefix in ['A', 'B', 'C']:
        # 假设每组的评分列都是连续的，并且以'-1', '-2', '-3'结尾
        scores_list = [group_data[f"{prefix}-{i + 1}"].iloc[0] for i in range(3)]
        scores_lists.append(scores_list)
        # 将当前实验组别的评分列表列表添加到结果字典中
    group_dict[group_id] = np.array(scores_lists)