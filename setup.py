#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: wqrf
# Mail: 1074321997@qq.com
# Created Time:  2019-10-08 14:39:00
#############################################

from setuptools import setup, find_packages

setup(
    name = "wqrf-selenium",
    version = "0.1.0",
    keywords = ("pip", "wqrf-selenium","wqrf"),
    description = "to fix find element",
    long_description = "if you can't find element,please use this",
    license = "MIT Licence",

    url = "https://github.com/Woqurefan/wqrf-selenium",
    author = "wqrf",
    author_email = "1074321997@qq.com",

    packages = [""],
    include_package_data = True,
    platforms = "any",
    install_requires = ['selenium','Levenshtein','xlrd','xlutils']
)
