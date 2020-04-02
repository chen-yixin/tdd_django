from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith访问首页,不小心提交了一个空的待办事项
        # 输入框中没输入内容,她按下了回车键

        # 首页刷新了,显示一个错误消息
        # 提示代办事项不能是空

        # 她输入了一些文字,然后再提交,这次没有问题了

        # 她有点儿调皮,又提交了一个空待办事项

        # 在清单页面她看到了一个类似的错误消息

        # 输入文字后就没有问题了
        self.fail('write me')
