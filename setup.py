from setuptools import setup

setup(
    name='httpie',
    version='0.9.3',
    install_requires=[
        'requests[security]>=2.10.0',
        'certifi',
    ],
    entry_points={
        'console_scripts': [
            'http = httpie.__main__:main',
        ],
    },
    # ... other metadata
)
