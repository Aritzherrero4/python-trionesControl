import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="trionesControl",
    version="1.0.0",
    author="Aritz Herrero",
    description="Simple python package to control smart lights using the Triones porotocol",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Aritzherrero4/python-trionesControl",
    license="MIT",
    packages=setuptools.find_packages(exclude=("tests",)),
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    install_requires=["pygatt", "pexpect"],
    python_requires='>=3.6'
)