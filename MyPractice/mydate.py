# Filename: mydate.py
# coding:gb2312

# import datetime
import time

print("��ǰʱ�����" + str(time.time()))
print("��ǰ���ڣ�" + str(time.ctime()))

1.���ַ�����ʱ��ת��Ϊʱ���
    ����:
        a = "2013-10-10 23:40:00"
        ����ת��Ϊʱ������
        import time
        timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")
    ת��Ϊʱ���:
    timeStamp = int(time.mktime(timeArray))
    timeStamp == 1381419600

2.�ַ�����ʽ����
    ��a = "2013-10-10 23:40:00",���Ϊ a = "2013/10/10 23:40:00"
    ����:��ת��Ϊʱ������,Ȼ��ת��Ϊ������ʽ
    timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")
    otherStyleTime = time.strftime("%Y/%m/%d %H:%M:%S", timeArray)
 
 
3.ʱ���ת��Ϊָ����ʽ����:
    ����һ:
        ����localtime()ת��Ϊʱ������,Ȼ���ʽ��Ϊ��Ҫ�ĸ�ʽ,��
        timeStamp = 1381419600
        timeArray = time.localtime(timeStamp)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        otherStyletime == "2013-10-10 23:40:00"
 
    ������:
        import datetime
        timeStamp = 1381419600
        dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
        otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
        otherStyletime == "2013-10-10 23:40:00"
 
4.��ȡ��ǰʱ�䲢ת��Ϊָ�����ڸ�ʽ
    ����һ:
        import time
        ��õ�ǰʱ��ʱ���
        now = int(time.time())  ->����ʱ���
        ת��Ϊ�������ڸ�ʽ,��:"%Y-%m-%d %H:%M:%S"
        timeArray = time.localtime(timeStamp)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
 
    ������:
        import datetime
        ��õ�ǰʱ��
        now = datetime.datetime.now()  ->����ʱ�������ʽ
        ת��Ϊָ���ĸ�ʽ:
        otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
 
5.�������ǰ��ʱ��
    ����:
        import time
        import datetime
        �Ȼ��ʱ�������ʽ������
        threeDayAgo = (datetime.datetime.now() - datetime.timedelta(days = 3))
        ת��Ϊʱ���:
            timeStamp = int(time.mktime(threeDayAgo.timetuple()))
        ת��Ϊ�����ַ�����ʽ:
            otherStyleTime = threeDayAgo.strftime("%Y-%m-%d %H:%M:%S")
    ע:timedelta()�Ĳ�����:days,hours,seconds,microseconds
 
6.����ʱ���,�����ʱ��ļ���ǰʱ��:
    timeStamp = 1381419600
    ��ת��Ϊdatetime
    import datetime
    import time
    dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
    threeDayAgo = dateArray - datetime.timedelta(days = 3)
    �ο�5,����ת��Ϊ�����������ʽ��