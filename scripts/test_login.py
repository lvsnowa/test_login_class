import os, sys, pytest, time
sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.login_page import LoginPage
from base.base_analyze_yml import analyze_yml


def analyze_with_key(key):
    return analyze_yml("login_data", key)


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.login_page = LoginPage(self.driver)

    # @pytest.mark.skipif(True, reason="")
    def test_login_001(self):
        # 判断完成按钮是否可用
        assert not self.login_page.is_login_btn_enabled()

    # @pytest.mark.skipif(True, reason="")
    def test_login_002(self):
        self.login_page.input_password("xxx")
        assert not self.login_page.is_login_btn_enabled()

    # @pytest.mark.skipif(True, reason="")
    def test_login_003(self):
        self.login_page.input_username("xxx")
        assert not self.login_page.is_login_btn_enabled()

    # @pytest.mark.parametrize("param", analyze_with_key("test_login"))
    # def test_login(self, param):
    #     print(param)
    #     self.login_page.input_username(param["username"])
    #     self.login_page.input_password(param["password"])
    #     if self.login_page.is_login_btn_enabled():
    #         self.login_page.click_login_btn()
    #         self.login_page.find_toast(param["hint"])
    #         assert True
    #     else:
    #         assert False


    # @pytest.mark.skipif(True, reason="")
    # def test_login_004(self):
    #     self.login_page.input_username("hitheima@163.com")
    #     self.login_page.input_password("itheima")
    #     if self.login_page.is_login_btn_enabled():
    #         self.login_page.click_login_btn()
    #         self.login_page.find_toast("登录成功")
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skipif(True, reason="")
    # def test_login_005(self):
    #     self.login_page.input_username("hitheima@163.com")
    #     self.login_page.input_password("itheima123")
    #     if self.login_page.is_login_btn_enabled():
    #         self.login_page.click_login_btn()
    #         self.login_page.find_toast("密码错误")
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skipif(True, reason="")
    # def test_login_006(self):
    #     self.login_page.input_username("hitheima123@163.com")
    #     self.login_page.input_password("itheima")
    #     if self.login_page.is_login_btn_enabled():
    #         self.login_page.click_login_btn()
    #         self.login_page.find_toast("账号不存在")
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skipif(True, reason="")
    # def test_login_007(self):
    #     self.login_page.input_username("hitheima123@163.com")
    #     self.login_page.input_password("itheima123")
    #     if self.login_page.is_login_btn_enabled():
    #         self.login_page.click_login_btn()
    #         self.login_page.find_toast("账号不存在")
    #         assert True
    #     else:
    #         assert False
    #
    # def test_login_008(self):
    #     self.login_page.input_username("hitheima@163.com ")
    #     self.login_page.input_password("itheima")
    #     if self.login_page.is_login_btn_enabled():
    #         self.login_page.click_login_btn()
    #         self.login_page.find_toast("登录成功")
    #         assert True
    #     else:
    #         assert False
    #
    # def test_login_009(self):
    #     self.login_page.input_username(" hitheima@163.com")
    #     self.login_page.input_password("itheima")
    #     if self.login_page.is_login_btn_enabled():
    #         self.login_page.click_login_btn()
    #         self.login_page.find_toast("登录成功")
    #         assert True
    #     else:
    #         assert False

    def teardown(self):
        pass