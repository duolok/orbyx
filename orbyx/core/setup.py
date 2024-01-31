from setuptools import setup, find_packages
setup(
    name="orbyx-core",
    version="0.1",
    packages=find_packages(),
    entry_points = {
        'console_scripts':
            ['orbyx_main=core.console_main:main'],
        'django_app':
            ['django=core.engine:Engine'],
    },
    install_requires=[
        'orbyx-api==0.1',
    ],
    zip_safe=True
)