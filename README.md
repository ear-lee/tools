# tools
python

## logger  
日志模块，可指定log位置、log文件名称、log level、或者直接设置autopath为True，自动向上追踪最近的log文件夹。切记把logger.py 内的root_path通过项目setting加载进来！   
引用示例：
```
from logger import get_logger
logger = get_logger()
logger.info('info message')
```

## 其他常用且需要二次封装的python模块，会持续更新……
