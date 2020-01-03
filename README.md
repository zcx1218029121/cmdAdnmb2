# cmdAdnmb2
命令行 刷a岛工具

非常简陋的代码 

抓包了安卓绿岛
## 需要安装的库和环境
### python 3.0

### requests 库
 ```python
    pip install requests
```
## 如何使用
### 添加模块到python环境
修改src/App.py

 ```python
sys.path.append('clone的位置/cmdAdnmb2')
```
### 启动
cd 到src 文件夹下
 ```python
python3 App.py
```

win的也可以直接 下载打包好的exe文件 在命令行里面运行 


###  选择板块
![avatar](https://s2.ax1x.com/2020/01/02/ltRtUS.png)
时间线板块需要 登录

### 板块页
![avatar](https://s2.ax1x.com/2019/12/30/lMRkUx.png)
### 详情页
![avatar](https://s2.ax1x.com/2019/12/30/lM2REt.png)
### 回复需要饼干 
![avatar](https://s2.ax1x.com/2020/01/02/lYFL8g.png)
## 操作 
 ### n 下一页
 ### pb 返回上一页
 ### b 上一页 (默认缓存10页)
 ### 1 2 3 4 5 6 进入对应index的串
 
 
 ### 回复 re:回复的内容 
    （需要在src/config/Config 填写cookies 可以把二维码导出 用https://cli.im/deqr扫描文字）


### 辣眼睛警告
    1. 用Javaer的思维方式写的Python.简单的功能有点过度设计
    2. 代码水平捉急 辣眼睛请见谅. 
### todo 
- [x] 读取json 配置
- [x] 选择板块
- [ ] 收藏串
- [ ] 岛内颜文字复制
- [ ] go:指定串跳转
    
