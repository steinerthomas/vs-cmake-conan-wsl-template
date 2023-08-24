from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMakeDeps, CMake, cmake_layout
from conan.tools.files import copy
from os.path import join
import os

class MyLibConan(ConanFile):
    name = "mylib"
    #TODO use conan lockfiles with conan2
    requires = "libxml2/2.9.12#8286b154e79f6e97c90c8fa34f2cbcb4",\
               "zlib/1.2.12#c67ce17f2e96b972d42393ce50a76a1a"
    generators = "CMakeToolchain", "CMakeDeps"
    settings = "os", "compiler", "arch", "build_type"
    license = "MIT"
    exports_sources = "src/*", "include/*", "CMakeLists.txt", "tests/*"
    description = "Showcase for VisualStudio 2022 cmake conan project with cross-compiling on wsl1."

    def configure(self):
        # simplified for showcase shared only
        self.options["libxml2"].shared = True
        self.options["zlib"].shared = True
        self.options["libxml2"].iconv = False
    
    def build_requirements(self):
        #TODO use conan lockfiles with conan2
        self.test_requires("gtest/1.14.0#a110ad735ec3df8d21666bcbc06161ed")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        if os.getenv("CONAN_RUN_TESTS", False):
            cmake.test()

    def layout(self):
        cmake_layout(self)

    def package(self):
        # simplified for showcase shared only
        copy(self, "*.h", join(self.source_folder, "include"), join(self.package_folder, "include"), keep_path=True)
        copy(self, "*.so", self.build_folder, join(self.package_folder, "lib"), keep_path=False)

    def package_info(self): 
        #TODO improve this: add finders ...
        self.cpp_info.libs = ["MyLib"]
