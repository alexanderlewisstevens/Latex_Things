# Use a minimal Debian base image
FROM debian:bookworm-slim

# Install required system packages and minimal TeX Live
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        texlive-latex-base \
        texlive-latex-recommended \
        latexmk \
        ca-certificates \
        git \
        python3 \
        python3-pip \
        && rm -rf /var/lib/apt/lists/*

        
# Set the working directory
WORKDIR /workspace

# Copy the entire project (except files in .dockerignore) into the container
COPY . /workspace/

# Default command: run the build_all.py script
CMD ["python3", "build_all.py"]
