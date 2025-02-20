import os
from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMakeDeps, CMake, cmake_layout
from conan.tools.files import copy
from conan.tools.build.cross_building import can_run

class MyLibConan(ConanFile):
    name = "mylib"
    generators = "CMakeToolchain", "CMakeDeps"
    settings = "os", "compiler", "arch", "build_type"
    license = "MIT"
    exports_sources = "src/*", "include/*", "CMakeLists.txt", "tests/*"
    description = "Showcase for VisualStudio 2022 cmake conan project with cross-compiling on wsl2."
    package_type = "shared-library"

    def configure(self):
        self.options["libxml2"].shared = True
        self.options["zlib"].shared = True
        self.options["libxml2"].iconv = False
    
    def requirements(self):
        self.requires("libxml2/2.11.4")

    def build_requirements(self):
        self.test_requires("gtest/1.14.0")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        if can_run(self) and not self.conf.get("tools.build:skip_test", default=False):
            cmake.test()

    def layout(self):
        cmake_layout(self)

    def package(self):
        cmake = CMake(self)
        cmake.install(component="CONAN")

    def package_info(self):
        self.cpp_info.libs = ["MyLib"]
        self.cpp_info.set_property("cmake_file_name", "MyLib")
