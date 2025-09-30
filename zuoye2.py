import pandas as pd  
import matplotlib.pyplot as plt  
import numpy as np  
from matplotlib import font_manager  
# # 读取数据  
data = pd.read_csv("C:\\Users\\周顺\\Documents\\Tencent Files\\3224349663\\FileRecv\\athlete_events.csv")  
df = data.head(200) 
# # df['Height'] = pd.to_numeric(df['Height'], errors='coerce')  
# # df = df.dropna(subset=['Height'])   
# # team_averages = df.groupby('NOC')['Height'].mean().reset_index()    
# # plt.figure(figsize=(15, 5))  
# # font = font_manager.FontProperties(fname=r"C:\\Windows\\Fonts\\STFANGSO.TTF", size=10)  
# # # 绘制条形图  
# # plt.bar(team_averages['NOC'], team_averages['Height'], label='Average Height per NOC', color='skyblue')  
# # # 设置x轴和y轴的标签  
# # plt.xlabel('NOC', fontproperties=font)  
# # plt.ylabel('Height', fontproperties=font)  
# # # 设置标题  
# # plt.title('各国运动员平均身高', fontproperties=font)  
# # # 显示图例  
# # plt.legend()  
# # # 显示网格  
# # plt.grid(True)  
# # # 显示图表  
# # plt.show()

# #散点图
# #import pandas as pd  
# #import matplotlib.pyplot as plt  
# # import numpy as np  
# # from matplotlib import font_manager  
# # data = pd.read_csv('C:\\Users\\周顺\\Documents\\Tencent Files\\3224349663\\FileRecv\\athlete_events.csv').dropna()
# # athletes = data.head(500)
# # male_athletes = athletes[athletes['Sex'] =='M']
# # male_heights = male_athletes['Height']
# # male_weights = male_athletes['Weight']
# # male_height_mean = male_heights.mean()
# # male_weight_mean = male_weights.mean()
# # female_athletes = athletes[athletes['Sex'] =='F']
# # female_heights = female_athletes['Height']
# # female_weights = female_athletes['Weight']
# # female_height_mean = female_heights.mean()
# # female_weight_mean = female_weights.mean()
# # plt.figure(figsize=(15,5))
# # plt.scatter(male_heights,male_weights,s=male_athletes['Age'],marker='^')
# # plt.scatter(female_heights,female_weights,s=female_athletes['Age'],alpha=0.5)
# # plt.axvline(male_height_mean,linewidth=2,c='b')
# # plt.axhline(male_weight_mean,linewidth=2,c='b')
# # plt.show()
# import pandas as pd  
# import matplotlib.pyplot as plt  
# import numpy as np  
# from matplotlib import font_manager
# data = pd.read_csv('C:\\Users\\周顺\\Documents\\Tencent Files\\3224349663\\FileRecv\\athlete_events.csv').dropna()
# athletes = data.head(100)
# font = font_manager.FontProperties(fname=r"C:\\Windows\\Fonts\\STFANGSO.TTF",size=20)
# plt.boxplot(athletes[['Weight']].dropna(),sym='^',vert=False, widths=[0.1], labels=['Weight'])
# countries = {'CHN':'中国','JPN':"日本",'KOR':'韩国','USA':"美国", 'CAN':"加拿大",'BRA':"巴西",'GBR':"英国",'FRA':"法国",'ITA':"意大利", 'ETH':"埃塞俄比亚",'KEN':"肯尼亚",'NIG':"尼日利亚"}
# dfs = []
# for code in countries.keys():
#     df = athletes[athletes['NOC']==code]['Weight'].dropna()
#     dfs.append(df)
# font = font_manager.FontProperties(fname=r"C:\\Windows\\Fonts\\msyh.ttc",size=14)
# plt.figure(figsize=(20,5))
# plt.boxplot(dfs)
# plt.xticks(range(1,13),countries.values(),fontproperties=font)  
# plt.show() 


# import pandas as pd  
# import matplotlib.pyplot as plt  
# import numpy as np  
# from matplotlib import font_manager  
  
# # 读取数据并删除缺失值  
# data = pd.read_csv('C:\\Users\\周顺\\Documents\\Tencent Files\\3224349663\\FileRecv\\athlete_events.csv').dropna(subset=['Weight', 'NOC'])  
# athletes = data.head(3000)  
# # 定义国家代码到名称的映射  
# countries = {'CHN': '中国', 'JPN': "日本", 'KOR': '韩国', 'USA': "美国", 'CAN': "加拿大",'BRA': "巴西", 'GBR': "英国", 'FRA': "法国", 'ITA': "意大利", 'ETH': "埃塞俄比亚", 'KEN': "肯尼亚", 'NIG': "尼日利亚"}  
# # 准备数据框架列表，每个国家一个  
# dfs = []  
# positions = []  # 用于存储箱线图的位置（x轴标签的索引）  
# for code, name in countries.items():  
#     df = athletes[athletes['NOC'] == code]['Weight']  
#     dfs.append(df)  
#     positions.append(name)  # 实际上这里应该使用数字索引，稍后会在xticks中映射到国家名称  
  
# # 注意：由于我们稍后会用xticks来设置x轴的标签，这里我们只需要一个占位符列表来指定箱线图的位置  
# # 因此，我们可以简单地使用range(len(dfs))来生成位置索引  
# # 但是为了保持代码的清晰性，我还是保留了positions列表（尽管在这里它没有被直接使用）  
# # 实际上，我们应该在xticks中直接使用range(len(dfs))作为ticks参数，并将countries.values()作为labels参数  
  
# # 设置字体  
# font = font_manager.FontProperties(fname=r"C:\\Windows\\Fonts\\msyh.ttc", size=14)  
  
# # 绘制箱线图  
# plt.figure(figsize=(20, 5))  
# plt.boxplot(dfs, vert=True, patch_artist=True)  # patch_artist=True用于后续设置箱体的颜色  
  
# # 设置箱体的颜色（可选）  
# for patch, color in zip(plt.gca().artists, ['pink', 'lightblue', 'lightgreen', 'lightcoral', 'lightgray',  
#                                            'lightcyan', 'lightgoldenrodyellow', 'lightpink', 'lightsteelblue',  
#                                            'lightyellow', 'lightsalmon', 'lightseagreen']):  
#     patch.set_facecolor(color)  
  
# # 设置x轴标签  
# plt.xticks(range(1, len(dfs) + 1), countries.values(), fontproperties=font)  
# plt.xlabel('国家',fontproperties=font)  
# plt.ylabel('体重 (kg)',fontproperties=font)  
# plt.title('各国运动员体重箱线图', fontproperties=font)  
# plt.grid(axis='y', linestyle='--', alpha=0.7)  
# plt.show()

#直方图

import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager 
# 用黑体显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
data = [2,6,12,19,10,8,4,2]
plt.ylim(0,23)
labels = ["149-152", "152-155", "155-158", "158-161","161-164","164-167","167-170","170-173"]
colors = ["red","yellow",'blue','black','green','orange','purple','pink']
font = font_manager.FontProperties(fname=r"C:\\Windows\\Fonts\\STFANGSO.TTF",size=20)
plt.bar(range(len(data)), data,color=colors,width=0.6)
plt.xticks(range(len(data)),labels)
for i in range(len(data)):
    plt.text(x= i- 0.05 , y=data[i] + 0.2, s = '%d' % data[i])
plt.xlabel("身高/cm",)
plt.ylabel("频数(学生人数)")