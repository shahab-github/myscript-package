from setuptools import setup, find_packages

setup(
    name="internal_services",
    version="0.0.1",
    packages=find_packages(),
    install_requires=["requests"],
    entry_points={
        'console_scripts': [
            'restore_redshift = internal_services.__main__:main',
            'myapi = internal_services.myapi.__main__:main',
            'test_redshift = internal_services.__main__:redshift_function',
            'redshift = internal_services.__main__:redshift',

        ]},
)