import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sphinxience",
    version="0.1",
    author="Bram Geron",
    author_email="bram@bram.xyz",
    description="A Sphinx extension to assist in publishing scientific writing in either HTML or PDF.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bgeron/sphinxience",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Framework :: Sphinx :: Extension",
        "Intended Audience :: Science/Research",
        "Topic :: Documentation :: Sphinx",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering",
    ),
)