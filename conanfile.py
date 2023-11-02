from conans import ConanFile, CMake, tools
import os

class MyLibConan(ConanFile):
    name = "mylib"
    #TODO use conan lockfiles with conan2
    # libxml2/2.9.12#8286b154e79f6e97c90c8fa34f2cbcb4
    # zlib/1.2.12#c67ce17f2e96b972d42393ce50a76a1a
    requires = "libxml2/2.9.12"
    generators = "cmake"
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
        # gtest/1.14.0#a110ad735ec3df8d21666bcbc06161ed
        self.build_requires("gtest/1.14.0", force_host_context=True)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        if tools.get_env("CONAN_RUN_TESTS", False) and not tools.cross_building(self):
            cmake.test()

    def package(self):
        self.copy("*.h", dst="include", src="include")
        # simplified for showcase shared only
        self.copy("*.so", dst="lib", src="lib")

    def package_info(self): 
        #TODO improve this: add finders ...
        self.cpp_info.libs = ["MyLib"]
