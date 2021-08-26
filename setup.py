import setuptools

#Genrate long description using readme file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stuffr",
    version="1.0.0",
    author="Juha Vierinen, Vetle Hofsøy-Woie",
    author_email="juha-pekka.vierinen@uit.no",
    description="Stuff from R implemented in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
    install_requires=[
        'h5py>=1.7.0',
        'numpy>=0.13.1',
        'scipy>=0.0.1',
        'matplotlib>=1.0.4'
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
