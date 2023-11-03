cmake_minimum_required(VERSION 3.17)
project(MyLib CXX)
set(THREADS_PREFER_PTHREAD_FLAG ON)

if(CONAN_EXPORTED) # in conan local cache
    # standard conan installation, deps will be defined in conanfile.py
    # and not necessary to call conan again, conan is already running
	include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
    conan_basic_setup(TARGETS)
else() # in user space
    include(cmake-conan/conan.cmake)
	conan_cmake_run(
		CONANFILE conanfile.py
		UPDATE
		BASIC_SETUP
        CMAKE_TARGETS
        BUILD missing
		PROFILE ${CONAN_PROFILE}
        PROFILE_BUILD default
        PROFILE_AUTO ALL
	)
endif()

# simplified for showcase shared only
add_library(MyLib SHARED)

target_sources(MyLib
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/src/MyLib.cpp
)

target_include_directories(MyLib PUBLIC include)

#TODO use CMake finders with conan2
target_link_libraries(MyLib
    PRIVATE
        CONAN_PKG::libxml2
)

# tests
enable_testing()
add_subdirectory(tests)
