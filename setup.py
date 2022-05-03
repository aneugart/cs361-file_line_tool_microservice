from setuptools import find_packages, setup
from version import version

setup(
    name='storageMicroservice',
    version=version,
    author = "Andrew Neugarten",
    author_email = "neugarta@oregonstate.edu",
    description = ("A microservice to store and retreive date/ keyword pairs via a RESTful API."),
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "Flask",
        "python-dotenv",
        "Flask-SQLAlchemy",
        "Flask-Migrate",
        "SQLAlchemy",
    ],
)