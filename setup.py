from setuptools import setup, find_packages
setup(
    name="module_two_company",
    version="0.1",
    description='something',
    url='https://github.com/omerholz/pymoduletwo',
    zip_safe=False,
    packages=find_packages(),

    install_requires=[
        'mongoengine==0.11.0'
    ],
    tests_require=['mongomock==3.7.0',
        'sure==1.4.0','pytest==3.0.5'
    ]

)

