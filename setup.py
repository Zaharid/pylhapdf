from distutils.extension import Extension
from distutils.core import setup
from Cython.Build import cythonize

import numpy

numpy_includes = numpy.get_include()

ext = Extension(
    "pylhapdf",
    ["pylhapdf.pyx"],
    extra_compile_args=["-std=c++17"],
    include_dirs=[numpy_includes],
    language="C++",
    libraries=["LHAPDF"],
)

setup(
    name="pylhapdf",
    version="0.1",
    ext_modules=cythonize([ext],  ),
    #zip_safe=False,
)
