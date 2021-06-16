import setuptools

#Genrate long description using readme file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stuffr",
    version="1.0.0",
    author="Juha Vierinen",
    author_email="juha-pekka.vierinen@uit.no",
    description="Stuff from R implemented in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
    install_requires=[
        'h5py>=2.10.0',
        'numpy>=1.19.5',
        'scipy>=1.4.1',
        'matplotlib>=3.3.4'
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)