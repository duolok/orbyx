#!/bin/bash

remove_package_artifacts() {
  local package_dir="$1"
  echo "Removing build artifacts in $package_dir..."
  pushd "$package_dir" >/dev/null 2>&1 || { echo "Failed to enter directory $package_dir"; return; }
  rm -rf build *.egg-info dist
  popd >/dev/null 2>&1
}

project_root=$(pwd)
orbyx_dir="$project_root/orbyx"

if [[ -d "$orbyx_dir" ]]; then
  echo "Moving to $orbyx_dir..."
  cd "$orbyx_dir" || exit

  remove_package_artifacts "api"
  remove_package_artifacts "core"
  remove_package_artifacts "block_visualizer"
  remove_package_artifacts "graph_explorer"
  remove_package_artifacts "java_data_source"

  cd "$project_root" || exit
else
  echo "Orbyx directory does not exist."
fi
