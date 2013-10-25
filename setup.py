#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name="libnimbits",
      py_modules=['nimbits'],
      version="0.1",
      description="Python library for Nimbits.com",
      license="MIT",
      author="Andrea Stagi",
      author_email="stagi.andrea@gmail.com",
      url="https://github.com/astagi/libnimbits",
      keywords= "nimbits raspberry domotics",
      install_requires=[
        "requests",
      ],
      zip_safe = True)