# wasterwater_arg_metagenomics

antibiotic resistance genes (ARGs) discovery and comparison among metagenomics sequenced data pipeline for paper 
"Profiling the fate of antibiotic resistance across a WWTP using metagenomics and epicPCR for risk estimation"

## Part1 Sample ARG Identification

### Required libraries, databases and tools:

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

### Usage
1. Install all the tools, libraries and their related databases.
2. Replace the second block in the jupyter notebook with custom path.
3. Run the code, but need to switch environment for PlasFlow.

## Part2 EpicPCR Analysis

### Methods

#### **Step1** Trim and filter out low qulity reads

a) Trim reads using porechop
```
porechop -t 15 -i [temp]_input.fastq --discard_middle -o trimmed_[temp].fastq
```

b) Remove reads with quality score below 7 

```
NanoFilt -q 7 trimmed_[temp].fastq > nanofilt_[temp].fastq
```

#### **Step2** Blast agaisnt linker primer sequences

```
blastn -db reference_[temp]_bridge -query [temp]_input_seq.fasta -outfmt 6 -num_threads 10 -out arg_mapping/[temp]_bridge_blast
```

#### **Step3** Split fusion reads using a customized script

```
python split_read_blast.py
```

#### **Step4** Taxonomic Classification 

```
emu abundance [temp]_input.fasta --output-dir output_dir --output-basename [temp]_emu --threads 10 --db dbs
```

