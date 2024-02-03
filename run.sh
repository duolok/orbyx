#!/usr/bin/env bash

install_package() {
  local package_dir=$1
  if [[ -d "$package_dir" && -f "$package_dir/setup.py" ]]; then
    echo "Installing package in $package_dir"
    cd "$package_dir" || exit
    python3 setup.py install || { echo "Installation failed for $package_dir"; exit 1; }
    cd - || exit
  else
    echo "Directory $package_dir does not exist or no setup.py found."
    exit 1
  fi
}

start_server() {
  local project_dir=$1
  if [[ -d "$project_dir" ]]; then
    echo "Starting Django server in $project_dir"
    cd "$project_dir" || exit
    python3 manage.py runserver >> server.log 2>&1 || { echo "Failed to start Django server in $project_dir"; exit 1; }
    cd - || exit
  else
    echo "Directory $project_dir does not exist."
    exit 1
  fi
}

echo "Cleaning the environment..."
./clean.sh || { echo "Cleaning failed."; exit 1; }

cd orbyx

install_package "api"
install_package "block_visualizer"
install_package "tinywiki"
install_package "core"
install_package "graph_explorer"

start_server "graph_explorer"
