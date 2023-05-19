# HuggingFace Transformer

This code uses the Hugging Face Transformers library to generate a summary of a PDF file. The code first imports the `textract` library to extract the text from the PDF file. The text is then passed to the `HfAgent` class, which is used to generate a summary using the BigCode/StarCoder model. The summary is then printed to the console.

## Instructions

To run this code, you will need to install the following libraries:

```
pip install transformers
pip install textract
```

Once you have installed the libraries, you can run the code by typing the following command in your terminal:

```
python HFTransformer.py
```

## Output

PDF file source: https://opensource.com/sites/default/files/open_source_eBook_AnOpenWorld_web.pdf

The output of the code will be a summary of the PDF file. The summary will be printed to the console.


## Vulnerabilities

Model used: https://huggingface.co/bigcode/starcoder

There are no known vulnerabilities in this code. However, it is important to note that the BigCode/StarCoder model is still under development, and it is possible that the model may generate summaries that are inaccurate or misleading.

## License

MIT License

Copyright (c) 2023 Sumit Sahoo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.


