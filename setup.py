from setuptools import setup, find_packages


requirements = [
    'structlog',
]

test_requirements = [
    'pytest',
    'numpy'
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='structlog-round',
    author='Stefan Schneider',
    version=1.0,
    description="A light-weight structlog processor to round floats for prettier logging.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/stefanbschneider/structlog-round',
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=requirements,
    extras_require={'dev': test_requirements, 'tests': test_requirements},
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
