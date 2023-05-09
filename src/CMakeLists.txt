cmake_minimum_required(VERSION 3.16)

project(main)

add_executable(main main.cpp)

install(TARGETS main)

enable_testing()
# Configure the test script for the current build
configure_file(${CMAKE_CURRENT_SOURCE_DIR}/tests/test_sum.sh.in ${CMAKE_CURRENT_BINARY_DIR}/test_sum.sh)
add_test(NAME test-summation COMMAND bash test_sum.sh)
