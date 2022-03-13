#!/bin/bash

for n in {1..100}
do
   current_number=$(python fizzbuzz_module.py $n)
   consul kv put acme/number$n $current_number
done