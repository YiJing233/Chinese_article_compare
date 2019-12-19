# -*- coding: utf-8 -*-
'''
海量文章查重脚本，

海量比对文章的相似度
这个算法对文字量比较大的文章，查询相似度，还是比较准的，
大于10 的(精度可以根据自己需要，一半设置为3，那是非常精确了)，为不相似，否则为极度相似。

但是对于那种只摘抄了一部分的，相似度查询，很差
如果要根据段落来，甚至是句子来，也可以，但是工作量就比较大了，
也每一句话都存一个simhash。.这样就可以做到按照句子来比对了。

'''
import jieba
import jieba.analyse
import numpy as np
import re

def calc_simhash(content):
    '''
    对一个文章，计算出他的simhash
    :param content:
    :return:
    '''

    # 结巴分词
    seg = jieba.cut(content)
    # 设置结巴的stopwords， 就是不需要进行处理或者是不重要的 string
    jieba.analyse.set_stop_words('./src/stopwords.txt')
    # 使用 extract 算法，计算出关键词和 关键词得分（权重）
    keyWord = jieba.analyse.extract_tags('|'.join(seg), topK=25, withWeight=True, allowPOS=())
    keyList = []
    for feature, weight in keyWord:
        weight = int(weight * 100)
        # 关键词hash化， 转化成 1和0
        feature = string_hash(feature)
        temp = []
        for i in feature:
            if(i == '1'):
                temp.append(weight)
            else:
                temp.append(-weight)
        # 计算每一个关键词的最终得分
        keyList.append(temp)
    print ('')
    # 计算整个文章中，找出的关键词（文中设置的是100），的得分相加
    list1 = np.sum(np.array(keyList), axis=0)

    if(keyList==[]): #编码读不出来
        return '00'
    simhash = ''
    for i in list1:
        if(i > 0):
            simhash = simhash + '1'
        else:
            simhash = simhash + '0'
    return simhash


def string_hash(source):  # 局部哈希算法的实现
    if source == "":
        return 0
    else:
        # ord()函数 return 字符的Unicode数值
        x = ord(source[0]) << 7
        m = 1000003  # 设置一个大的素数
        mask = 2 ** 128 - 1  # key值
        for c in source:  # 对每一个字符基于前面计算hash
            x = ((x * m) ^ ord(c)) & mask

        x ^= len(source)  #
        if x == -1:  # 证明超过精度
            x = -2
        x = bin(x).replace('0b', '').zfill(64)[-64:]
    return str(x)

def hamming_dis(simhash1, simhash2):#计算汉明距离
    '''
    使用位运算，比较两个文章最终 关键hash
    :param simhash1:
    :param simhash2:
    :return:
    '''
    t1 = '0b' + simhash1
    t2 = '0b' + simhash2
    n=int(t1, 2) ^ int(t2, 2)
    i=0
    while n:
        n &= (n-1)
        i+=1
    return i


if __name__ == '__main__':
    simhash_1 = calc_simhash(u'''电子科技大学信息与软件工程学院



实 验 报 告



学    号      2017221103009   
姓    名       王 耀 旭       
（实验）	课程名称   面向对象程序设计   
理论教师        周 帆         
实验教师        周 帆         








电 子 科 技 大 学
实   验   报   告
学生姓名： 王耀旭   学号：2017221103009   指导教师：周帆       
实验地点： 信软楼 304     实验时间：2018/12/9
一、	实验名称：JDK使用及JAVA基础
二、	实验学时：2
三、	实验目的：熟悉JDK安装和参数方法；熟悉JAVA的基本结构和变量，数组和数据类型

四、	实验原理：
JDK 是Java开发工具包 (Java Development Kit ) 的缩写。
　　它是一种用于构建在 Java 平台上发布的应用程序、applet 和组件的开发环境。其中包括Java编辑器、JVM、大量的Java工具以及Java基础API里面是Java类库和Java的语言规范，同时Java语言的任何改进都应当加到其中，作为后续版本发布。要成为一名程序员，JDK是一种最基本的工具。
　　Java SDK最早叫Java Software Develop Kit，后来改名为JDK，即Java Develop Kit。JDK作为Java开发工具包，主要用于构建在Java平台上运行的应用程序、Applet 和组件等。
　　JDK的功能如下：
　　它的功能是用于构建在 Java 平台上发布的应用程序、applet 和组件的开发环境。它不提供具体的开发软件,它提供的是无论你用何种开发软件写Java程序都必须用到的类库和Java语言规范。
Java application是可独立运行的Java程序，它由一个或多个类组成，其中必须有一个类中定义了main（）方法，main（）方法就像C语言的main方法一样是Java application运行的始点。
Java applet程序是在Java兼容浏览器上执行的，它的创建和实用操作步骤 ，有别于application的操作步骤。


五、	实验内容：
1.	完成第一张习题5、6编程
2.	完成第二章习题7编程
3.	编写程序，计算一个整数的各位数字之和，例如：整数20170925，则计算并显示2+0+1+7+0+9+2+5的值
4.	打印输出斐波拉契数列
六、	实验器材（设备、元器件）：
PC机一台，eclipse
七、	实验步骤：
Win10环境下设置JDK环境





随后打开命令行进行验证JDK是否安装成功
设置JDK完成
八、	实验结果与分析（含重要数据结果分析或核心代码流程分析）
第一章
（5）	
		


		结果
		（6）
		结果
	



第二章
	（7）
	结果

第三大题
	结果
	










第四大题
	结果
	
九、	总结及心得体会：
	在学习的时候一定要专心，不会的一定要问清楚，要学会让知识为我所用。在看书的时候一定要做好标记。建议大家在上课的时候少看课本，课本要在下课的时候看特别是上课前一定要先看看课本，上课的时候呢就不要看了，不要老师讲到那个问题了你马上在书上找，这样不好，会影响你的注意力，其实还真不如注意听老师讲呢？因为你要是一边听一边看课本，你是看到了书上的答案但是老师的思路你没有听到，而要是你不看的话，你听明白了思路，一定是想迫切的看到结果，这个时候看课本才是记的最死的时候，学习要的是就是个效率。



十、对本实验过程及方法、手段的改进建议：
无

报告评分：   
指导教师签字：
''')

    simhash_2 = calc_simhash(u'''电子科技大学信息与软件工程学院



实 验 报 告



学    号    2017221005027                  
姓    名    田义会                  
（实验）	课程名称    数据库原理与应用                  
理论教师    文军                  
实验教师    河中海                  




电子科技大学教务处制表



电 子 科 技 大 学
实   验   报   告
学生姓名：田义会	学号：2017221005027    指导教师：河中海  
实验地点：信软学院楼西303     实验时间：2019.06.14
一、实验名称：图书销售管理系统数据库 SQL 应用编程
二、实验学时：4
三、实验目的：
针对图书销售管理数据库开发，了解 SQL 语言 DDL、DML、DQL 类型语句在数据库操作访问中的应用方法，培养数据库 SQL 编程访问能力。同时也掌握基本的数据库触发器、存储过程 SQL 编程方法，培养数据库后端编程能力。本实验完成图书销售管理系统数据库的 SQL 数据操作访问和后端数据处理功能。

四、实验原理：
（1）.首先对图书销售管理系统进行数据需求分析，定义组成系统数据结构的实体、实体属性以及实体之间的关系。通过建模设计工具完成系统概念数据模型设计。进一步对图书销售管理数据库进行物理模型设计，给出数据库设计方案。
（2）.基于数据库设计方案，通过 SQL 编程执行来完成对数据库的实现操作。在本实验中，使用 SQL 语句完成对数据库、关系表、索引、视图、触发器、存储过程的创建，并编写 SQL 语句对数据库表进行数据的增删查改操作，以及利用视图、存储过程、触发器实现业务数据处理。

五、实验内容：
使用 pgAdmin4 数据库管理工具对图书销售管理系统数据库进行 SQL 编程操作，并完成触发器、存储过程后端编程，具体实验内容如下:
1.	在数据库服务器中，执行 SQL 创建图书销售管理系统数据库 BookSale。
2.	在数据库 BookSale 中，执行 SQL 创建数据库表、视图、索引等对象。
3.	在数据库 BookSale 中，执行 SQL 进行数据增、删、查、改访问操作。
4.	在数据库 BookSale 中， 采用 PL/pgSQL 语言编写存储过程函数
Pro_CurrentSale，实现当日图书销售量及销售金额汇总统计。
5.	在数据库 BookSale 中，采用 PL/pgSQL 语言编写过程语句块，实现对存储过程函数 Pro_CurrentSale 的调用，并输出统计结果。
6.	在数据库 BookSale 中，采用 PL/pgSQL 语言编写编写图书销售表 Insert 触
 
发器 Tri_InsertSale，实现图书库存数据同步修改处理。
7.	在数据库 BookSale 中，对图书销售表 Insert 触发器 Tri_InsertSale 程序进行功能验证。
8.	在数据库 BookSale 中，创建存储过程函数实现图书销售数量和金额统计。

在实验计算机上，利用 pgAdmin4 数据库管理工具及 SQL、PL/pgSQL 语言，
完成图书销售管理系统数据库应用编程操作，同时记录实验过程的步骤、操作、运行结果界面等数据，为撰写实验报告提供素材。

六、实验器材（设备、元器件）：
pc 计算机、服务器以及网络环境，pc 计算机与服务器在同一局域网络。
操作系统：Windows7 / Windows XP 
管理工具： pgAdmin4
DBMS 系统： PostgreSQL 11

七、实验步骤：
1.	在数据库服务器中，采用 SQL 语句执行方式，创建图书销售管理系统数据库 BookSale。
2.	在 BookSale 数据库中，采用 SQL 语句执行方式，创建 book（图书表）、auther
（作者表）、publisher（出版社表）、stock（库存流水表）、customer（客户表）、
sale（销售表），以及各表主键外键的创建，并为给表创建索引。
3.	为 book、auther、publisher、customer 表准备样本数据，采用 SQL 语句执行方式，将样本数据插入到表中。采用 SQL 语句对 book、auther、publisher、
customer 表进行数据修改、删除、查询、统计等访问操作。
4.	创建视图 BOOK_AUTHER_PUBLISHER，该视图查询数据库，输出图书名、作者、出版社以及图书价格等数据。对视图 Book_View 进行数据查询访问操作。
5.	编写触发器函数，实现在 sale 表数据插入时，级联操作 stock 表，将图书的库存流水进行记录，同时级联更新 book 表中对应图书的库存数据。
6.	创建完触发器函数之后，创建相对应的触发器，实现上一步中提到的功能。
7.	测试触发器的功能，准备 sale 表的样本数据，并将其插入sale 表，插入之后查看 stock 表是否有对应的更新，并对比插入 sale 数据前后 book 中对应数据的修改情况。
8.	编写存储过程函数，实现统计某日图书的销售总量以及总金额数据。
9.	调用存储过程函数，查看输出结果是否准确实现业务数据处理功能。

八、实验结果与分析（含重要数据结果分析或核心代码流程分析）
1.创建 BookSale 数据库
SQL 语句：create database "BookSale"

运行结果：

 
2.	创建各数据库表

SQL 语句：
create table Auther (
AU_ID	CHAR(18)	not null,
AU_Name	VARCHAR(20)	not null,
 
AU_Gender	CHAR(2)	not null,
AU_Phone	VARCHAR(11)	not null,
AU_Address	VARCHAR(50)	not null, constraint PK_AUTHER primary key (AU_ID)
);
create table Book (

Book_ISBN
AU_ID	CHAR(13)
CHAR(18)	not null,
null,
PUB_ID	CHAR(11)	null,
Book_Name	VARCHAR(50)	not null,
Book_Pubdate	DATE	not null,
Book_Price	MONEY	not null,
Book_Category	VARCHAR(20)	not null,
Book_Stock	INT4	not null,
Book_Notes	VARCHAR(100)	null,
Book_List	VARCHAR(100)	null,
constraint PK_BOOK primary key (Book_ISBN)
);
create table CUSTOMER (
CUST_ID	CHAR(18)	not	 null,
CUST_Name	VARCHAR(20)	not 	null,
CUST_Phone	VARCHAR(15)			not null, CUST_Address    	VARCHAR(50)     		not null, 
CUST_Email	VARCHAR(50) 			not null, 
constraint PK_CUSTOMER primary key (CUST_ID)
);
create table Publisher (
PUB_ID	CHAR(11)	not null,
PUB_Name	VARCHAR(20)          not null,
PUB_Phone	VARCHAR(15) 			not null, 
PUB_Address     	VARCHAR(50)     		not null, 
constraint PK_PUBLISHER primary key (PUB_ID)
);
create table Sale (

SALE_ID	VARCHAR(11)	not null,
Book_ISBN	CHAR(13)	null,
CUST_ID	CHAR(18)	null,
SALE_Date	DATE	not null,
SALE_QTY	INT4	not null,
SALE_Amount	MONEY	not null,
constraint PK_SALE primary key (SALE_ID)
);
create table Stock (
Stock_ID	VARCHAR(10)	not null,
 
Book_ISBN	CHAR(13)	null,
Stock_Change	INT4	not null,
Stock_Operation	CHAR(4)	not null,
Stock_Datetime	DATE	not null,
constraint PK_STOCK primary key (Stock_ID)
);

运行结果：
 
 
 
 
 
 
3.	创建数据库表中主外键和索引
alter table Book
add constraint FK_BOOK_BOOK_AUTH_AUTHER foreign key(AU_ID) 
references Auther (AU_ID)
on delete restrict on update restrict; 
alter table Book
add constraint FK_BOOK_BOOK_PUBL_PUBLISHE foreign key (PUB_ID) references Publisher (PUB_ID)
on delete restrict on update restrict; 
alter table Sale
add constraint FK_SALE_BOOK_SALE_BOOK foreign key (Book_ISBN) 
references Book (Book_ISBN)
on delete restrict on update restrict;
 alter table Sale
add constraint FK_SALE_CUSTOMER CUSTOMER foreign key (CUST_ID) 
references CUSTOMER (CUST_ID)
on delete restrict on update restrict; 
alter table Stock
add constraint FK_STOCK_BOOK_STOC_BOOK foreign key (Book_ISBN) 
references Book (Book_ISBN)
on delete restrict on update restrict;

运行结果：

 
4.	插入样本数据并对 publisher 表进行增删查改操作
（1）执行 SQL 语句，插入样本数据到图书销售数据库
Insert into Auther values('330309198504150527','吴欣怡','女','13557869867','重庆市万州区人民北路二段九号');
Insert into Auther values('540135199103281548','杨金鱼','男','15558324519','江苏省无锡市天路区白草二十八号');
Insert into Auther values('120857198811123587','朱洁','女','18028975670','北京市朝阳区智学巷六号');
Insert into PUBLISHER values('PUB00000001','高等教育出版社','010-65321854','北京'); 
Insert into PUBLISHER values('PUB00000002','电子工业出版社','010-65329857','北京'); 
Insert into PUBLISHER values('PUB00000003','人民邮电出版社','010-65325987','北京');
Insert into BOOK values('9787115502742','330309198504150527','PUB00000001','Web 前端开发最佳实践','2016-01-01', '59','IT 技术','100');
Insert into BOOK values('9875325415577','540135199103281548','PUB00000002','Java EE Web 编 程','2008-01-01', '52','IT 技术','200');
Insert into BOOK values('9865365975234','120857198811123587','PUB00000003',' 数 据 库 实 验 指 导','2013-08-1','29','IT 技术', '150');
Insert into customer values('680554199207120325','林一','15963512578','四川省成都市成华区建设北路二段十一号','450448745@qq.com');
Insert into customer values('345021198608120258','黄三','18636598574','浙江省杭州市天路区梅田路二十九号','657873215@qq.com');
Insert into customer values('542244197812121687','玛丽','13615869875','北京市朝阳区梅山路二巷十六号','647864378@qq.com');


运行结果：

 
（2）查看 publisher 表数据
select * from publiser;

运行结果：
 
（3）增加一条数据到 publisher 表
SQL 语 句 ： Insert into PUBLISHER values('PUB00000004',' 清 华 大 学 出 版 社
','010-65323169','北京');


运行结果：
 
（4）删除一条 publisher 表数据
SQL 语句：delete from publisher where pub_id = 'PUB00000004';


运行结果：
 
 
（5）修改一条 publisher 表数据
SQL 语句：update publisher set pub_address = '南京' where pub_id = 'PUB00000003';

运行结果：
 
 
5.	创建视图
SQL 语句如下：
create view BOOK_AUTHER_PUBLISHER as
select B.book_name as "图书",AU.au_name as "作者",PU.pub_name as "出版社",B.book_price as "图书价格" from book as B join auther as AU on B.au_id = AU.au_id join publisher as PU on B.pub_id = PU.pub_id

运行结果：
 
6.视图数据查询
SQL 语句： select * from BOOK_AUTHER_PUBLISHER; 

运行结果：
 
7.创建触发器函数
SQL 语句：
CREATE OR REPLACE FUNCTION InsertSale() RETURNS TRIGGER AS $$ BEGIN
IF (TG_OP = 'INSERT') THEN
INSERT INTO stock values(new.sale_id,new.book_isbn,new.sale_qty,' 出 库 ',new.sale_date); update book set book_stock = book_stock - new.sale_qty where book.book_isbn =
new.book_isbn;
RETURN NEW;
END IF; RETURN NULL;
END;
$$ LANGUAGE plpgsql;

运行结果：
 
8.创建触发器
SQL 语句：
CREATE TRIGGER Tri_InsertSale AFTER INSERT ON SALE
FOR EACH ROW EXECUTE PROCEDURE InsertSale();


运行结果：
 
9.测试触发器
 SQL 语句：
Insert into sale values('SA00001','9787115502742','680554199207120325','2019-06-21',15,'799'); 
Insert into sale values('SA00002','9875325415577','345021198608120258','2019-06-21',20,'10408';
Insert into sale values('SA00003','9865365975234','542244197812121687','2019-06-21',50,'1360';

运行结果：
 
10.查看 stock 表数据以及对比 book 表数据
SQL语句：SELECT * FROM public.stock

运行结果：
 
SELECT * FROM public.book
 
11.创建存储过程
SQL语句：
CREATE OR REPLACE FUNCTION countsale(OUT amount int,OUT allmoney money) as $count$ 
BEGIN
	select sum(sale_qty) into amount FROM sale WHERE sale_date = '2019-06-21'; 
	select sum(sale_amount) into allmoney FROM sale WHERE sale_date = '2019-06-21';
END;
$count$ LANGUAGE plpgsql;

运行结果：
 
12.调用存储过程
SQL语句：Select * from countsale()

运行结果：
 


九、总结及心得体会：
这次实验让我更加熟练的使用PostgreSQLAdmin4,以及SQL 语言 DDL、DML、DQL 类型语句在数据库操作访问中的应用，提高了数据库 SQL 编程访问能力。同时我也掌握了基本的数据库触发器、存储过程 SQL 编程，提高了我数据库后端编程能力。

十、对本实验过程及方法、手段的改进建议：

                                                     报告评分：   
                                      指导教师签字：
 
电 子 科 技 大 学
实   验   报   告
学生姓名：田义会	学号：2017221005027    指导教师：河中海  
实验地点：信软学院楼西303     实验时间：2019.06.14
一、实验名称：图书销售管理系统数据库安全管理

二、实验学时：4

三、实验目的：

了解 DBMS 系统对数据库管理的内容与方法，特别是理解数据库安全机制和作用，以及 PostgreSQL 数据库角色管理、用户管理、权限管理的基本方法，培养数据库管理能力。在图书销售管理系统数据库中，创建必要的角色和用户，并完成上述角色与用户的权限管理。

四、实验原理

1.设计数据存取权限控制模型，对各角色进行不同权限的赋予，保证数据库数据的安全性。
2.使用 SQL 语句进行角色、用户的创建、对角色进行权限赋予、对用户分派角色。
3.使用不同的用户登录时，就拥有了该用户的权限，在对数据库表进行操作的时候就会受到不同程度的制约。
五、实验内容

使用 pgAdmin4 数据库管理工具对图书销售管理系统数据库进行数据库安全管理，具体实验内容如下:
1.	针对图书销售管理系统数据库，设计数据存取权限控制模型。
2.	在数据库中，创建客户（R_Customer）、商家（R_Seller）角色。
3.	在数据库中，根据业务规则为客户（R_Customer）、商家（R_Seller）角色赋	予数据库对象权限。
 
4.	在数据库中，分别创建客户用户 U_Customer、商家用户 U_Seller。
5.	分别为客户用户 U_Customer、商家用户 U_Seller 分派客户（R_Client）、商	家（R_Seller）角色。
6.	分别以客户用户 U_Customer、商家用户 U_Seller 身份访问图书销售管理	数据库，验证所实现数据存取权限控制模型的正确性。
在实验计算机上，利用pgAdmin4 数据库管理工具及SQL 语句，完成图书销售管理系统数据库安全管理，同时记录实验过程的步骤、操作、运行结果界面等数据，为撰写实验报告提供素材。
六、实验设备及环境

“数据库原理及应用”实验所涉及的机房硬件设备为 pc 计算机、服务器以及网络环境，pc 计算机与服务器在同一局域网络。
操作系统： Windows7 / Windows XP 管理工具： pgAdmin4
DBMS 系统： PostgreSQL 11

七、实验步骤

1.	针对图书销售管理系统，在设计数据存取权限控制模型。
2.	在 pgAdmin4 中的 BookSale 数据库中， 使用 SQL 语句创建客户
（R_Customer）角色、商家（R_Seller）角色。
3.	在 pgAdmin4 中， 根据第一步设计的数据存取权限控制模型对客户
（R_Customer）角色、商家（R_Seller）角色赋予所定义的数据库对象权限。
4.	在 pgAdmin4 中，分别创建客户用户 U_Customer、商家用户 U_Seller，并为客户用户分配客户角色，为商家用户分配商家角色。
5.	分别以客户用户 U_Customer、商家用户 U_Seller 身份访问图书销售管理数据库，并分别以这两个用户对各数据库表进行操作，以验证是否正确分配了两用户不同的角色权限。


八、实验数据及结果分析

1.	针对图书销售管理系统，设计数据存取权限控制模型。


图 2-1 客户角色安全模型


 

2.	创建客户角色
 
图 2-2 商家角色安全模型
 
SQL语句：
CREATE ROLE "R_Customer"	WITH LOGIN
NOSUPERUSER NOCREATEDB NOCREATEROLE NOINHERIT NOREPLICATION CONNECTION LIMIT -1

运行结果：
 
3.	创建商家角色 
SQL语句：
CREATE ROLE "R_Seller"	WITH LOGIN
NOSUPERUSER NOCREATEDB NOCREATEROLE NOINHERIT NOREPLICATION CONNECTION LIMIT -1

运行结果：
 

4.	赋予客户角色权限
SQL语句：
GRANT  SELECT ON book TO "R_Customer";
GRANT SELECT ON auther TO "R_Customer"; GRANT  SELECT ON publisher TO "R_Customer";

运行结果：
 
5.赋予商家角色 
SQL语句：
GRANT SELECT,INSERT,UPDATE,DELETE ON book TO "R_Seller"; GRANT SELECT,INSERT,UPDATE,DELETE ON auther TO "R_Seller"; GRANT SELECT,INSERT,UPDATE,DELETE ON publisher TO "R_Seller";
GRANT SELECT ON stock TO "R_Seller";
GRANT SELECT,INSERT,UPDATE,DELETE ON sale TO "R_Seller"; GRANT SELECT,INSERT,UPDATE,DELETE ON customer TO "R_Seller";

运行结果：
 
6.创建客户用户和商家用户，并将客户角色和商家角色赋予他们
SQL语句:
CREATE USER "U_Customer" WITH LOGIN
CONNECTION LIMIT -1
IN ROLE "R_Customer" PASSWORD '123456';
 

CREATE USER "U_Seller" WITH LOGIN
CONNECTION LIMIT -1
IN ROLE "R_Seller" PASSWORD '123456';

运行结果：
 



7.用客户用户登录数据库，并进行操作来验证是否赋予权限成功。
	

	



图 2-10  登录客户用户
 
测试一：查看 book 表
SQL 语句：select * from book
运行结果：
 
测试二：删除 book 表中的数据
SQL 语句：delete from book where book_isbn = '9787115502742'

运行结果：
 

测试三：查看 auther 表
SQL 语句：select * from auther
运行结果：
 

测试四：插入一条数据到 auther 表中
SQL 语句：insert into auther values('330304198802150325','李天','男','12365748953','北京市产阳区李二路 18555 号')
运行结果：
 
测试五：查看 sale 表
SQL 语句：select * from sale
运行结果：
 
8.用商家用户登录数据库，并进行操作来验证是否赋予权限成功。



 





 
测试一：查看 customer

 
SQL 语句：select * from customer
运行结果：
 

测试二：插入一条数据到 auther 中
SQL 语句：insert into auther values('330304198802150325','李天','男','12365748953','北京市产阳区李二路 18555 号')
运行结果：
  

测试三：从 stock 表中删除一条数据
SQL 语句：delete from stock where stock_id = 'SA00001'
运行结果：
 

测试四：更新 sale 表的一条数据
SQL 语句：UPDATE sale SET sale_date = '2019-05-21' WHERE sale_id = 'SA00001'
运行结果：
 
 


九、总结及心得体会
了解 了DBMS 系统对数据库管理的内容与方法，特别是理解数据库安全机制和作用，以及 PostgreSQL 数据库角色管理、用户管理、权限管理的基本方法，提高了我的数据库管理能力。

十、对本实验过程及方法、手段的改进建议：
                                                     报告评分：   
                                      指导教师签字：
 

''')

    # 计算最终差异度
    diff_value =  hamming_dis(simhash_1, simhash_2)
    print (u'差异值：  %s' % (diff_value))
    # if diff_value > 8:
    #     print u'差异值：  %s' % (diff_value)