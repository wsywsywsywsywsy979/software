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
from tkinter import Tk,Label,Text,Button,END
class wsy_dictionary:
    def __init__(self) -> None:
        self.ui=Tk()
        self.dictionary_path="" # 放置词典文件的绝对路径

    def ui_design(self):
        """
        设计界面
        """
        text_label=Label(self.ui,text="在下方输入要读取文件的绝对路径",font=("华文行楷",20),fg="green",bg="pink")
        text_label.pack()
        file_path_text=Text(self.ui,height=1)
        file_path_text.pack()
        file_insert_b=Button(self.ui,text="插入文本中的单词",width=20,
                    command=lambda :self.insert_word_from_text(path=file_path_text.get(1.0,END)))
        file_insert_b
                
    def insert_word_from_text(self,path):
        """
        从文本中读取单词进行插入
        """



        


if __name__=="__main__":
    pass