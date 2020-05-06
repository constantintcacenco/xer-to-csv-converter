from setuptools import setup, find_packages


setup_args = dict(
    name='xertocsv',
    version='1.0.3',
    description='XER to CSV convertor',
    long_description_content_type="",
    license='Constantin Tcacenco',
    packages=find_packages(),
    author='Constantin Tcacenco',
    author_email='constantin.tcacenco@gmail.com',
    keywords=['csv', 'xer', 'converter'],
    url='https://github.com/constantintcacenco/xer-to-csv-converter',
    download_url='https://github.com/constantintcacenco/xer-to-csv-converter'
)

install_requires = [
    'pandas'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)