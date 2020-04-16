"""
Driver File
To be able to configure the capabilities, please go to capabilities.json file
"""

from appium import webdriver
import os
import json
import unittest


class Driver(unittest.TestCase):
    """
    Driver
    """
    @classmethod
    def start_app(cls):
        """Start the app"""
        app = os.path.abspath("./core/configs/resources/apk/SoundCloud Music Audio_v2019.07.08-release_apkpure.com.apk")
        with open("./core/configs/capabilities.json", "r") as caps_file:
            capabilities = json.load(caps_file)
        capabilities["app"] = app
        cls.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities=capabilities
        )
        return cls

    def shutdown(self):
        """
        Close and quit app
        """
        self.driver.quit()
