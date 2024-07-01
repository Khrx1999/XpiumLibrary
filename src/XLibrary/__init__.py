#XLibrary/__init__.py
# -*- coding: utf-8 -*-
from robot.api.deco import keyword
from .main import MainClass
from .submodule1 import XAppiumFlutter
from .submodule1 import XMongoDB
from .submodule2 import XLog
from .submodule2 import Module22


 
__all__ = [ 'XLibrary','MainClass', 'XAppiumFlutter', 'XMongoDB','XLog', 'Module22']



class XLibrary(
    MainClass,
    XAppiumFlutter, 
    XMongoDB,
    XLog,
    Module22
    ):
    """ 
    *` XLibrary `* เป็นไลบรารีที่พัฒนาขึ้นเฉพาะ เพื่อรองรับการใช้งานส่วนบุคคลในงานพัฒนา Script Automate
    """

    @keyword("Hello World")
    def TTTTTT(self):
        """ พิมพ์ข้อความ 'Hello, world!' ลงในคอนโซล """
        print("Hello, world!")

