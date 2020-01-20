export PATH=${PREFIX}/bin:${PATH}
echo `which python3`
mkdir build
cd build
meson -Dbuildtype=release --prefix=${PREFIX}
ninja install
