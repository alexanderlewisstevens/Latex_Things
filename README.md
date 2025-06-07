# Practice Problem Banks, Exams, and Quizzes: LaTeX Workflow

This repository provides a streamlined, automated workflow for compiling LaTeX question banks into PDFs using Docker and Python. All question banks use a compact, standardized LaTeX template for consistency and space efficiency.

## Directory Structure


```
2370_question_banks/
    Quiz_1_Bank.tex
    Quiz_2_Bank.tex
    ...
    Quiz_8_Bank.tex
    Quiz_1_Bank.pdf
    ...
Dockerfile
build_all.py
```

## How It Works

- **LaTeX Source Files:** All quizzes are in `2370_question_banks/` as `.tex` files, using a compact header strip for metadata.
- **PDF Output:** Compiled PDFs are saved in the same directory with matching names.
- **Automation:** The `build_all.py` script builds a minimal Docker image, compiles all `.tex` files to `.pdf`, and cleans up all LaTeX auxiliary files.
- **Dockerfile:** Uses a minimal Debian image with only the essential TeX Live packages for fast, small builds.

## Usage

### 1. Prerequisites
- [Docker](https://www.docker.com/) installed and running
- [Python 3](https://www.python.org/) installed

### 2. Build and Compile All PDFs

From the project root, run:

```zsh
python3 build_all.py
```

This will:
- Build the Docker image (if not already built)
- Compile all `.tex` files in `2370_question_banks/` to `.pdf`
- Remove all LaTeX auxiliary files (`.aux`, `.log`, `.fls`, `.fdb_latexmk`)

### 3. Add or Edit Question Banks
- Edit or add new `.tex` files in `2370_question_banks/` using the provided template (see any existing file for the format).
- Re-run `python3 build_all.py` to regenerate all PDFs.

### 4. Customization
- The LaTeX template uses a compact header strip for course, quiz, and bank info.
- To change the header, edit the `\lhead`, `\chead`, and `\rhead` lines in your `.tex` files.

## Troubleshooting
- If you see LaTeX errors, check your `.tex` file for syntax issues.
- If you need additional LaTeX packages, add them to the `RUN apt-get install ...` line in the `Dockerfile` and rebuild.

## License
MIT License.
