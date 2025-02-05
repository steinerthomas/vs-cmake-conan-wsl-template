set(CONAN_PROFILE "default" CACHE STRING "conan profile")

message (STATUS "conan install ${CMAKE_SOURCE_DIR} -pr:h ${CONAN_PROFILE} -pr:b default -s build_type=${CMAKE_BUILD_TYPE} --output-folder ${CMAKE_BINARY_DIR} --build missing")
execute_process(
	COMMAND conan install ${CMAKE_SOURCE_DIR} -pr:h ${CONAN_PROFILE} -pr:b default -s build_type=${CMAKE_BUILD_TYPE} --output-folder ${CMAKE_BINARY_DIR} --build missing
	WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
	RESULT_VARIABLE CONAN_RESULT
)

#set(CMAKE_TOOLCHAIN_FILE "${CMAKE_BINARY_DIR}/build/${CMAKE_BUILD_TYPE}/generators/conan_toolchain.cmake")
