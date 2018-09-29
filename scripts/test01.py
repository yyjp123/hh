import allure
import pytest


class Test01():
    @allure.step("1被执行")
    def test01(self):
        print("1被执行")
    @allure.step("2被执行")

    def test02(self):
        allure.attach("")
        print("2被执行")
        allure.attach("")

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test03(self):
        print("3被执行")