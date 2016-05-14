INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_DETECTMARKSPACE detectmarkspace)

FIND_PATH(
    DETECTMARKSPACE_INCLUDE_DIRS
    NAMES detectmarkspace/api.h
    HINTS $ENV{DETECTMARKSPACE_DIR}/include
        ${PC_DETECTMARKSPACE_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    DETECTMARKSPACE_LIBRARIES
    NAMES gnuradio-detectmarkspace
    HINTS $ENV{DETECTMARKSPACE_DIR}/lib
        ${PC_DETECTMARKSPACE_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(DETECTMARKSPACE DEFAULT_MSG DETECTMARKSPACE_LIBRARIES DETECTMARKSPACE_INCLUDE_DIRS)
MARK_AS_ADVANCED(DETECTMARKSPACE_LIBRARIES DETECTMARKSPACE_INCLUDE_DIRS)

