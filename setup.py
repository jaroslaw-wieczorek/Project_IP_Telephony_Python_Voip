
# import build_ui

from setuptools import setup
try:
    from pyqt_distutils.build_ui import build_ui
    cmdclass = {"build_ui": build_ui}
except ImportError:
    build_ui = None # 
    cmdclass = {}

setup(
    name="JaroEliCall",
    version="0.1",
    packages=["JaroEliCall"],
    cmdclass=cmdclass,
)




