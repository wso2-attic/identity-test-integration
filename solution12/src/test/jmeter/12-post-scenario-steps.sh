#!/bin/bash

prgdir=$(dirname "$0")
script_path=$(cd "$prgdir"; pwd)

echo "working directory : "$script_path
#run base-setup.sh to deploy artifacts
source $script_path/../teardown.sh 


echo "post-steps are done..."


