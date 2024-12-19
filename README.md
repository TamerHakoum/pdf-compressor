# PDF Compressor

A Python script to compress PDF files using Ghostscript.

## Requirements

*   Python 3
*   Ghostscript (install it from [https://www.ghostscript.com/](https://www.ghostscript.com/))

## Installation

1.  Clone the repository:

    ```bash
    git clone [https://github.com/](https://github.com/)<your_username>/pdf-compressor.git
    ```

2.  Navigate to the project directory:

    ```bash
    cd pdf-compressor
    ```

## Usage

1.  Place the PDF file you want to compress (e.g., `input.pdf`) in the same directory as the script.
2.  Run the script:

    ```bash
    python pdf_compressor.py
    ```

    You can also specify the output filename and compression quality:

    ```bash
    python pdf_compressor.py input.pdf output.pdf printer
    ```

    Where `printer` can be replaced with `screen`, `ebook`, or `prepress`.

## Example

To compress a PDF named `my_document.pdf` to `compressed_document.pdf` with ebook quality:

```bash
python pdf_compressor.py my_document.pdf compressed_document.pdf ebook
