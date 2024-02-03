from setuptools import setup, find_packages
setup(
    name="wikipedia_data_source",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'orbyx_data_source_plugin':
            ['template=tinywiki.engine:WikipediaDataSource'],
        'orbyx_tinywiki':
            ['template=tinywiki.engine:WikipediaDataSource'],
    },
    install_requires=[
        'orbyx-api==0.1',
        'beautifulsoup4',
        'requests'
    ],
    zip_safe=True
)
