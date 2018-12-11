#-*- coding:utf-8 -*-
#从获取的scan话题信息中提取数据
import sys
import re
def main(lyfile):
    try:
        f=open(lyfile,'r')
        ref=open('/home/ros/image1.txt','w')
        lyf=f.read()
        pattern=r'rate: .*'
        refind=re.findall(pattern,lyf)
        for i in range(len(refind)):
            a=refind[i].split('rate: ')
            b=a[1]
            ref.write(b+'\n')
            
    except:
        print 'error occurs while reading file'
    finally:
        f.close()
        ref.close()
        print 'Success!'
if __name__ == '__main__':
    if len(sys.argv) == 2:
        lyfile=sys.argv[1]
        main(lyfile)
    else:
        print 'useage: python reloadips.py filename'
        sys.exit(1)
