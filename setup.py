import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / 'README.md').read_text()

setup_args = dict(
    name='xer2csv',
    version='1.0.5',
    description='A simple XER to CSV converter',
    long_description_content_type='text/markdown',
    long_description=README,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    packages=['xer2csv'],
    author='Constantin Tcacenco',
    author_email='constantin.tcacenco@gmail.com',
    keywords=['csv', 'xer', 'converter'],
    url='https://github.com/constantintcacenco/xer-to-csv-converter',
    download_url='https://github.com/constantintcacenco/xer-to-csv-converter',
    install_requires=['pandas']
)

if __name__ == '__main__':
    setup(**setup_args)
