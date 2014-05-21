import sys
from setuptools import setup

version = 0.1

if not '3.3' <= sys.version <= '3.4':
    raise ImportError('python version not supported')

test_require = ['nose']
if sys.version < '3.3':
    test_require.append('elementtree')

setup(name="Zamza",
      version=version,
      description="zamza is CircuitEditor on CLI",
      author="HAYASAKA Ryosuke",
      author_email="hayasaka.ryosuke@gmail.com",
      include_package_data=True,
      test_suite="nose.collector",
      test_require=test_require,
      )
