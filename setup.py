import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="A-Simple-Dungeon-Engine",
    version="0.0.1",
    author="John Allison",
    author_email="john123allison@gmail.com",
    description="A modular framework for text-based adventure games.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/john123allison/a-simple-dungeon",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
