from setuptools import setup, find_packages #library

setup(
    name='SanskritAPI',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        # Add other dependencies here
    ],
    author='Vandan Patel',
    author_email='vandan11patel@gmail.com',
    description='A library for translating Sanskrit to English',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/patelvandan11/sanskrit',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
