from setuptools import setup, find_packages

setup(
    name='vgmparse',
    version='2.0.2',
    description='VGM (Video Game Music) file parser',
    url='https://github.com/rejunity/vgmparse',
    author='Craig Dodd', 'Renaldas Zioma'
    author_email='craig@dodd.io', 'rzioma@acm.org'
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Multimedia :: Sound/Audio',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
    ],
    packages=find_packages(),
)
