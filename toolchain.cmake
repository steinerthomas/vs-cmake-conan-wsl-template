# this one is important
set(CMAKE_SYSTEM_NAME Linux)
set(CMAKE_SYSTEM_PROCESSOR x86)

SET(CMAKE_CXX_COMPILER_ID GNU)
SET(CMAKE_COMPILER_IS_GNUCXX 1)
SET(CMAKE_C_COMPILER_ID GNU)
#SET(CMAKE_CXX_COMPILER_VERSION 8)
#SET(CMAKE_C_COMPILER_VERSION 8)
SET(CMAKE_CXX_COMPILER_VERSION "8.3.0" CACHE STRING "C++ Version")
SET(CMAKE_C_COMPILER_VERSION "8.3.0" CACHE STRING "C Version")

SET(_GLIBCXX_USE_CXX11_ABI ON)
SET(CMAKE_EXPORT_COMPILE_COMMANDS ON)
SET(THREADS_PTHREAD_ARG "2" CACHE STRING "Forcibly set by toolchain.cmake." FORCE)

# specify the cross compiler
# for showcase the system ones are used - in the real toolchain the paths are:
# e.g. "/opt/x-tools/i686-cube3210-linux-gnu/bin/i686-cube3210-linux-gnu-gcc", "/opt/x-tools/i686-cube3210-linux-gnu/i686-cube3210-linux-gnu/sysroot/", ...
set(CMAKE_C_COMPILER "/usr/bin/i686-linux-gnu-gcc" CACHE STRING "C compiler")
set(CMAKE_CXX_COMPILER "/usr/bin/i686-linux-gnu-g++" CACHE STRING "C++ compiler")
# Name of archiving tool for static libraries
set(CMAKE_AR "i686-linux-gnu-ar" CACHE PATH "Linux ar Program")
# where is the target environment (compiler and third-party)
set(CMAKE_FIND_ROOT_PATH "/" CACHE STRING "Find Root Path")
set(CMAKE_SYSROOT "/" CACHE STRING "SysRoot")

# search for programs in the build host directories
set(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
# for libraries and headers in the target directories
set(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)


# special linker flags
set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -Wl,-rpath-link -Wl,/usr/i686-linux-gnu/lib/")
set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -Wl,--unresolved-symbols=ignore-in-shared-libs")
