cmake_minimum_required(VERSION 3.24)
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

# tests installation (for cpack ...)
set(TESTS_INSTALL_DIR "tests/${PROJECT_NAME}")
install(TARGETS MyLib_ut DESTINATION ${TESTS_INSTALL_DIR}/bin COMPONENT SETUP_TESTS)
install(TARGETS ${PROJECT_NAME} DESTINATION ${TESTS_INSTALL_DIR}/lib COMPONENT SETUP_TESTS)
# copy dependencies for testing
install(DIRECTORY $<TARGET_PROPERTY:LibXml2::LibXml2,INTERFACE_LINK_DIRECTORIES> DESTINATION ${CMAKE_BINARY_DIR}/import COMPONENT SETUP_TESTS)
