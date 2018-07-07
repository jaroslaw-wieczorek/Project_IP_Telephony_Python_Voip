
# import build_ui

from setuptools import setup

try:
	from setuptools.command.build_py import build_py
	from pyqt_distutils.build_ui import build_ui

except ImportError as err:
	print(err)
	build_ui = None # 
	cmdclass = {}

class custom_build_py(build_py):
    def run(self):
        self.run_command('build_ui')
        build_py.run(self)


  
setup(
       	name="JaroEliCall",
	version="0.1",
	packages=["JaroEliCall"],
	cmdclass={
       		"build_ui": build_ui,
       		"build_py": custom_build_py,
       	}
)
   
         







