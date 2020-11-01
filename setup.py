import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gamma-facet", # Replace with your own username
    version="0.0.1",
    author="Konstantin Hemker",
    author_email="konstantin.hemker@googlemail.com",
    description="Mock package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/konst-int-i/facet-mock",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)