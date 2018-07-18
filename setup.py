# import community modules.
import os
import sys
from setuptools import setup,find_packages
from setuptools.command.install import install

# custom install controller.
class _install(install):
  
  # run operations.
  def run(self):
    from subprocess32 import call
    config_dir = call(['mkdir','/etc/slen'])
    if config_dir==0:
      call(['chmod','-R','600','/etc/slen'])
    install.run(self)

if __name__=='__main__':

  # run only as sudo/root user.
  if not os.geteuid()==0:
    print 'You should run this command as sudo/root user.'
    sys.exit(1)

  # setup configuration.
  setup(
    name='slen-utils',
    version='1.1.2',
    description='A bundle of utilities to manage SLEN resources.',
    long_description=open('README.rst').read(),
    author='SLEN DevOps',
    author_email='devops@sloopengine.io',
    url='https://github.com/sloopstash/slen-utils',
    python_requires='~=2.7',
    # packages=['slen'],
    packages=find_packages(),
    zip_safe=True,
    scripts=['bin/slen-cli','bin/slen-config'],
    install_requires=['subprocess32==3.2.7','requests==2.18.4','termcolor==1.1.0','jinja2==2.10','fqdn==1.1.0'],
    cmdclass={'install':_install},
    data_files=[('/etc/slen',['conf/main.ini','conf/main.ini.template'])],
    license='Apache License 2.0'
  )
