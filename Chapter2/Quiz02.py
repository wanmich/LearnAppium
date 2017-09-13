# coding:utf-8
import os
from time import sleep

import unittest

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class SimpleAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.2'
        desired_caps['deviceName'] = 'Android Emulator'
        # desired_caps['app'] = PATH(
        #     '../../normandy_hjpc.apk'
        # ) #http://m.hujiang.com/ar_ANDROID_69/?source=PC
        # desired_caps['udid'] = 'e6a7432'
        desired_caps['appPackage'] = 'com.hujiang.normandy'
        desired_caps['appActivity'] = '.SplashActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        # end the session
        self.driver.quit()

    def test_login(self):
        print('test_login')
        sleep(3)
        home_username = self.driver.find_element_by_id('com.hujiang.normandy:id/home_username')
        #try_use = self.driver.find_element_by_id('com.hujiang.normandy:id/try_use')
        if home_username.is_displayed:
            home_username.click()
        # else:_
        # loginbtn = self.driver.find_element_by_id('com.hujiang.normandy:id/login')
        # loginbtn.click()
        # yesBtn = self.driver.find_element_by_id('android:id/button1')
        # if yesBtn.is_displayed:
        #     yesBtn.click()

        els = self.driver.find_elements_by_class_name('android.widget.EditText')
        els[0].clear()
        els[0].send_keys('appium_test_user')
        els[1].clear()
        els[1].send_keys('password')

        loginbtn2 = self.driver.find_element_by_class_name('android.widget.Button')
        loginbtn2.click()
        # errormsg = self.driver.find_element_by_accessibility_id(u'用户名密码不匹配').text
        # self.assertEqual(errormsg, u'用户名密码不匹配')

        # registerlink = self.driver.find_element_by_accessibility_id(u'注册 ')
        # trylink = self.driver.find_element_by_accessibility_id(u'试用一下 ')

        phonetab = self.driver.find_element_by_accessibility_id(u'手机快速登录')
        ntab = self.driver.find_element_by_accessibility_id(u'普通登录')

        phonetab.click()
        els1 = self.driver.find_elements_by_class_name('android.widget.EditText')
        els1[0].clear()
        els1[0].send_keys('13123456789')
        sleep(3)
        els2 = self.driver.find_elements_by_class_name('android.widget.EditText')
        els2[1].clear()
        els2[1].send_keys('123456')
        els2[2].clear()
        els2[2].send_keys('123456')
        loginbtn2.click()

        errormsg1 = self.driver.find_element_by_accessibility_id(u'动态码输入错误').text
        # self.assertEqual(errormsg1, '动态码输入错误')

        ntab.click()

        # guidskip = self.driver.find_element_by_id('com.hujiang.normandy:id/guide_skip')
        # if guidskip.is_displayed:
        #     guidskip.click()

        # home = self.driver.find_element_by_name('首页')
        # self.assertIsNotNone(home)
        # el = self.driver.find_element_by_accessibility_id('Graphics')
        # el.click()
        # el = self.driver.find_element_by_accessibility_id('Arcs')
        # self.assertIsNotNone(el)

        # self.driver.back()

        # el = self.driver.find_element_by_accessibility_id("App")
        # self.assertIsNotNone(el)

        # els = self.driver.find_elements_by_android_uiautomator("new UiSelector().clickable(true)")
        # self.assertGreaterEqual(12, len(els))

        # self.driver.find_element_by_android_uiautomator('text("API Demos")')


    # def test_signup(self):
    #     print('test_signup')

        # el = self.driver.find_element_by_accessibility_id('Graphics')
        # el.click()

        # el = self.driver.find_element_by_accessibility_id('Arcs')
        # el.click()

        # self.driver.find_element_by_android_uiautomator('new UiSelector().text("Graphics/Arcs")')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
