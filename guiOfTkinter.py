#import tkinter
from tkinter import *
from easysnmp import snmp_walk






root = Tk()  # 创建窗口对象的背景色

root.geometry('500x300')

L1 = Label(root, text="ip地址")
L1.pack()
E1 = Entry(root, bd =5)
E1.pack()

L2 = Label(root, text="标识符")
L2.pack( )
E2 = Entry(root, bd =5)
E2.pack()
w = Text(root)

def requestSearch():
    stringIP = E1.get()
    stringTag = E2.get()
    community = 'public'
    res = snmp_walk(stringTag, hostname=stringIP, community=community, version=2)

    for each in res:
        oid =each.oid
        oid_index=each.oid_index
        snmp_type=each.snmp_type
        value=each.value

        print(each)
        w.insert("insert","oid=")
        w.insert("insert",oid)
        w.insert("insert", "  oid_index=")
        w.insert("insert", oid_index)
        w.insert("insert", "  snmp_type=")
        w.insert("insert", snmp_type)
        w.insert("insert", "  value=")
        w.insert("insert", value)
        w.insert("insert","\n")

def clearAll():
    w.delete('1.0', 'end')

btn1 = Button(root,text="提交请求",command = requestSearch)
btn1.pack()
btn2 = Button(root,text="清空输出",command = clearAll)
btn2.pack()

w.pack()


root.mainloop()  # 进入消息循环