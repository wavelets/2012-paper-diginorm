#! /usr/bin/env python
import blastparser
import screed
import sys

fa_1 = sys.argv[1]
fa_2 = sys.argv[2]
blast_1x2 = sys.argv[3]
blast_2x1 = sys.argv[4]

seqs1 = {}
seqs2 = {}

for record in screed.open(fa_1):
    seqs1[record.name] = record.sequence

for record in screed.open(fa_2):
    seqs2[record.name] = record.sequence

for b in blastparser.parse_fp(open(blast_1x2)):
    assert b.query_name in seqs1
    del seqs1[b.query_name]

for b in blastparser.parse_fp(open(blast_2x1)):
    assert b.query_name in seqs2
    del seqs2[b.query_name]

print len(seqs1), 'missing 1'
print len(seqs2), 'missing 2'

fp = open(blast_1x2 + '.missing', 'w')
for name in seqs1:
    fp.write(">%s\n%s\n" % (name, seqs1[name]))
fp.close()

fp = open(blast_2x1 + '.missing', 'w')
for name in seqs2:
    fp.write(">%s\n%s\n" % (name, seqs2[name]))
fp.close()


