# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.195.0/containers/cpp/.devcontainer/base.Dockerfile
# [Choice] Debian / Ubuntu version (use Debian 11/9, Ubuntu 18.04/21.04 on local arm64/Apple Silicon): debian-11, debian-10, debian-9, ubuntu-21.04, ubuntu-20.04, ubuntu-18.04
ARG VARIANT=debian-11
FROM mcr.microsoft.com/vscode/devcontainers/cpp:0-${VARIANT}

# [Optional] Uncomment this section to install additional packages.
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
     && apt-get -y install --no-install-recommends pip g++-i686-linux-gnu

ADD .conan2 /home/vscode/.conan2
RUN pip install conan==2.12.1 \
     && conan profile detect \
     && cp /root/.conan2/profiles/default /home/vscode/.conan2/profiles/default \
     && sudo chown -R vscode:vscode /home/vscode/.conan2

COPY resources/toolchains/engel-toolchain-cube3210-i686_1.26.0+rc1_amd64.deb .
RUN dpkg -i engel-toolchain-cube3210-i686_1.26.0+rc1_amd64.deb

RUN curl -s https://cmake.org/files/v3.31/cmake-3.31.5-linux-x86_64.tar.gz | tar --strip-components=1 -xz -C /usr/local