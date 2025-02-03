# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.195.0/containers/cpp/.devcontainer/base.Dockerfile
# [Choice] Debian / Ubuntu version (use Debian 11/9, Ubuntu 18.04/21.04 on local arm64/Apple Silicon): debian-11, debian-10, debian-9, ubuntu-21.04, ubuntu-20.04, ubuntu-18.04
ARG VARIANT=debian-11
FROM mcr.microsoft.com/vscode/devcontainers/cpp:0-${VARIANT}

# [Optional] Uncomment this section to install additional packages.
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
     && apt-get -y install --no-install-recommends pip g++-i686-linux-gnu

ADD .conan /home/vscode/.conan
RUN pip install conan==1.66.0 \
     && conan profile new default --detect \
     && cp /root/.conan/profiles/default /home/vscode/.conan/profiles/default \
     && sudo chown -R vscode:vscode /home/vscode/.conan

COPY resources/toolchains/engel-toolchain-cube3210-i686_1.26.0+rc1_amd64.deb .
RUN dpkg -i engel-toolchain-cube3210-i686_1.26.0+rc1_amd64.deb