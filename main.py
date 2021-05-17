# This is a sample Python script.
from easysnmp import snmp_walk
import  tkinter
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

device_ip = '127.0.0.1'
community = 'public'
# oid = 'IF-MIB::ifDescr'
oid = '1.3.6.1.2.1.2.2.1.1'
def test():
    res = snmp_walk(oid, hostname=device_ip, community=community, version=2)

    for each in res:
        print(each)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    test()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
