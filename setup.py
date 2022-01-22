from setuptools import setup
import io
import re
from os.path import dirname
from os.path import join

def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ) as fh:
        return fh.read()

setup(
    name='mmpower',
    description='Power calculator for Indoor model airplanes',
    long_description=re.compile(
        '^.. start-badges.*^.. end-badges',
        re.M | re.S
    ).sub(
        '',
        read('README.rst')
    ),
    long_description_content_type='text/x-rst',
    author='Roie R. Black',
    author_email='roie.black@gmail.com',
    url='https://github.com/rblack42/erbach-power',
    license='BSD',
    version='0.1.2',
    packages=['mmpower'],
entry_points= {
        "console_scripts": [
            "mmf = erbach.cli:cli"
        ]
    },
    python_requires='>=3.9',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Testing',
    ],
)
