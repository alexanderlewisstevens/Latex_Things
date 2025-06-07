# Use a minimal Debian base image
FROM debian:bookworm-slim

# Install required system packages and minimal TeX Live
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        texlive-latex-base \
        texlive-latex-recommended \
        latexmk \
        ca-certificates \
        && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /workspace

# Copy the entire project (except files in .dockerignore) into the container
COPY . /workspace/

# Default command: compile all .tex files in 2370_question_banks to PDFs
CMD ["sh", "-c", "for f in 2370_question_banks/*.tex; do latexmk -pdf -output-directory=2370_question_banks \"$f\"; done"]
