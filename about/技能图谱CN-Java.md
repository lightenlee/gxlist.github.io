# 基础

## 精通多线程

### 线程状态

新建、阻塞、就绪、运行、死亡。

阻塞包括：等待阻塞、同步阻塞、其他阻塞。

### 线程池

Executor类创建线程池，有4种：newCachedThreadPool, newFixedThreadPool, newScheduledThreadPool, newSingleThreadPool.

newCachedThreadPool

### Synchronized 类



## 精通集合

## 精通NIO

## 精通Netty（源码）

## 精通设计模式

## 精通JVM原理

### 虚拟机结构

程序计数器、栈、本地栈、堆、元空间。

### 对象结构



### 类加载机制

类加载的顺序为：加载、连接、初始化，加上使用和卸载，则构成类的生命周期。

加载时，通过类名获取二进制流，解析到方法区，并创建类的实例。

连接包括验证、准备和解析。验证是验证类文件的格式正确。准备阶段为类的静态变量分配内存，并初始化为默认值。解析阶段将符号引用转化为直接引用。

初始化时，执行\<clinit\>方法，执行静态变量的赋值和静态代码块。

使用时，执行\<init\>方法，执行非静态变量的赋值和构造代码块，以及构造函数。

卸载时，回收类的实例，类对象，以及加载器类。

### 垃圾回收

确定对象可回收的方法：

1. 引用计数法不能解决循环引用的问题。

2. 枚举根节点，做可达性分析。

根节点包括：方法区静态属性引用的对象，方法区常量池引用的对象，方法栈本地变量表引用的对象，本地方法栈引用的对象，被同步锁持有的对象，虚拟机内部的对象，以及反映虚拟机内部情况的对象等。

#### 垃圾回收算法

标记-清除、标记-整理、复制算法，分代回收算法。包括新生代和老年代，新生代通常包括Eden区和两个surviver区，空间比例是8:1:1。

临时产生大量新对象，那么可以设置较大的Eden区间。

每次新生代回收，对象头的分代年龄+1。

#### 垃圾收集器

对于新生代，收集器包括：Serial收集器，ParNew收集器，Parallel Scavenge收集器。

对于老年代，收集器包括：Serial Old收集器，Parallel Old收集器，CMS收集器，G1收集器。

其中，ParNew收集器只能与CMS收集器搭配。Parallel Scavenge收集器只能与Parallel Old收集器搭配。

G1收集器，把堆分为Rigion区域，扮演新生代的Eden区域和Surviver区域，以及老年代空间，作为单词回收的最小单元，避免了全局回收，因此，G1建立了可预测的停顿时间模型。通过后台维护一个优先级列表，提高了回收效率。

ZGC收集器，动态创建小中大三种容量的Rigion，使用了读屏障、染色指针和内存多重映射等技术来实现可并发的标记-整理算法。

其中，染色指针，把垃圾收集的标记信息记录到指针上，4位记录三色标记状态。

### Java内存模型

对象变量在主内存中，每个线程有独立的工作内存。虚拟机保证8种原子操作。**lock**, **unlock**, **read**, load, use, assign, store, **write**.

#### volatile关键字

保证线程可见性，禁止指令重排。

加入了内存屏障。

可用于双重校验锁的单例模式。

未声明为volatile的long类型变量在32位虚拟机的读写有线程安全问题。但64位虚拟机没有，JDK9后也没有，double类型有专门的浮点处理器专门处理，也没有这种问题。

#### 原子性

#### Synchronized关键字

底层是通过字节码指令monitorenter和monitorexit来实现的，

# 框架

## 熟练掌握Spring（源码），Spring Boot



## 熟练掌握Spring Cloud

## 熟练掌握MyBatis（源码）

## 熟练掌握Maven

# 数据

## 精通MySQL

## 精通Redis

## 熟悉消息队列

如何保证消息队列的高可用？

RabbitMQ基于主从做高可用性，有三种模式：单机模式、普通集群模式、镜像集群模式。

普通集群模式，意思就是在多台机器上启动多个 RabbitMQ 实例，每台机器启动一个。你创建的 queue，只会放在一个 RabbitMQ 实例上，但是每个实例都同步 queue 的元数据。消费的时候，实际上如果连接到了另外一个实例，那么那个实例会从 queue 所在实例上拉取数据过来。

### RocketMQ（源码）

### Kafka



## 精通Elasticsearch（源码）

# DevOps

## 熟悉Linux

## 熟悉Docker

## 熟悉Kubernetes

## 熟悉Jenkins



## 【会议通知】 面试邀约，时间：2022-08-09 10:00-11:00(UTC+08:00)，地点：CN-DG-XLBPC-F1-4F-C04R

收件箱

![img](https://lh3.googleusercontent.com/a/default-user=s40-p)

| **Meeting Book** <uMeeting@huawei.com>                       | 10:22 (0分钟前) |      | ![img](https://mail.google.com/mail/u/0/images/cleardot.gif)![img](https://mail.google.com/mail/u/0/images/cleardot.gif) |
| ------------------------------------------------------------ | --------------- | ---- | ------------------------------------------------------------ |
| 发送至![img](https://mail.google.com/mail/u/0/images/cleardot.gif) |                 |      |                                                              |

英语

中文

翻译邮件

对英语停用



| 会议主题 Subject                                           |
| ---------------------------------------------------------- |
| 面试邀约                                                   |
|                                                            |
| 会议时间 Time                                              |
| 2022-08-09 10:00-11:00(UTC+08:00)Beijing                   |
|                                                            |
| 会议地点 Location                                          |
| CN-DG-XLBPC-F1-4F-C04R                                     |
|                                                            |
|                                                            |
|                                                            |
| Welink视频会议 Welink Video Meeting                        |
| [加入会议(External)](https://welink.zhumu.com/j/172045750) |
|                                                            |
| 会议ID Meeting ID                                          |
| 0172045750                                                 |
|                                                            |
|                                                            |
|                                                            |
| 召集人 Convener                                            |
| 张元                                                       |
|                                                            |
|                                                            |