import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cifconvert",
    version="1.0.0",
    author="Maxim Lippeveld",
    author_email="lippeveld.maxim@gmail.com",
    description="Convert Amnis ImageStream cif-files to a usable format.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.ugent.be/mlippeve/cifconvert",
    packages=setuptools.find_packages(),
    python_requires=">3.6.1",
    install_requires=[
        "javabridge==1.0.18",
        "python-bioformats==1.5.2",
        "numpy==1.15.4",
        "joblib==0.13.0",
        "tqdm==4.28.1",
        "h5py==2.9.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "cifconvert=cifconvert.main:main"
        ]
    }
)
