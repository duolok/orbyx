from setuptools import setup, find_packages
setup(
    name="block_visualizer",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'orbyx_visualizer':
            ['block_visualiser2=proba2.ispis2:Ispis'],
        'generate_template':
            ['template=visualize.generate_template:BlockVisualizer'],
        'orbyx_visualizer_plugin':
            ['template=visualize.generate_template:BlockVisualizer'],
    },
    install_requires=[
        'orbyx-api==0.1',
        "jinja2"
    ],
    package_data={'visualize': ['templates/*.html']},
    zip_safe=True
)
