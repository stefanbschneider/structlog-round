from setuptools import setup, find_packages


requirements = [
    'structlog',
]

test_requirements = [
    'pytest',
    'numpy'
]

setup(
    name='structlog-round',
    author='Stefan Schneider',
    version=0.1,
    description="A light-weight structlog processor to round floats for prettier logging.",
    url='https://github.com/stefanbschneider/structlog-round',
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=requirements,
    extras_require={'dev': test_requirements, 'tests': test_requirements},
    zip_safe=False
)
