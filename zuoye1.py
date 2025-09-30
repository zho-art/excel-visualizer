# #生产成本

# import numpy as np
# import matplotlib.pyplot as plt 
# # 设置中文显示
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为黑体
# plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
# # 生产材料及其成本占比
# categories = ['硬件', '软件', '数据', '开发', '维护']
# cost_percentages = [40, 20, 15, 15, 10]  # 各项成本占比
# # 将数据闭合（雷达图需要闭合）
# categories += [categories[0]]
# cost_percentages += [cost_percentages[0]]
# # 计算角度
# angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
# angles += angles[:1]  # 闭合
# # 绘制雷达图
# fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
# ax.fill(angles, cost_percentages, color='skyblue', alpha=0.6)  # 填充区域
# ax.plot(angles, cost_percentages, color='blue', linewidth=2)  # 绘制边界线

# # 设置角度刻度
# ax.set_xticks(angles[:-1])
# ax.set_xticklabels(categories[:-1], fontsize=12)

# # 设置角度标签的位置
# for label, angle in zip(ax.get_xticklabels(), angles):
#     if angle in (0, np.pi):
#         label.set_horizontalalignment('center')
#     elif 0 < angle < np.pi:
#         label.set_horizontalalignment('left')
#     else:
#         label.set_horizontalalignment('right')

# # 设置径向刻度
# ax.set_rlabel_position(180)  # 将径向刻度标签放在左侧
# plt.yticks([20, 40, 60, 80, 100], ["20%", "40%", "60%", "80%", "100%"], color="grey", size=10)
# plt.ylim(0, 100)

# # 添加标题
# plt.title('生产材料成本占比雷达图', size=16, y=1.1)

# # 显示图表
# plt.tight_layout()
# plt.show()


# #发展能力比率
# import matplotlib.pyplot as plt
# import numpy as np

# # 数据
# years = ['2023', '2024', '2025', '2026']
# net_profit_growth = [None, -0.19, 0.94, 1.25]  # 净利润增长率
# main_business_growth = [None, 0.02, 1.11, 1.08]  # 主营业务增长率
# asset_growth = [None, 0.18, 0.18, 0.15]  # 资产增长率

# # 过滤掉 None 值
# years_filtered = years[1:]
# net_profit_growth_filtered = net_profit_growth[1:]
# main_business_growth_filtered = main_business_growth[1:]
# asset_growth_filtered = asset_growth[1:]

# # 创建折线图
# plt.figure(figsize=(10, 6))

# # 绘制净利润增长率折线
# plt.plot(years_filtered, net_profit_growth_filtered, marker='o', label='净利润增长率', color='blue', linewidth=2)

# # 绘制主营业务增长率折线
# plt.plot(years_filtered, main_business_growth_filtered, marker='s', label='主营业务增长率', color='green', linewidth=2)

# # 绘制资产增长率折线
# plt.plot(years_filtered, asset_growth_filtered, marker='^', label='资产增长率', color='orange', linewidth=2)

# # 标注数据点
# for i, (year, net_profit, main_business, asset) in enumerate(zip(years_filtered, net_profit_growth_filtered, main_business_growth_filtered, asset_growth_filtered)):
#     plt.text(i, net_profit + 0.05, f'{net_profit:.2f}', ha='center', va='bottom', color='blue')
#     plt.text(i, main_business + 0.05, f'{main_business:.2f}', ha='center', va='bottom', color='green')
#     plt.text(i, asset + 0.05, f'{asset:.2f}', ha='center', va='bottom', color='orange')

# # 设置标题和标签
# plt.title('地脉之眼-电成像微裂缝智能分析系统发展能力比率', fontsize=16)
# plt.xlabel('年份', fontsize=12)
# plt.ylabel('增长率', fontsize=12)
# plt.legend(loc='upper left')

# # 设置网格线
# plt.grid(True, linestyle='--', alpha=0.6)

# # 显示图表
# plt.tight_layout()
# plt.show()


import matplotlib.pyplot as plt

# 设置中文字体，确保汉字正常显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 数据
labels = ['自筹资金', '专利技术入股', '合作单位和风险投资', '银行贷款']
sizes = [90, 90, 120, 200]  # 单位：万元
colors = ['black', '#333333', '#666666', 'yellow']  # 黑色、渐黑、黄色

# 绘制饼图
plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)

# 设置标题
plt.title('公司融资构成', fontsize=16)

# 显示图形
plt.axis('equal')  # 使饼图为正圆形
plt.show()