
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="text2image-Saurabh_Kumar", # Replace with your own username
    version="0.0.1",
    author="Saurabh Kumar",
    author_email="skp1535@gmail.com",
    description="Package to convert text data into image",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)