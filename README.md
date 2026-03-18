# DNA Analyzer
 
A command-line bioinformatics tool for DNA sequence analysis. Input any DNA sequence and get instant validation, nucleotide composition, GC content, reverse complement, and live NCBI species identification — all in one script.
 
Built with Python and Biopython as a self-directed learning project during BSc Bioinformatics.
 
---
 
## Features
 
- **Sequence validation** — checks whether the input is a valid biological DNA sequence before any analysis runs
- **Nucleotide breakdown** — counts individual A, T, G, C bases with percentages
- **GC content and ratio** — calculates GC% and GC ratio, key metrics in genome analysis
- **Reverse complement** — generates the reverse complement strand of the input sequence
- **NCBI species identification** — searches the NCBI nucleotide database using the Entrez API and returns the closest matching accession number, organism name, and sequence details
 
---
 
## Requirements
 
- Python 3.7+
- Biopython
 
Install dependencies:
 
```bash
pip install biopython
```
 
---
 
## Usage
 
```bash
python dna_analyzer.py
```
 
You will be prompted to enter a DNA sequence. Example:
 
```
Enter DNA sequence: ATGCGATACGCTTACGAT
 
Validating sequence...      VALID
Nucleotide count:
  A: 5  (27.8%)
  T: 5  (27.8%)
  G: 4  (22.2%)
  C: 4  (22.2%)
 
GC Content:     44.4%
GC Ratio:       0.44
Reverse Complement: ATCGTAAGCGTATCGCAT
 
Searching NCBI...
Accession:      NM_001234567
Organism:       Homo sapiens
Description:    DNA-binding protein gene, partial sequence
```
 
---
 
## How It Works
 
1. User inputs a raw DNA sequence string
2. The script validates the input — only A, T, G, C characters are accepted
3. If valid, nucleotide counts and percentages are calculated using Biopython's `Seq` object
4. GC content is computed using `GC()` from `Bio.SeqUtils`
5. Reverse complement is generated using Biopython's built-in `.reverse_complement()` method
6. The sequence is submitted to NCBI via `Bio.Entrez` using a BLAST-style nucleotide search
7. The top match is parsed and returned with accession number, organism, and description
 
---
 
## Project Structure
 
```
dna-analyzer/
├── dna_analyzer.py     # Main script
└── README.md
```
 
---
 
## Planned Features
 
- Protein translation (DNA → amino acid sequence)
- ORF (Open Reading Frame) finder
- Support for FASTA file input
- Multiple sequence comparison
- Export results to CSV or text file
 
---
 
## Why I Built This
 
I am a first-year BSc Bioinformatics student teaching myself computational biology. This project started as a curiosity — I wanted to understand how bioinformatics tools actually work under the hood by building one from scratch. It uses real biological databases and produces results consistent with established tools.
 
This is an actively developed project. Contributions and suggestions are welcome.
 
---
 
## Author
 
**Adarsh**

BSc Bioinformatics- <!--Swami Vivekanand Subharti University-->  
GitHub: [adrix-ft](https://github.com/adrix-ft)  
ORCID: [0009-0002-7040-170X](https://orcid.org/0009-0002-7040-170X)  
 
---
 
## License
 
MIT License — free to use, modify, and distribute with attribution.
 
