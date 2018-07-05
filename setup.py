import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="restpki-client",
    version='1.0.0',
    author="Ismael Medeiros",
    author_email="IsmaelM@lacunasoftware.com",
    description="Client package for REST PKI",
    long_description=long_description,
    url="https://github.com/LacunaSoftware/RestPkiPythonClient",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        "Operating System :: OS Independent",
    ),
    install_requires=[
        'simplejson==3.8.1',
        'requests==2.19.1',
        'six==1.11.0'
    ],
)
