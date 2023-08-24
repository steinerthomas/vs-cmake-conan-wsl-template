from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMakeDeps, CMake, cmake_layout
from conan.tools.files import copy
from os.path import join
import os

class MyLibConan(ConanFile):
    name = "mylib"
    requires = "libxml2/2.11.4",\
               "zlib/1.2.13"
    #generators = "CMakeToolchain", "CMakeDeps"
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
        self.test_requires("gtest/1.14.0")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        if os.getenv("CONAN_RUN_TESTS", False):
            cmake.test()

    def layout(self):
        cmake_layout(self)

    # according to https://docs.conan.io/1/reference/conanfile/tools/cmake/cmaketoolchain.html#user-presets-path this should prevent generating "CMakeUserPresets.json"
    # this should be removed (standard generators)
    def generate(self):
        tc = CMakeToolchain(self)
        tc.user_presets_path = False # this only works for conan v2, but is also described for conan v1
        # renaming to e.g. "ConanPresets.json" doesn't work aswell -> 2 files "ConanPresets.json" and "CMakeUserPresets.json" will be generated then
        tc.generate()
        deps = CMakeDeps(self)
        deps.generate()

    def package(self):
        # simplified for showcase shared only
        copy(self, "*.h", join(self.source_folder, "include"), join(self.package_folder, "include"), keep_path=True)
        copy(self, "*.so", self.build_folder, join(self.package_folder, "lib"), keep_path=False)

    def package_info(self): 
        #TODO improve this: add finders ...
        self.cpp_info.libs = ["MyLib"]
