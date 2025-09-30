import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# y1 = [np.random.randint(0,10) for x in range(20)]
# x1 = range(5,25)
# plt.plot(x1,y1)
# plt.show()
# y1 = [x for x in range(10)]
# y2 = [np.random.randint(0,10) for x in range(10)]
# lines = plt.plot(range(10),y1,range(10),y1,range(10),y2)
# line = lines[0]
# line.set_color('r')
# line.set_linewidth(4)
# line.set_alpha(1)
# line.set_drawstyle('steps-post')
# plt.show()
# y1 = [x for x in range(10)]
# y2 = [np.random.randint(0,10) for x in range(10)]
# lines = plt.plot(range(10),y1,range(10),y2)
# plt.setp(lines,linewidth=4)
# plt.show()
from matplotlib import font_manager
# y = [np.random.randint(10) for x in range(10)]
font = font_manager.FontProperties(fname=r"C:\\Windows\\Fonts\\STFANGSO.TTF",size=20)
# plt.plot(y)
# plt.title("折线图",fontproperties=font)
# plt.xlabel("天数",fontproperties=font)
# plt.xlim((0,10))
# plt.xticks(range(0,11,5))
# plt.show()
#折线图
# avenger = [17974.4,50918.4,30033.0,40329.1,52330.2, 
# 19833.3,11902.0,24322.6,47521.8,32262.0,22841.9,12938.7,
# 4835.1,3118.1,2570.9,2267.9,1902.8,2548.9,5046.6,3600.8]
# plt.figure(figsize=(15,5))
# plt.plot(avenger,marker="o")
# font.set_size(10)
# plt.xticks(range(20),["第%d天"%x for x in range(1,21)],fontproperties=font)
# plt.ylim(0,100000)
# plt.xlabel("天数",fontproperties=font)
# plt.ylabel("票房（单位：万）",fontproperties=font)
# plt.title("复仇者联盟前20天票房数据",fontproperties=font)
# plt.grid(True)
# plt.show()

#柱状图
# movies = {"流浪地球":40.78, "飞驰人生":15.77, "疯狂的外星人":20.83, "新喜剧之王":6.10, "廉政风云":1.10, "神探蒲松龄":1.49, "小猪佩奇过大年":1.22, "熊出没·原始时代":6.71}
# plt.figure(figsize=(15,5))
# movie_df = pd.DataFrame(data={"names":list(movies.keys()), "tickets":list(movies.values())})
# plt.bar(movies.keys(),movies.values())
# plt.xticks(fontproperties=font,size=12)
# plt.yticks(range(0,45,5),["%d亿"%x for x in range(0,45,5)], fontproperties=font,size=12)
# plt.show()
import pandas as pd  
import matplotlib.pyplot as plt 
import numpy as np
from matplotlib import font_manager
data = pd.read_csv("C:\\Users\\周顺\\Documents\\Tencent Files\\3224349663\\FileRecv\\athlete_events.csv") 
df = data.head(100)
df.sort_values(by='Team', inplace=True) 
plt.figure(figsize=(15, 5))
font = font_manager.FontProperties(fname=r"C:\\Windows\\Fonts\\STFANGSO.TTF",size=20)
for category, group in df.groupby('NOC'):
    plt.plot(group['Team'], group['Height'], label=category, marker='o') 
# 设置x轴和y轴的标签
plt.xlabel('Team')  
plt.ylabel('Height')  
# 设置标题 
plt.title('各国运动员',fontproperties=font)  
# 显示图例 
plt.legend()
# 显示网格
plt.grid(True)     
plt.show()