# encoding: utf-8
"""
@author: Three
@site: 
@software: PyCharm
@file: main_excel_report.py
@time: 2017/6/9 12:45
"""

from Public.pyreport_excel import create
import os,threading,datetime
from testCase.test_case import testinterface
from Public.emmail import  sendemali
from Public.get_excel import datacel
from Public.create_report import save_result


def start():
    starttime=datetime.datetime.now()
    m=datetime.datetime.now().strftime("%Y%m%d")
    basdir = os.path.abspath(os.path.dirname(__file__))
    listid,listkey,listconeent,listurl,listfangshi,listqiwang,listname=datacel()
    listrelust,list_fail, list_pass, list_json =testinterface()
    filepath = os.path.join(basdir + '\\test_Report\\%s-result.xls'%m)
    if os.path.exists(filepath) is False:
        os.system(r'touch %s' % filepath)
    save_result(starttime, len(listrelust), ((list_pass)), list_fail)
    create(filename=filepath,list_fail=list_fail, list_pass=list_pass, list_json=list_json, listurls=listurl,
           listkeys=listkey,listconeents=listconeent, listfangshis=listfangshi, listqiwangs=listqiwang,
           listids=listid, listrelust=listrelust, listnames=listname)


def teThread():
    st = datetime.datetime.now()
    m = threading.Thread(target=start, args=())
    m.run()
    end = datetime.datetime.now()
if __name__ == '__main__':
    teThread()