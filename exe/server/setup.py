from cx_Freeze import Executable
from setuptools import setup, find_packages


build_exe_options = {
      "packages": ["common", "logs", "server", "unit_tests"]
}
setup(name='server_chat_svg',
      version='0.1',
      description='server packet',
      # packages=find_packages(),
      options={
            "build_exe": build_exe_options
      },
      executables=[Executable('server_test.py',
                             base='Win32GUI',
                             target_name='server.exe',
                             )],
      # author_email='svg95@list.ru',
      # author='Sergey Grishin',
      # install_requires=['PyQt5', 'sqlalchemy', 'pycruptodome', 'pycryptodomex']

      )
