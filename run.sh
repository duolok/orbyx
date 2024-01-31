lay_eggs(){
  cd $1
  pwd
  python3 setup.py install
  cd ..
}

run_server(){
  cd $1
  python3 manage.py runserver
}
pwd
source clean.sh
pwd
lay_eggs api
lay_eggs block_visualizer
lay_eggs core
run_server graph_explorer
