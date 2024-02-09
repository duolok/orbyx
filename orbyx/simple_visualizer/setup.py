from setuptools import setup, find_packages
setup(
    name="simple_visualizer",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'generate_template':
            ['template=visualize_simple.generate_template:SimpleVisualizer'],
        'orbyx_visualizer_plugin':
            ['template=visualize_simple.generate_template:SimpleVisualizer'],
    },
    install_requires=[
        'orbyx-api==0.1',
        'jinja2'
    ],
    package_data={'visualize_simple': ['templates/*.html']},
    zip_safe=True
)
