# encoding:utf-8
# author:zee
from pyecharts import Bar
'''
可以画的图有：
Bar(柱状图/条形图),Bar3D(3D柱状图),Boxplot(箱形图),EffectScatter(带有涟漪特效动画的散点图),Funnel(漏斗图),
Gauge(仪表图),Geo(地理坐标图),Graph(关系图),HeatMap(热力图),Kline(K线图),
Line(折线图),Line3D(3D折线图),Liquid(水球图),Map(地图),Parallel(平行坐标图),Pie(饼图),
Polar(极坐标图),Radar(雷达图),Sankey(桑基图),Scatter(散点图),ThemeRiver(主题河流图),WordCloud(词云图)
'''
bar = Bar("超市一周销量","模拟")
bar.use_theme('dark')
# 添加图表的数据
bar.add("日用品",["粮面类","饮料类","衣服类","文具类","烟酒类","水果类"],[40,90,30,10,60,70],is_more_utils=True)
bar.render(r"D:/my_first_chart.html")