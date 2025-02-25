from setuptools import setup

requirements = ['aiodns', 'aiohttp', 'backoff', 'base58', 'loguru']

setup(
    name='pythclient',
    version='0.0.2',
    packages=['pythclient'],
    author='Pyth Developers',
    author_email='contact@pyth.network',
    install_requires=requirements,
    extras_require={
        'testing': requirements + ['mock', 'pytest', 'pytest-cov', 'pytest-socket',
                                   'pytest-mock', 'pytest-asyncio'],
    },
    python_requires='>=3.7.0',
)
