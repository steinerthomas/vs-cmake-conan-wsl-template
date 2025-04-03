cmake_minimum_required(VERSION 3.24)
project(MyLib CXX)
set(THREADS_PREFER_PTHREAD_FLAG ON)

find_package(libxml2 CONFIG REQUIRED)

add_library(MyLib)

set(HELLO_MESSAGE "Hello world from cmake!")
configure_file(${CMAKE_CURRENT_SOURCE_DIR}/src/Constants.gen.h.in ${CMAKE_CURRENT_SOURCE_DIR}/out/generated/Constants.gen.h)

target_sources(MyLib
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/src/MyLib.cpp
)

target_include_directories(MyLib 
    PUBLIC include
    PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/out/generated
)

target_link_libraries(MyLib
    PRIVATE
        LibXml2::LibXml2
)

install(TARGETS MyLib COMPONENT CONAN)
install(DIRECTORY include/ DESTINATION include COMPONENT CONAN)

# tests
enable_testing()
add_subdirectory(tests)
