# https://github.com/devcontainers/images/blob/main/src/cpp/README.md
FROM conanio/gcc11-ubuntu16.04

USER root

# TODO g++-i686-linux-gnu
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
     && apt-get -y install --no-install-recommends build-essential

ADD .conan2 /root/.conan2
RUN conan profile detect

COPY resources/toolchains/engel-toolchain-cube3210-i686_1.26.0+rc1_amd64.deb .
RUN dpkg -i engel-toolchain-cube3210-i686_1.26.0+rc1_amd64.deb

COPY toolchain.cmake /opt/x-tools/

RUN curl -s https://cmake.org/files/v3.31/cmake-3.31.5-linux-x86_64.tar.gz | tar --strip-components=1 -xz -C /usr/local
