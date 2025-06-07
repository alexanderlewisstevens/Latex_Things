import subprocess
import os
import sys


def build_all_tex():
    print("Compiling all .tex files in 2370_question_banks/ to PDF...")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    question_banks_dir = os.path.join(script_dir, "2370_question_banks")
    tex_files = [f for f in os.listdir(question_banks_dir) if f.endswith('.tex')]
    for tex_file in tex_files:
        tex_path = os.path.join(question_banks_dir, tex_file)
        result = subprocess.run([
            "latexmk", "-pdf", f"-output-directory={question_banks_dir}", tex_path
        ])
        if result.returncode != 0:
            print(f"Failed to compile {tex_file}")
            sys.exit(1)


def local_cleanup():
    print("Cleaning up auxiliary files locally...")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    question_banks_dir = os.path.join(script_dir, "2370_question_banks")
    aux_patterns = ["*.aux", "*.log", "*.fls", "*.fdb_latexmk"]
    for pattern in aux_patterns:
        subprocess.run(f"rm -f {os.path.join(question_banks_dir, pattern)}", shell=True)


def main():
    build_all_tex()
    local_cleanup()
    print("All PDFs built and auxiliary files cleaned up!")

if __name__ == "__main__":
    main()
