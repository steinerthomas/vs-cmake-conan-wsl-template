cmake_minimum_required(VERSION 3.17)
project(MyLib CXX)
set(THREADS_PREFER_PTHREAD_FLAG ON)

find_package(LibXml2 REQUIRED CONFIG)

# simplified for showcase shared only
add_library(MyLib SHARED)

target_sources(MyLib
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/src/MyLib.cpp
)

target_include_directories(MyLib PUBLIC include)

target_link_libraries(MyLib
    PRIVATE
        LibXml2::LibXml2
)

# tests
enable_testing()
add_subdirectory(tests)
