from setuptools import setup, find_packages


setup(
    name='t2s-fingeruebung',
    version='0.1.0',
    packages=['', 'data', 'eval', 'nlp'],
    package_dir={"": "src"},
    url='',
    license='MIT',
    author='Arne Gideon',
    author_email='s2903023@stud.uni-frankfurt.de',
    description='Text2Scene Praktikum WiSe 2021-22 Fingeruebung von Arne Gideon',
    install_requires=[
        'numpy >= 1.21.3',
        'spacy >= 3.1.4',
        'networkx >= 2.6.3',
        'matplotlib >= 3.4.3',
        'xmltodict',
        'setuptools >= 58.3.0'
    ]
)
