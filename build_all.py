import subprocess
import os
import sys

def build_image():
    print("Building Docker image (latex-pdf-converter)...")
    result = subprocess.run([
        "docker", "build", "-t", "latex-pdf-converter", "."
    ])
    if result.returncode != 0:
        print("Docker build failed.")
        sys.exit(1)


def run_container():
    print("Running container to compile PDFs and clean up...")
    shell_cmd = (
        "for f in 2370_question_banks/*.tex; do "
        "latexmk -pdf -output-directory=2370_question_banks \"$f\"; "
        "done; "
        "rm -f 2370_question_banks/*.{aux,log,fls,fdb_latexmk}"
    )
    result = subprocess.run([
        "docker", "run", "--rm",
        "-v", f"{os.getcwd()}/2370_question_banks:/workspace/2370_question_banks",
        "latex-pdf-converter",
        "sh", "-c", shell_cmd
    ])
    if result.returncode != 0:
        print("Docker run failed.")
        sys.exit(1)


def local_cleanup():
    print("Cleaning up auxiliary files locally...")
    aux_patterns = ["*.aux", "*.log", "*.fls", "*.fdb_latexmk"]
    for pattern in aux_patterns:
        subprocess.run(f"rm -f 2370_question_banks/{pattern}", shell=True)


def main():
    build_image()
    run_container()
    local_cleanup()
    print("All PDFs built and auxiliary files cleaned up!")

if __name__ == "__main__":
    main()
