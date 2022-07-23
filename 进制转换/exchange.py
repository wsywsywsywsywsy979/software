"""
    author：wsy
    data:2022-6-13
    target:Conversion between computer unit base
"""
if __name__=="__main__":
    base=['bit','Byte','KB','MB','GB','TB','PB','EB','ZB','BB']
    while True:
        c=input("停止程序输入-1，否则输入其他:")
        if c=="-1":
            break;
        from_num=float(input("请输入原始数量(可为小数):"))
        from_base=int(input("请输入原始单位对应的编号(0(bit),1(Byte),2(KB),3(MB),4(GB),5(TB), 6(PB), 7(EB),8(ZB),9(BB)):"))
        to_base=int(input("请输入想要转换的单位编号(编号对应同上):"))
        if from_base==to_base:
            print(str(from_num)+str(base[from_base])+"=",str(from_num)+str(base[to_base]))
        elif from_base<to_base:
            tmp=from_base
            target_num=from_num
            if from_base==0:
                target_num/=8
                tmp+=1
            while tmp<to_base:
                target_num/=1024
                tmp+=1
            print(str(from_num)+str(base[from_base])+"="+str(target_num)+str(base[to_base]))
        elif from_base>to_base:
            tmp=from_base
            target_num=from_num
            while tmp>to_base and tmp>1:
                target_num*=1024
                tmp-=1
            if to_base==0:
                target_num*=8
            print(str(from_num)+str(base[from_base])+"="+str(target_num)+str(base[to_base]))