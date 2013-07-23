#!/bin/bash
KHMER=${PWD}/../mr-c-khmer-bleeding-edge

. ${KHMER}/.env/bin/activate

cd pipeline

make clean
make -j8 all KHMER=${KHMER}

pylint -f parseable pipeline/*.py  | tee ../pylint.out
