#!/bin/bash
. ../mr-c-khmer-bleeding-edge/.env/bin/activate

cd pipeline

make -j8 clean all KHMER=../../mr-c-khmer-bleeding-edge/
