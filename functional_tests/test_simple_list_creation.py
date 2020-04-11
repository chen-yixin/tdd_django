from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVistorTest(FunctionalTest):

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith听说有个很酷的在线代办事项应用
        # 她首先看了这个应用的主页
        self.browser.get(self.live_server_url)

        # 她注意到网页的标题和头部都包含"To-Do"这个词
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 应用邀请她输入一个代办事项
        inputbox = self.get_item_input_box()
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # 她在一个文本框中输入了"Buy peacock feathers" (购买孔雀羽毛)
        # Edith的爱好是使用假蝇做鱼饵钓鱼
        inputbox.send_keys('Buy peacock feathers')

        # 她安回车键后,页面更新了
        # 代办事项中显示了"1: Buy peacock feathers"
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # 页面中又出现了一个文本框,可以输入其他的待办事项
        # 她输入了"Use peacock feathers to make a fly" (使用孔雀羽毛做假蝇)
        # Edith做事很有条理
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # 页面再次更新,她的清单中显示了这两个待办事项
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # 她很满意,去睡觉了

        # Edith想知道这个网站是否会记住她的清单
        # 她看到网站为她生成了一个唯一的URL
        # 而且页面中有一些文字解说这个功能

        # 她访问那个URL,发现她的代办事项列表还在

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Edith新建一个代办事项清单
        self.browser.get(self.live_server_url)
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # 她注意到清单有个唯一的URL
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')

        # 现在有个叫做Francis的新用户访问了网站

        # 我们使用一个新浏览器会话
        # 确保Edith的信息不会从cookie中泄露出去
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis访问首页
        # 首页看不到Edith的清单
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)
        
        # Francis输入一个新的待办事项,新建一个新的清单
        # 他不像Edith那样兴趣盎然
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # Francis获得了他的唯一URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # 这个页面中还是没有Edith的清单
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        # 两人都很满意,然后去睡觉了
