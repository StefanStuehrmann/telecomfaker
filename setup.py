from setuptools import setup, find_packages

setup(
    name="telecomfaker",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "": ["data/*.json"],
    },
    install_requires=[],
    python_requires=">=3.6",
    description="A Python package for generating realistic telecom operator test data",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/StefanStuehrmann/telecomfaker",
    entry_points={
        "console_scripts": [
            "telecomfaker=telecomfaker.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
) 