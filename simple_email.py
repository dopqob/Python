# !/usr/bin/env python
#  -*- coding: utf-8 -*-
#  @Time    : 2019/1/8 10:39
#  @Author  : Bilon
#  @File    : simple_email.py
import os
import mimetypes
import smtplib
from datetime import datetime
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# 获取最新报告的地址
def acquire_report_address(reports_address):
    # 获取当前年月日
    now = datetime.now().strftime('%Y-%m-%d')
    new_address = reports_address + '\\' + now

    # 测试报告文件夹中的所有文件加入到列表
    test_reports_list = os.listdir(new_address)
    # 按照升序排序生成新的列表
    new_test_reports_list = sorted(test_reports_list)
    # 获取最新的测试报告
    the_last_report = new_test_reports_list[-1]
    # 最新的测试报告的地址
    the_last_report_address = os.path.join(new_address, the_last_report)
    return the_last_report_address


# 获取附件的相关信息
def get_attach_file(attach_file):
    """
    带附件的邮件可以看做包含若干部分的邮件：文本和各个附件本身，所以，可以构造一个MIMEMultipart对象代表邮件本身，
    然后往里面加上一个MIMEText作为邮件正文，再继续往里面加上表示附件的MIMEBase对象即可，
    我们把附件那部分抽取到get_attach_file()方法中
    """
    if attach_file is not None and attach_file != '':
        try:
            with open(attach_file, 'rb') as file:
                # mimetypes是python自带的标准库，可以根据文件的后缀名直接得到文件的MIME类型
                ctype, encoding = mimetypes.guess_type(attach_file)
                if ctype is None or encoding is not None:
                    ctype = 'application/octet-stream'
                maintype, subtype = ctype.split('/', 1)
                mime = MIMEBase(maintype, subtype)
                mime.set_payload(file.read())
                # 设置信息头
                mime.add_header('Content-Disposition', 'attachment',
                                filename=os.path.basename(attach_file))
                mime.add_header('Content-ID', '<0>')
                mime.add_header('X-Attachment-Id', '0')
                # 设置编码规则
                encoders.encode_base64(mime)
                return mime
        except Exception as e:
            print('%s......' % e)
            return None
    else:
        return None


# 自动发送邮件
def send_email(new_report):
    # 读取测试报告中的内容作为邮件的内容
    with open(new_report, 'r', encoding='utf8') as f:
        mail_body = f.read()
    # 发件人地址
    from_addr = '30884413@qq.com'
    # 收件人地址
    to_addr = '1335150450@qq.com,1551658080@qq.com'
    # 发送邮箱的服务器地址
    mail_server = 'smtp.qq.com'
    # 邮件的标题
    subject = 'APP测试报告'
    # 发件人的邮箱地址
    username = '30884413@qq.com'
    password = 'latimgqpunpgcbeb'
    # 邮箱的内容和标题
    # message = MIMEText(mail_body, 'html', 'utf8')
    # message['Subject'] = Header(subject, charset='utf8')
    message = MIMEMultipart()
    message['Subject'] = Header(subject, 'utf-8')   # 邮件标题
    message.attach(MIMEText(mail_body, 'html', 'utf8'))  # 邮件主体内容
    attach_file = get_attach_file(new_report)
    message.attach(attach_file)     # 添加附件

    # 发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(mail_server)
    smtp.login(username, password)
    smtp.sendmail(from_addr, to_addr.split(', '), message.as_string())
    print("Send succeed!!")
    smtp.quit()


if __name__ == '__main__':
    # 生成测试报告并发送邮件
    # 测试报告文件夹地址
    # test_reports_address = 'F:\\python_selenium\\soft_test_selenium2.0\\test_report'
    test_reports_address = r'C:\Users\o_p_q_o\PycharmProjects\Python\ccloud\TestReport'
    # 测试用例的文件夹地址
    # test_cases_dir = r'F:\python_selenium\soft_test_selenium2.0\test_cases'
    # 获取所有的测试用例
    # test_cases = unittest.defaultTestLoader.discover(test_cases_dir, pattern='*.py')
    # 获取当前时间
    # now = datetime.now().strftime('%Y%m%d%H%MM%f')
    # 生成以当前时间命名的测试报告文件名
    # test_report_name = r'{}\report_{}.html'.format(test_reports_address, datetime.now().strftime('%Y%m%d%H%M%f'))
    # 生成以当前时间命名的测试报告文件
    # file_report = open(test_report_name, 'w', encoding='utf8')
    # 生成html形式的报告
    # runner = HTMLTestRunner(stream=file_report, title='测试报告', description='QQ登录测试报告结果：')
    # 运行
    # runner.run(test_cases)
    # 关闭打开的测试报告文件
    # file_report.close()

    # time.sleep(5)
    # 查找最新生成的测试报告地址
    new_report_addr = acquire_report_address(test_reports_address)
    # 自动发送邮件
    send_email(new_report_addr)
