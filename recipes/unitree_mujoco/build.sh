set -exo pipefail

cmake -GNinja -DCMAKE_INSTALL_PREFIX=$PREFIX $SRC_DIR/simulate -DCMAKE_INSTALL_LIBDIR=lib $CMAKE_ARGS
ninja
