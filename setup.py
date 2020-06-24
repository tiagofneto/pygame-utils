import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="utils-pygame",
    version="0.0.1",
    license="MIT",
    author="Tiago Neto",
    author_email="tiago.f.neto@gmail.com",
    description="A compilation of utility tools for pygame",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tiagofneto/pygame-utils",
    packages=setuptools.find_packages(),
    install_requires=[
        "pygame",
        ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
