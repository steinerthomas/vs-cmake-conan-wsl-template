cmake_minimum_required(VERSION 3.17)
include(CTest)

add_executable(MyLib_ut)
target_sources(MyLib_ut
    PRIVATE
        "UTMyLib.cpp"
)

target_link_libraries(MyLib_ut
    CONAN_PKG::gtest
    MyLib
)

add_test(NAME MyLib_ut COMMAND ${CMAKE_BINARY_DIR}/bin/MyLib_ut)
