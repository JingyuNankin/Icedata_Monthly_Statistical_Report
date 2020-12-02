import pandas as pd
import numpy as np
import sys

#当前目录的data202011.xlsx为已经人工筛查完的数据表
df = pd.read_excel(sys.path[0] + r"\\data202011.xlsx")

vocalNames = ["洛天依","言和","乐正绫","乐正龙牙","徵羽摩柯","墨清弦",
              "星尘","心华","初音未来","赤羽","诗岸","苍穹","海伊",
              "中文VOCALOID","中文Synthesizer V","总体"]
viewList = [[] for i in range(len(vocalNames))]
favoList = [[] for i in range(len(vocalNames))]

#遍历这个Data Frame的每一行，判断这一行是哪个歌姬唱的、属于什么引擎
for index, row in df.iterrows():
    isVocalod = False
    isSynthv = False
    for i in range(len(vocalNames) - 3):
        #如果在标题、简介、tag中找到了歌姬的名字
        string = str(row['title']) + str(row['description']) + str(row['tag'])
        if string.count(vocalNames[i]) > 0:
            viewList[i].append(row['play'])
            favoList[i].append(row['favorites'])
            if i <= 8:#前面几个是VOCALOID虚拟歌姬
                isVocalod = True
            if i >= 9:#后面几个是Synthesizer V虚拟歌姬
                isSynthv = True
    if isVocalod:
        viewList[13].append(row['play'])
        favoList[13].append(row['favorites'])
    if isSynthv:
        viewList[14].append(row['play'])
        favoList[14].append(row['favorites'])
    viewList[15].append(row['play'])
    favoList[15].append(row['favorites'])

#创建resultDF作为保存结果的Data Frame，填写各行的内容
resultDf = pd.DataFrame()
for i in range(len(vocalNames)):
    if len(viewList[i]) >= 1:
        npViewArray = np.asarray(viewList[i])
        npFavoArray = np.asarray(favoList[i])
        newDF = pd.DataFrame({"类名":       vocalNames[i],
                              "投稿数":     np.sum(npViewArray >= 0),
                              "播放>1000":  np.sum(npViewArray >= 1000),
                              "播放>10000": np.sum(npViewArray >= 10000),
                              "播放>100000":np.sum(npViewArray >= 100000),
                              "播放p-90%":  np.percentile(npViewArray, 90),
                              "播放p-95%":  np.percentile(npViewArray, 95),
                              "最高播放":   np.amax(npViewArray),
                              "总播放":     np.sum(npViewArray),
                              "收藏>1000":  np.sum(npFavoArray >= 1000),
                              "收藏>10000": np.sum(npFavoArray >= 10000),
                              "收藏>100000":np.sum(npFavoArray >= 100000),
                              "收藏p-90%":  np.percentile(npFavoArray, 90),
                              "收藏p-95%":  np.percentile(npFavoArray, 95),
                              "最高收藏":   np.amax(npFavoArray),
                              "总收藏":     np.sum(npFavoArray),
                              },index=[i])
    else:
        newDF = pd.DataFrame({"类名":       vocalNames[i],
                              "投稿数":     np.sum(npViewArray >= 0),
                              "播放>1000":  np.sum(npViewArray >= 1000),
                              "播放>10000": np.sum(npViewArray >= 10000),
                              "播放>100000":np.sum(npViewArray >= 100000),
                              "播放p-90%":  0,
                              "播放p-95%":  0,
                              "最高播放":   np.amax(npViewArray),
                              "总播放":     np.sum(npViewArray),
                              "收藏>1000":  np.sum(npFavoArray >= 1000),
                              "收藏>10000": np.sum(npFavoArray >= 10000),
                              "收藏>100000":np.sum(npFavoArray >= 100000),
                              "收藏p-90%":  0,
                              "收藏p-95%":  0,
                              "最高收藏":   np.amax(npFavoArray),
                              "总收藏":     np.sum(npFavoArray),
                              },index=[i])
    resultDf = resultDf.append(newDF)
#提示运行结束并保存结果
print("运行完毕")
resultDf.to_csv(sys.path[0] + r"\\result202011.csv")