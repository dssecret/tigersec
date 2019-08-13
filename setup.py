import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='tigersec',
    version="0.1.1",
    author="Deekshan Saravanan",
    author_email="dsstudios.dev@gmail.com",
    description="Penetration Testing Tools Implemented in Python",
    long_description=long_description,
    url="https://www.github.com/dssecret/tigersec",
    packages=setuptools.find_packages(),
    license="MIT License",
    classifiers=(
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Security"
    )
)
