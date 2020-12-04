# tools
python、c++

## logger  
日志模块，可指定log位置、log文件名称、log level、或者直接设置autopath为True，自动向上追踪最近的log文件夹。切记把logger.py 内的root_path通过项目setting加载进来！   
引用示例：
```
from logger import get_logger
logger = get_logger()
logger.info('info message')
```

## vscode_common
vscode的配置，用来写python和c++的，目前为mac版所以编译器选的是clang

## scheduler
基于apscheduler的定时任务，job相关请重写scheduler/scheduler/job.py，相关时间间隔配置在scheduler/scheduler/conf.py下修改，dockerfile已经准备好，可以以镜像方式在k8s、swarm等下运行，log使用本工具包中的logger，可随意替换

## 其他常用且需要二次封装的python模块，会持续更新……
