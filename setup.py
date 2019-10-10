import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="a-simple-dungeon",
    version="0.0.1",
    author="John Allison",
    author_email="author@example.com",
    description="A framework for building text-based fantasy games",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/John123Allison/a-simple-dungeon",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        # "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)