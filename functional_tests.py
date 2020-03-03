from selenium import webdriver
import unittest


class NewVistorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith听说有个很酷的在线代办事项应用
        # 她首先看了这个应用的主页
        self.browser.get('http://localhost:8000')

        # 她注意到网页的标题和头部都包含"To-Do"这个词
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the tests!')

        # 应用邀请她输入一个代办事项
        # 她在一个文本框中输入了"Buy peacock feathers" (购买孔雀羽毛)
        # Edith的爱好是使用假蝇做鱼饵钓鱼

        # 她安回车键后,页面更新了
        # 代办事项中显示了"1: Buy peacock feathers"

        # 页面中又出现了一个文本框,可以输入其他的待办事项
        # 她输入了"Use peacock feathers to make a fly" (使用孔雀羽毛做假蝇)
        # Edith做事很有调理

        # 页面再次更新,她的清单中显示了这两个待办事项

        # Edith想知道这个网站是否会记住她的清单
        # 她看到网站为她生成了一个唯一的URL
        # 而且页面中有一些文字解说这个功能

        # 她访问那个URL,发现她的代办事项列表还在

        # 她很满意,去睡觉了


if __name__ == "__main__":
    unittest.main(warnings='ignore')