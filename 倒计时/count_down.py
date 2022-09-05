"""
create date：2022年9月5日
author: wsy
target：实现一个自己的倒计时器
"""
"""
初步设计思路：
    输入目标日期，以及日期的含义
    程序自动获取当天日期，并进行计算显示天数：距离“含义”还剩“”天
    数字单独放在一个组件中，放大
实际实现：
    可能需要看一下软件工程中对于thinker的使用
    设置哆啦A梦背景
"""
from tkinter import StringVar, Tk,Label,Text,Button,END
import datetime
class count_down:
    def __init__(self):
        self.ui=Tk()
        self.meaning=StringVar()
        self.days=StringVar()
        self.ui_design()

    def ui_design(self):
        """
        简单设计UI
        """
        self.ui.geometry("300x300+200+200") # 对应的格式为宽乘以高加上水平偏移量加上垂直偏移量
        title_ui=Label(self.ui,text="倒计时--To wsy",font=("华文行楷",20),fg="green",bg="pink")
        title_ui.pack()#调用pack方法将label标签显示在主界面
        # 设置输入 ：
        target_date=Label(self.ui,text="目标日期（格式：xxxx xx xx）")
        target_date.pack()
        target_date_text=Text(self.ui,height=1) # 用于用户自己输入日期
        target_date_text.pack()
        meaning=Label(self.ui,text="日期含义")
        meaning.pack()
        meaning_text=Text(self.ui,height=1) # 用于用户自己输入日期
        meaning_text.pack()
        submit=Button(self.ui,text="设置完成",width=20,
                    command=lambda :self.show(date_string=target_date_text.get(1.0,END),meaning_string=meaning_text.get(1.0,END)))
        submit.pack()
        label1=Label(self.ui,text="距离")
        label1.pack()
        meaning_label=Label(self.ui,textvariable=self.meaning,font=("华文行楷",20),fg="green",bg="pink")
        meaning_label.pack()
        label2=Label(self.ui,text="还剩")
        label2.pack()
        date_label=Label(self.ui,textvariable=self.days,font=("华文行楷",20),fg="green",bg="pink")
        date_label.pack()
        label3=Label(self.ui,text="天")
        label3.pack()
        self.ui.mainloop()

    def show(self,date_string,meaning_string):
        """
        设置日期之后更新显示
        """
        # 获取当前日期计算距离天数：
        meaning_string=meaning_string.replace('\n', '').replace('\r', '')
        self.meaning.set(meaning_string)
        today=datetime.date.today()
        par1=date_string.split(" ")
        par1[2]=par1[2].replace('\n', '').replace('\r', '')
        target_date= datetime.date(int(par1[0]),int(par1[1]),int(par1[2]))
        interval=target_date-today
        # print(interval)
        self.days.set(int(interval.days))

if __name__=="__main__":
    cd=count_down()