# Use a minimal Debian base image
FROM debian:bookworm-slim

# Install full TeX Live, latexmk, Python, and useful tools
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        texlive-full \
        latexmk \
        make \
        git \
        python3 \
        python3-pip \
        less \
        nano \
        ca-certificates \
        fonts-lmodern \
        && rm -rf /var/lib/apt/lists/*

# Set up a non-root user for safer development
RUN useradd -ms /bin/bash latexuser
USER latexuser
WORKDIR /home/latexuser

# Default shell
SHELL ["/bin/bash", "-c"]

# Start in a shell by default
CMD ["/bin/bash"]
