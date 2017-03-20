try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import os.path
import re
VERSION_RE = re.compile(r'''__version__ = ['"]([0-9.]+)['"]''')
BASE_PATH = os.path.dirname(__file__)


with open(os.path.join(BASE_PATH, 'shadowproxy.py')) as f:
    try:
        version = VERSION_RE.search(f.read()).group(1)
    except IndexError:
        raise RuntimeError('Unable to determine version.')

with open(os.path.join(BASE_PATH, 'requirements.txt')) as f:
    install_requires = [line for line in f.readlines() if line.strip()]

long_description=open('README.md').read()

setup(
    name='shadowproxy',
    description='A proxy server that implements Socks5/Shadowsocks/Redirect/HTTP (tcp) and Shadowsocks/TProxy/Tunnel (udp) protocols.',
    long_description=long_description,
    license='MIT',
    version='0.1',
    author='Yingbo Gu',
    author_email='tensiongyb@gmail.com',
    maintainer='Yingbo Gu',
    maintainer_email='tensiongyb@gmail.com',
    url='https://github.com/guyingbo/shadowproxy',
    py_modules = ['shadowproxy'],
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'shadowproxy = shadowproxy:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
    ]
)
