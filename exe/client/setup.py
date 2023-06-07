from cx_Freeze import Executable
from setuptools import setup, find_packages


build_exe_options = {
      "packages": ["common", "logs", "client", "unit_tests"]
}
setup(name='client_chat_svg',
      version='0.1',
      description='Client packet',
      # packages=find_packages(),
      options={
            "build_exe": build_exe_options
      },
      executables=[Executable('client_test.py',
                             base='Win32GUI',
                             target_name='client.exe',
                             )],
      # author_email='svg95@list.ru',
      # author='Sergey Grishin',
      # install_requires=['PyQt5', 'sqlalchemy', 'pycruptodome', 'pycryptodomex']

      )
