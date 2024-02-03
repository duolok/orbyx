from setuptools import setup, find_packages
setup(
    name="java_data_source",
    version="0.2",
    packages=find_packages(),
    entry_points={
        'orbyx_data_source_plugin':
            ['template=java_data_source.java_data_source:JavaDataSource']
    },
    install_requires=[
        'orbyx-api==0.1',
        'antlr4-python3-runtime==4.7.2'
    ],
    zip_safe=True
)