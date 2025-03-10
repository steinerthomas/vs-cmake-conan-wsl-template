# https://github.com/devcontainers/images/blob/main/src/cpp/README.md
FROM mcr.microsoft.com/devcontainers/cpp:1-debian-11

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
     && apt-get -y install --no-install-recommends pip g++-i686-linux-gnu

ADD .conan2 /home/vscode/.conan2
RUN pip install conan==2.12.1 \
     && conan profile detect \
     && cp /root/.conan2/profiles/default /home/vscode/.conan2/profiles/default \
     && sudo chown -R vscode:vscode /home/vscode/.conan2

COPY resources/toolchains/engel-toolchain-cube3210-i686_1.26.0+rc1_amd64.deb .
RUN dpkg -i engel-toolchain-cube3210-i686_1.26.0+rc1_amd64.deb

COPY toolchain.cmake /opt/x-tools/

RUN curl -s https://cmake.org/files/v3.31/cmake-3.31.5-linux-x86_64.tar.gz | tar --strip-components=1 -xz -C /usr/local
