from pafpy import PafFile, Strand
from Bio import SeqIO
import glob,os
files = glob.glob("nanofilt*.fasta")
dict1 = {"ermB":39,"sul1":38,"tetO":39}
for file in files:
    target = file.split("/")[-1][9:-6] # arg_location
    name = target.split("_")[0]
    output = "arg_mapping/%s_blast_reads.fasta"%target
    output2 = "arg_mapping/%s_arg.fasta"%target
    mapping = "arg_mapping/%s_bridge_blast"%target
    if os.path.isfile(mapping):
        handle = open(output,"w")
        handle2 = open(output2,"w")
        arg = {}
        with open(mapping) as paf2:
            for line in paf2:
                record = line.rstrip().split("\t")
                qname = record[0] # read name
                identity = float(record[2]) # 100% alignment identity
                length = int(record[3]) # alignment length == bridge primer
                if (qname not in arg.keys()) and (identity == 100) and (length == dict1[name]):
                    if int(record[8]) == 1: # forward strand 
                        arg[qname] = (0,int(record[6]))
                    else: # reverse strand
                        arg[qname] = (1,int(record[7]))
        for record in SeqIO.parse(file, "fasta"):
            if (str(record.id) in arg.keys()):
                seq = str(record.seq)
                qname = str(record.id)
                pos = arg[qname]
                if pos[0] == 0:
                    seq1 = seq[:pos[1]]
                    seq2 = seq[pos[1]:]
                else:
                    seq1 = seq[pos[1]:]
                    seq2 = seq[:pos[1]]
                handle.write(">%s_%i_%i\n%s\n"%(qname,pos[0],pos[1],seq1))
                handle2.write(">%s_%i_%i\n%s\n"%(qname,pos[0],pos[1],seq2))
        handle.close()
        handle2.close()
