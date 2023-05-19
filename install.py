
import os
from os.path import join, expanduser, abspath
from subprocess import run

import sys

import urllib.request
import venv
import subprocess
from venv import create


#import requests


def main():
    URL='https://github.com/VladimirJz/efisys-migracion-db.git'
    MODULES=['clientes']
    RAW_REQUIREMENTS='https://raw.githubusercontent.com/VladimirJz/safi-migracion-repository/main/requirements.txt'
    
    #os.system("sshpass -p your_password ssh user_name@your_localhost")
    clone =URL
    GIT_INIT='git init'
    GIT_SET_MODE='git config core.sparseCheckout true'
    GIT_ADD_REMOTE='git remote add -f origin ' + URL
    GIT_PULL='git pull origin main'
    GIT_SPARSE_CHECKOUT='.git/info/sparse-checkout'
    #create_environment='python3 -mvenv env'
    #use_environment='source '
    #GET_CURRENT_MODULES='python3 -mpip freeze > current.txt'
    PIP_INSTALL='python3 -m pip install -r requirements.txt'
   
    current_path=os.getcwd()
    if os.path.exists("tmp"):
        os.system("rm -rf tmp")
    os.mkdir('tmp')
    os.chdir('tmp') # Specifying the path where the cloned project needs to be copied
    os.system(GIT_INIT)
    os.system(GIT_SET_MODE)
    os.system(GIT_ADD_REMOTE)
    os.system(GIT_PULL)
    filter_modules = open(GIT_SPARSE_CHECKOUT, 'a')
    for module in MODULES:
        filter_modules.write('microfin/' + module)

    filter_modules.close()

    os.system(GIT_PULL)

    print('terminado')
    #os.system(GET_CURRENT_MODULES)

    #os.system(create_environment)
    #subprocess.check_call(['/.env/bin/activate'],executable='source')
    #subprocess.check_call([sys.executable, '-m', 'pip', 'install','-r', 'requirements.txt'])
    dir = join(expanduser("~"), "my-venv")
    dir='env2'
    pip_path=os.getcwd()
    pip_path=pip_path + '/env2/bin/pip'
    print(pip_path)
    create(dir, with_pip=True)
    # requirements
    requirements=open(pip_path+'_requirements.txt', 'a')
    with urllib.request.urlopen(RAW_REQUIREMENTS) as f:
        modules_list = f.read().decode('utf-8')
    requirements.write(modules_list)
    req_path="/home/vladimir/Documents/EFISYS/dev/safi-migracion-deploy/tmp/env2/bin/pip_requirements.txt"
    print(req_path)
    #run([pip_path, "install", "--upgrade","pip"], cwd= 'env2')
    #run([pip_path, "install",  "requests"], cwd='env2')
    print(pip_path)
    
    with open(req_path, "r") as requirements:
        for line in requirements:
            module = line.strip()
            run([pip_path, "install", module], cwd='env2')
    #print(stripped_line)
    requirements.close()
    
    #run([pip_path, "install", "-r pip_requirements.txt"], cwd='env2')
    print('modulos instalados')

    



    
    pass

main()