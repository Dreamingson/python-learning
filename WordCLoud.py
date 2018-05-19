import jieba
import wordcloud
w = wordcloud.WordCloud(width=1000,height=700)
# width default 400
# height default 200
# min_font_size min font size default 4
# max_font_size max font size 根据高亮自动调节
# font_step 增大步长 默认为1
# font_path 指定字体文件路径 默认None
# max_words 显示最大单词量 default 200
# stop_words={} 排除词列表
# background_color

# 指定词云的形状
# from scipy.misc import imread
# mk = imread("pic.png")
# mask = mk


# w.generate("Life is short, you need python") # 向wordcloud对象中添加字符串
str = '''程序设计是给出解决特定问题程序的过程，是软件构造活动中的重要组成部分。程序设计往往以某种程序设计语言为工具，给出这种语言下的程序。程序设计过程应当包括分析、设计、编码、测试、排错等不同阶段。专业的程序设计人员常被称为程序员。
任何设计活动都是在各种约束条件和相互矛盾的需求之间寻求一种平衡，程序设计也不例外。在计算机技术发展的早期，由于机器资源比较昂贵，程序的时间和空间代价往往是设计关心的主要因素；随着硬件技术的飞速发展和软件规模的日益庞大，程序的结构、可维护性、复用性、可扩展性等因素日益重要。'''
w.generate("".join(jieba.lcut(str)))
w.to_file("outfile.png") # 将词云输出成图像文件，jpg或者png

# 配置对象参数
# 加载词云文本
# 输出词云文本
