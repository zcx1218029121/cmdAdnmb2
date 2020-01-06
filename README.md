# cmdAdnmb2
命令行 刷a岛工具

非常简陋的代码 

抓包了安卓绿岛
## 需要安装的库和环境
### python 3.0
Python 3.0 及以上
### requests 库
 ```python
    pip install requests
```
## 如何使用

##$ 0. win环境下可以直接
[下载]("https://github.com/zcx1218029121/cmdAdnmb2/releases").
### 1. 添加模块到python环境
 修改src/App.py

```python
    sys.path.append('clone的位置/cmdAdnmb2')
```
### 2. 启动
cd 到src 文件夹下
 ```python
python3 App.py
``` 

## 运行效果

###  选择板块
![选择板块](https://s2.ax1x.com/2020/01/02/ltRtUS.png)
时间线板块需要 登录
### 板块页
![板块也](https://s2.ax1x.com/2019/12/30/lMRkUx.png)
### 详情页
![详情页](https://s2.ax1x.com/2019/12/30/lM2REt.png)
### 回复页
![avatar](https://s2.ax1x.com/2020/01/02/lYFL8g.png)
1. 在板块页 进行回复就是发串到当前板块
2. 需要填写饼干


## 操作 
 ### n 
  下一页 
 ### pb 
  返回上一页 ,如果页面栈为空 就退出程序
 ### b 上一页 
  上一分页 如果缓存不为空就显示缓存 
 ### 1 2 3 4 5 6 
  进入对应index的串
 
 
### 回复 re:回复的内容 
    （需要在src/config/Config 填写cookies）
    
### 辣眼睛警告
    1. 用Javaer的思维方式写的Python.简单的功能有点过度设计
    2. 代码水平捉急 辣眼睛请见谅. 
### todo 
- [x] 读取json 配置
- [x] 选择板块
- [ ] 收藏串
- [ ] 岛内颜文字复制
- [ ] go:指定串跳转
    
