import matplotlib.pyplot as plt  
import numpy as np  
import pandas as pd  
from matplotlib import font_manager  
  
# 读取CSV文件并获取前100行数据，同时确保没有缺失值  
file_path = 'C:\\Users\\周顺\\Documents\\Tencent Files\\3224349663\\FileRecv\\athlete_events.csv'  
data = pd.read_csv(file_path).dropna()  
athletes = data.head(2000)  
  
# 假设身高数据存储在名为'Height'的列中（请根据实际情况修改列名）  
height_column = 'Height'  # 替换为实际的身高列名  
  
# 将身高数据分组到不同的区间内，并计算每个区间的频数  
bins = [159, 162, 170, 175, 180, 185, 190, 192, 195]  
labels = ["159-162", "162-170", "170-175", "175-180", "180-185", "185-190", "190-192", "192-195"]  
heights, bin_edges = np.histogram(athletes[height_column], bins=bins)  
  
# 设置字体以显示中文  
font = font_manager.FontProperties(fname=r"C:\\Windows\\Fonts\\STFANGSO.TTF", size=20)  
plt.rcParams['font.sans-serif'] = ['SimHei']  
  
# 绘制条形图  
plt.ylim(0, 500)  # 设置y轴限制  
colors = ["red", "yellow", 'blue', 'black', 'green', 'orange', 'purple', 'pink']  
plt.bar(range(len(heights)), heights, color=colors, width=0.6)  
plt.xticks(range(len(heights)), labels)  
for i in range(len(heights)):  
    plt.text(x=i - 0.05, y=heights[i] + 0.2, s='%d' % heights[i])  
plt.xlabel("身高/cm", fontproperties=font)  
plt.ylabel("频数(运动员人数)", fontproperties=font)  
plt.show()