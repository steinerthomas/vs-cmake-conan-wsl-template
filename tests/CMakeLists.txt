cmake_minimum_required(VERSION 3.17)
include(CTest)

find_package(GTest REQUIRED CONFIG)

add_executable(MyLib_ut)
target_sources(MyLib_ut
    PRIVATE
        "UTMyLib.cpp"
)

target_link_libraries(MyLib_ut
    GTest::gtest GTest::gtest_main
    MyLib
)

add_test(NAME MyLib_ut COMMAND ${CMAKE_BINARY_DIR}/tests/MyLib_ut)
