# wasterwater_arg_metagenomics

antibiotic resistance genes (ARGs) discovery and comparison among metagenomics sequenced data pipeline for paper 
"Profiling the fate of antibiotic resistance across a WWTP using metagenomics and epicPCR for risk estimation"

## Required libraries, databases and tools:

    megahit https://github.com/voutcn/megahit 
    rgi https://github.com/arpcard/rgi
    card-databse https://card.mcmaster.ca/download 
    mob-suite https://github.com/phac-nml/mob-suite
    bowtie2 https://github.com/BenLangmead/bowtie2
    blastn and blastx 
    MGE-database https://bench.cs.vt.edu/ftp/data/databases/MGEs90.fasta 
    centrifuge https://github.com/DaehwanKimLab/centrifuge 
    PlasFlow https://github.com/smaegol/PlasFlow
    seqkit https://github.com/shenwei356/seqkit
    seqtk https://github.com/lh3/seqtk 
    os, subprocess, collections, pathlib, numpy, pandas, BioPython

## Usage
1. Install all the tools, libraries and their related databases.
2. Replace the second block in the jupyter notebook with custom path.
3. Run the code, but need to switch environment for PlasFlow.
