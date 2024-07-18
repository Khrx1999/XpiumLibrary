from setuptools import setup, find_packages

setup(
    name="robotframework-xlibrary",
    version="12.0.2",
    author="Tassana Khrueawan",
    author_email="tassana.khr@gmail.com",
    description="Library Custom For Automate",
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Khrx1999/robotframework-xlibrary.git",
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=[
        'robotframework>=6.1.1',
        'selenium>=3.141.0',
        'requests>=2.25.1',
        'pymongo>=4.7.2',
        'bson>=0.5.10',
        'appium-python-client>=1.0.2',
        'robotframework-appiumlibrary>=1.5.0',
        'robotframework-requests>=0.7.0',
        'robotframework-appiumflutterlibrary>=1.0.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Framework :: Robot Framework',
    ],
    python_requires='>=3.6',
)
