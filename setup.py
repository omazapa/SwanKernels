"""
Setup Module to setup Python Handlers for the SwanKernelEnv extension.
"""
import os

import glob

import os, shutil
import setuptools
from setuptools.command.install import install

name="swankernels"

package_data_spec = {
    name: [
        "*"
    ]
}

DATA_FILES = [
    ('share/jupyter/kernels/', [
     ] + glob.glob('./kernels')
    )
]
with open("README.md", "r") as fh:
    long_description = fh.read()

setup_args = dict(
    name=name,
    version="0.0.1",
    url="https://github.com/swan-cern/jupyter-extensions",
    author="SWAN Admins",
    description="SWAN Kernels for Jupyter",
    long_description= long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    data_files=DATA_FILES,
    install_requires=[
          'notebook==6.1.*',
          'tornado',
          'jupyter_core',
          'requests'
    ],
    zip_safe=False,
    include_package_data=True,
    license="AGPL-3.0",
    platforms="Linux, Mac OS X, Windows",
    keywords=["Jupyter", "Notebooks", "SWAN", "CERN"],
    classifiers=[
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Framework :: Jupyter",
    ],
)


if __name__ == "__main__":
    os.system("./generate "+os.getcwd())
    setuptools.setup(**setup_args)
