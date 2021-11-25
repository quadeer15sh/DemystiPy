import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DemystiPy",                     # This is the name of the package
    version="0.0.1",                        # The initial release version
    author="Quadeer Shaikh",                     # Full name of the author
    author_email='quadeershaikh15.8@gmail.com', # Author Email ID
    description="An approach towards explainable statistics and machine learning", # Short Description of the module
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),    # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.6',                # Minimum version requirement of the package
    # py_modules=["pdistributions"],             # Name of the python package
    package_dir={'':'src'},     # Directory of the source code of the package
    install_requires=['scipy','numpy','matplotlib']                     # Install other dependencies if any
)