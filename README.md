# Icedata_Monthly_Statistical_Report
冰数据，哔哩哔哩弹幕视频网（BILIBILI，下简称B站）音乐区VOCALOID·UTAU分区《中文VOCALOID与Synthesizer V统计月报》相关程序。本程序使用Python语言编写。
统计月报见于https://www.bilibili.com/read/readlist/rl68394
本仓库包括B站数据获取、数据简单分析两个部分。

## 第一节、功能简介

### 1.数据获取（尚未上传）

从B站音乐区-VOCALOID·UTAU子分区获取“标题、简介或标签包含各VOCALOID、Synthesizer V歌姬名称”的投稿。存储为一份Excel表格，包括AV号、BV号、标题、UP主、播放量、收藏量、评论量、公开时间等多个列（字段）。
- 能够设置起始时间，至获取起始时间之后的投稿信息。
- 能够排除重复的行（记录）。
- 可以修改程序的部分参数，获取其它区（或所有区）、其它关键词（不一定是歌姬名字）的B站视频数据。

### 2.数据分析

获取到的数据一般需要手工进行数据预处理（恕我暂不能自动化）：在Excel中删除不必要的行（记录），添加漏掉的行（记录）。（譬如《忘川风华录》系列曲就经常漏）

数据分析程序能够读取本地的Excel文件，对各个歌姬、引擎及总体的数据进行简单分析。分析结果包括投稿数、殿堂数、播放量90%分位数、最高播放量、总播放量等等多个字段。
分析结果以csv格式存储。

## 第二节、使用方法

下载本程序的源代码，需要有Python相应的运行环境。

### 1.数据获取（咕咕咕）

### 2.数据分析
将已经手工处理过的Excel表格保存好，该Excel表格需要包括'title'、'description'、'tag'、'play'、'favorites'这5列（字段），
修改源代码中最前面与最后面的
```
df = pd.read_excel(sys.path[0] + r"\data202011.xlsx")
```
和
```
resultDf.to_csv(sys.path[0] + r"\result202011.csv")
```
中的参数，来修改欲读取的数据文件路径与保存路径。
