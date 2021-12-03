# bgcp

homework for big data and cloud platform 

应课程要求将相关代码上传至 github 仓库中

## 拉取镜像

通过
`docker pull registry.cn-beijing.aliyuncs.com/nkzwchen/bgcp:1.0`
从阿里云仓库拉取镜像

## 开启集群

首先输入
`docker network create --subnet=172.20.0.0/16 hnet`
创建网络
之后再运行 start 文件夹中的 `start_cluster.sh` 文件创建集群

## 环境初始化

相关代码位于start文件夹中
通过运行`hadoop_start.sh`文件开启hadoop
通过运行`hive_start.sh`文件开启hive
通过运行`spark_start.sh`文件开启start
通过运行`data.sh`文件将 `metric.txt` 文件上传到 `hdfs://data/` 文件夹储存

## 利用hadoop 的 mapreduce 框架求平均值

相关代码位于 hadoop 文件夹中。

运行`avg.sh`文件通过 java 接口利用 hadoop 的 mapreduce 框架计算 hdfs文件存储系统中 `metric.txt`
中不同的 id 和 kpi 对应的 value 的平均值。


## 利用 hive 交互式编程求分位数

相关代码用于 hive 文件中

通过 hive 命令打开 hive 交互式输入界面，输入 hive 文件夹下的 `hive.md` 中的语句即求出不同的 id 和 kpi 对应的 value 的分位数

## 利用spark 求最大最小值

相关代码位于 spark 文件中

通过 spark-shell 交互式界面输入 spark 文件夹下的 `spark.md` 中的语句即求出不同的 id 和 kpi 对应的 value 的极值

## 利用 seaborn 库做结果的可视化展示

相关代码位于 plot 文件夹中, 修改 `plot.py` 中的 name 变量即可画出对应的 cmbd 和 kpi 的数据分布情况

