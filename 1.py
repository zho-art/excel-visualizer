# from gettext import translation
# import tkinter as tk
# from turtle import width

# def CLick():
#     key = input_va.get()
#     result = translation(key)
#     text.insert('insert',result)
# from numpy import pad
# root = tk.Tk()
# root.title('翻译软件')
# root.geometry('700x500+200+200')
# #固定窗口大小
# #root.resizable(width:False,height:False)
# input_frame = tk.Frame(root)
# input_frame.pack(pady=20)
# input_va = tk.StringVar()
# tk.Label(input_frame,text='请输入要翻译的内容:',font=('微软雅黑',20)).pack(side=tk.LEFT)
# tk.Entry(input_frame,font=('微软雅黑',20) ,textvariable=input_va).pack(side=tk.LEFT,fill=tk.BOTH,padx=20)
# #设置按钮
# tk.Button(input_frame,text="翻译",font=('微软雅黑',20),command=CLick).pack(side=tk.LEFT)
# text_frame = tk.Frame(root)
# text_frame.pack()
# text = tk.Text(text_frame,font=('微软雅黑',20))
# text.pack()
# root.mainloop()


import numpy as np
import matplotlib.pyplot as plt 

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 生产材料及其成本占比
categories = ['硬件', '软件', '数据', '开发', '维护']
cost_percentages = [40, 20, 15, 15, 10]  # 各项成本占比

# 将数据闭合（雷达图需要闭合）
categories += [categories[0]]
cost_percentages += [cost_percentages[0]]

# 计算角度
angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
angles += angles[:1]  # 闭合

# 绘制雷达图
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.fill(angles, cost_percentages, color='skyblue', alpha=0.6)  # 填充区域
ax.plot(angles, cost_percentages, color='blue', linewidth=2)  # 绘制边界线

# 设置角度刻度
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories[:-1], fontsize=12)

# 设置角度标签的位置
for label, angle in zip(ax.get_xticklabels(), angles):
    if angle in (0, np.pi):
        label.set_horizontalalignment('center')
    elif 0 < angle < np.pi:
        label.set_horizontalalignment('left')
    else:
        label.set_horizontalalignment('right')

# 设置径向刻度
ax.set_rlabel_position(180)  # 将径向刻度标签放在左侧
plt.yticks([20, 40, 60, 80, 100], ["20%", "40%", "60%", "80%", "100%"], color="grey", size=10)
plt.ylim(0, 100)

# 添加标题
plt.title('生产材料成本占比雷达图', size=16, y=1.1)

# 显示图表
plt.tight_layout()
plt.show()
