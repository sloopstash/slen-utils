# Import community modules.
import os
import sys
from setuptools import setup,find_packages
from setuptools.command.install import install


# Custom installer.
class _install(install):
  
  # Run operations.
  def run(self):
    from subprocess32 import call
    config_dir = call(['mkdir','/etc/slen'])
    if config_dir==0:
      call(['chmod','-R','600','/etc/slen'])
    install.run(self)

if __name__=='__main__':

  # Run only as sudo/root user.
  if not os.geteuid()==0:
    print 'Run this command as sudo/root user.'
    sys.exit(1)

  # Setup configuration.
  setup(
    name='slen-utils',
    version='1.1.3',
    description='A command line utility to manage SloopEngine resources.',
    long_description=open('README.rst').read(),
    author='SLEN DevOps',
    author_email='devops@sloopengine.io',
    url='https://github.com/sloopstash/slen-utils',
    python_requires='~=2.7',
    # packages=['slen'],
    packages=find_packages(),
    zip_safe=True,
    scripts=['bin/slen-cli','bin/slen-config'],
    install_requires=['subprocess32==3.2.7','requests==2.20.0','termcolor==1.1.0','jinja2==2.10','fqdn==1.1.0'],
    cmdclass={'install':_install},
    data_files=[('/etc/slen',['conf/main.ini','conf/main.ini.template'])],
    license='Apache License 2.0'
  )
