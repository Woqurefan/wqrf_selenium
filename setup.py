#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: wqrf
# Mail: 1074321997@qq.com
# Created Time:  2019-10-08 14:39:00
#############################################

from setuptools import setup, find_packages

setup(
    name = "wqrfnium",
    version = "0.1.0",
    keywords = ("wqrf"),
    description = "to fix find element",
    long_description = "if you can't find element,please use this",
    license = "MIT Licence",
    url = "https://github.com/Woqurefan/wqrf_selenium",
    author = "wqrf",
    author_email = "1074321997@qq.com",
    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ['selenium','xlrd','xlutils']
)
