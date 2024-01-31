remove_eggs(){
  cd $1
  rm -rf build
  rm -rf *.egg-info
  rm -rf dist
  cd ..
}
cd orbyx

remove_eggs api
remove_eggs core
remove_eggs block_visualizer