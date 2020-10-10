import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="restpki-client",
    version='1.2.0',
    author="Ismael Medeiros",
    author_email="IsmaelM@lacunasoftware.com",
    description="Client package for REST PKI",
    long_description=long_description,
    keywords='python pki rest certificate digital signature x509',
    url="https://github.com/LacunaSoftware/RestPkiPythonClient",
    packages=setuptools.find_packages(),
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Information Technology',
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        "Operating System :: OS Independent",
        'Topic :: Security',
        'Topic :: Security :: Cryptography',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    install_requires=[
        'simplejson==3.16.0',
        'requests==2.21.0',
        'six==1.12.0'
    ],
)
