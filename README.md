# TrumpTwitterAnalysis
## 推特数量、发送时间分析

### 每日发推时间分析
可以看出特朗普每日发推时间段集中在午夜之后和19：00到20：00之间
![img](./img/发推时间.png)
<br>
<br>

### 发推的增速
中后期增速变大
![img](./img/发推增速.png)
<br>
<br>
<br>

### 最高喜欢

<video style="width:100%" controls>
  <source src="./img/FraudNewsCNN FNN.mp4" type="video/mp4">
</video>

<br>
<br>
<br>

### 最高转发
![img](./img/最高喜欢.png)
<br>
<br>
<br>

### 评论中提及各国的次数
![img](./img/各国占比.png)
<br>
<br>
<br>

#### 评论中对中国的态度
![img](./img/对中国态度.png)
<br>
关键字：批评了奥巴马、布什对中国政策，声明中国在非洲的军事威胁，抵制中国货
<br>
<br>
<br>

#### 评论中对俄罗斯态度
![img](./img/对俄罗斯态度.png)
<br>
关键字：双边关系、间谍事件、Russia and the world has already started to respect us again!
<br>
<br>
<br>

#### 评论中对日本态度
![img](./img/对日本态度.png)
<br>
关键字：共建更好的军事、新PPP协定
<br>
<br>
<br>

#### 评论中对英国态度
![img](./img/对英国态度.png)
<br>
关键字：欢迎光临白宫、超级碗、英国新闻
<br>
<br>
<br>

### 代码说明
* img文件夹内分析之后媒体文件
* HTML文件夹内放置的的是用于展示的HTML文件
* data文件夹下放置爬取下来的文件，以csv格式存储，文件格式为["id","content","user_id",'user_screen_name','user_name','created_at','retweets','favorites']
* single文件夹下放入的是分离出来的data.csv文件，根据文件名可以获得相应数据

