project('pylhapdf', ['cpp'], default_options: ['cpp_std=c++17'], version: '0.1')


python = dependency('python3')

deps = [
    dependency('lhapdf'),
	python,
]


cython = find_program('cython')

py3_mod = import('python')

pyx_c = custom_target('pylhapdf_cpp_generated_src',
  output : 'pylhapdf.cpp',
  input : ['pylhapdf.pyx', 'clhapdf.pxd'],
  command : [cython, '-a', '--cplus' , '-3' , '@INPUT0@', '-o', '@OUTPUT@'],
)


python_inst = py3_mod.find_installation('python3')


# Having a way to get the install path on meson is apparently too difficult
# https://github.com/mesonbuild/meson/issues/6469
# so we get it manually
python_install_dir = run_command(
  python_inst, '-c',
  'from distutils.sysconfig import get_python_lib; print(get_python_lib())',
  check: true,
).stdout().strip()

numpy_includes = run_command(
	python_inst, '-c', 'import numpy; print(numpy.get_include())',
	check:true
).stdout().strip()


pymod = python_inst.extension_module('pylhapdf',
  pyx_c,
  dependencies: deps,
  install: true,
  include_directories: [numpy_includes],
  install_dir: python_install_dir,
)
