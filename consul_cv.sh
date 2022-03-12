#!/bin/bash

for n in {1..10} 
do
   current_number=$(python fizzBuzz_module.py $n)
   echo "consul kv put acme/operator/number $current_number"
done