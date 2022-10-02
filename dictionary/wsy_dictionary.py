"""
date：2022年10月2日
author：wsy
target：a dictionary
"""
"""
思路：
    (1)写一个UI
    (2)存放词典
    (3)直接输入单词先搜索，如果不存在，则需要输入单词含义然后进行插入，但如果存在就直接显示单词即可
	(4)还需要考虑批量插入，因为一个一个插入也不太行，自己整理的就不太能放进去，应该写个文件读取，然后自动一个一个插入就行
"""
from tkinter import Tk,Label,Text,Button,END,StringVar
import os
import pymysql
class wsy_dictionary:
    def __init__(self):
        self.ui=Tk()
        self.tip=StringVar() # 用于用户点击按钮之后进行反馈
        # self.dictionary_path="" # 放置词典文件的绝对路径，改变想法：想直接存放到数据库中，方便查找。
        self.db=None

    def ui_design(self):
        """
        设计界面
        """
        self.ui.geometry("700x500+200+200")
        # 读取文件进行插入
        text_label=Label(self.ui,text="在下方输入要读取文件的绝对路径",font=("华文行楷",20),fg="green",bg="pink")
        text_label.pack()
        file_path_text=Text(self.ui,height=1)
        file_path_text.pack()
        file_insert_b=Button(self.ui,text="插入文本中的单词",width=20,
                    command=lambda :self.insert_word_from_text(path=file_path_text.get(1.0,END)))
        file_insert_b.pack()
        # 直接输入单词和含义进行插入
        direct_label=Label(self.ui,text="在下方输入要直接插入的单词及其词意",font=("华文行楷",20),fg="green",bg="pink")
        direct_label.pack()
        word_label=Label(self.ui,text="word:")
        word_label.pack()
        word_text=Text(self.ui,height=1)
        word_text.pack()
        meaning_label=Label(self.ui,text="meaning:")
        meaning_label.pack()
        meaning_text=Text(self.ui,height=1)
        meaning_text.pack()
        direct_insert_b=Button( self.ui,text="插入输入的单词和含义",width=20,
                    command=lambda :self.insert_direct(word=word_text.get(1.0,END),meanding=meaning_text.get(1.0,END)))
        direct_insert_b.pack()
        # 查询单词：
        search_label=Label(self.ui,text="在下方输入要进行查询的单词",font=("华文行楷",20),fg="green",bg="pink")
        search_label.pack()
        search_word_text=Text(self.ui,height=1)
        search_word_text.pack()
        search_b=Button(self.ui,text="查询上方的单词",width=20,
                    command=lambda :self.search_word(word=search_word_text.get(1.0,END)))
        search_b.pack()
        tip=Label(self.ui,textvariable=self.tip,font=("华文行楷",20),fg="green",bg="pink") # 动态变化的设置
        tip.pack()
        self.ui.mainloop()
        self.db.close() # 当界面被关闭之后在关闭数据库连接。

    def search_word(self,word):
        """
        在数据库中查询单词，该函数可以被插入函数先进行调用
        """ 
        word=word[:-1] # 去除空行
        cursor=self.db.cursor()
        query="""select meaning from my_dt where word='"""+word+"""'"""
        cursor.execute(query)
        re=cursor.fetchone() 
        cursor.close() # 查完就关闭
        if re: 
            self.tip.set(word+"："+re[0]) # 设置查询到的结果
            return "1"
        else: # 查不到返回0
            return "0"
       
    def insert_word_from_text(self,path): # 测试成功
        """
        从文本中读取单词进行插入
        """ 
        # 先检查文件是否存在：
        path=path[:-1] # 去掉输入的换行
        if not os.path.exists (path): # 存在会返回true
            print("文件不存在")
            return 
        # try:
        query="""insert into my_dt (word,meaning) values(%s,%s)""" # 插入数据的语句
        cursor=self.db.cursor() # 获取游标对象？？
        with open(path,encoding='utf-8') as f:
            while True:       
                line=f.readline()
                # 以下处理是根据自己之前记录词汇的文件来特定处理的，需根据实际需要处理的文件进行修改
                #---------------------------------------------------------------------------------
                if line.startswith("#"):
                    pass
                elif len(line)==0: # 条件更强的要放在前面
                    break
                elif len(line)<3: # 因为记录的单词中没有长度小于3的，此处处理是用来跳过空行的
                    pass
                else: # 单词或词组
                    line=line.strip()  # 此处需要具体调试看情况
                    # 插入到数据库中
                    pars=line.split(" ")
                    l=len(pars)
                    if l==2: # 表示是单词
                        values=(str(pars[0]),str(pars[1]))
                    elif l>2: # 表示是词组
                        temp=""
                        for i in range(l-1):
                            temp+=pars[i]
                            temp+=" " # 加空格
                        pars[0]=temp
                        values=(str(temp),str(pars[l-1]))
                    if self.search_word(str(pars[0]))=="1": # 表示已经存在，则跳过
                        continue
                    cursor.execute(query,values)
                    #--------------------------------------------------------------------------------
                # while line!= # 此处想实现的是一直读取到文件尾，不可直接通过空行来判断，因为有
        # except EOFError:                                                                                                                                        
        print("文本已读取完毕")     
        # 关闭游标，提交
        cursor.close()
        self.db.commit()       
        self.tip.set("文本批量插入成功！")                                                                                                                              
        # 逐行读取文件进行一些处理：比如去掉空格和空行（但是要考虑到由词组的情况），读取之后先查询是否已经存在

    def insert_direct(self,word,meanding):
        """
        插入手动输入的单词和含义
        """
        # 先查询是否已存在，如果不存在再插入
        if self.search_word(str(word))=="1":
            self.tip.set(word+"在词典中已存在")
        else:
            query="""insert into my_dt (word,meaning) values(%s,%s)""" # 插入数据的语句
            cursor=self.db.cursor()
            values=(str(word),str(meanding))
            cursor.execute(query,values)
            cursor.close()
            self.db.commit()       
            self.tip.set(word+"已成功插入到词典中！")


if __name__=="__main__":
    wd=wsy_dictionary()
    #--------db:
    wd.db=pymysql.connect(host="localhost",user="root",password="xxxx",db="dictionary") # 与数据库建立连接
    wd.ui_design()