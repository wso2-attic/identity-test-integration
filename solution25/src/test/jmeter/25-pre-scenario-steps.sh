#!/bin/bash
server_host=$server_host
prgdir=$(dirname "$0")
script_path=$(cd "$prgdir"; pwd)

#run base-setup.sh to deploy artifacts
source $script_path/../base-setup.sh > $script_path/basesetup.log

echo "working directory : "$script_path
#updating jmeter properties - user.properties
sed -i "s|^\(server_host\s*=\s*\).*\$|\1${server_host}|" $script_path/../resources/user.properties
sed -i "s|^\(server_port\s*=\s*\).*\$|\1${server_port}|" $script_path/../resources/user.properties
sed -i "s|^\(ei_host\s*=\s*\).*\$|\1${ei_host}|" $script_path/../resources/user.properties
sed -i "s|^\(ei_port\s*=\s*\).*\$|\1${ei_port}|" $script_path/../resources/user.properties

echo "pre-steps are done..."
