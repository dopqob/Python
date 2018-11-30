#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/27 19:37
# @Author  : Bilon
# @File    : wrapper.py

def getImage(function):
    @wraps(function)
    def get_ErrImage(self,*args, **kwargs):
        try:
            result = function(self,*args, **kwargs)
        except:
            timestr = time.strftime("%Y-%m-%d_%H_%M_%S")
            self.dr.get_screenshot_as_file('E:\\Appium\\Mailchat\\image\\getscreen\\%s %s.png' %
                                           (function.__name__timestr))
        else:
            logging.info (" %s 脚本运行正常" %
                (function.__name__)
                )
        return result
    return get_ErrImage


class myInitiate_addOppionTest(unittest.TestCase):

    def setUp(self):
        public.setUp.setUp(self)

    def tearDown(self):
        self.dr.quit()

    @getImage
    def test_myInitiate_addOppion(self):
        go_loginPage(self)   #访问登录页

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(myInitiate_addOppionTest)
    unittest.TextTestRunner(verbosity=2).run(suite)