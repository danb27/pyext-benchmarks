from Cython.Build import cythonize
from pathlib import Path
from setuptools import setup

setup(
    ext_modules=cythonize(str(
        Path(__file__).parent /
        "funcs.pyx"
    ))
)
