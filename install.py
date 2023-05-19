
import os
from os.path import join, expanduser, abspath
from subprocess import run

import sys

import urllib.request
import venv
import subprocess
import venv 
from time import sleep


#import requests

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
 
 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
 
 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
 
 
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
 
 
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
 
 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
 
 
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
 
 
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))

def print_comment(skk): 
    print("\033[97m {}\033[00m" .format(skk))
    sleep(2)
def print_info(skk): 
    print("\033[96m {}\033[00m" .format(skk))
    sleep(2)

def main(): 
    URL='https://github.com/VladimirJz/efisys-migracion-db.git'
    MODULES=['clientes']
    RAW_REQUIREMENTS='https://raw.githubusercontent.com/VladimirJz/safi-migracion-repository/main/requirements.txt'
    HOME='.safi_migracion'
    #os.system("sshpass -p your_password ssh user_name@your_localhost")
    clone =URL
    PIP='/env/bin/pip'
    GIT_INIT='git init'
    GIT_SET_MODE='git config core.sparseCheckout true'
    GIT_ADD_REMOTE='git remote add -f origin ' + URL
    GIT_PULL='git pull origin main'
    GIT_SET_BRANCH='git config --global init.defaultBranch main'
    GIT_SPARSE_CHECKOUT='.git/info/sparse-checkout'
    #create_environment='python3 -mvenv env'
    #use_environment='source '
    #GET_CURRENT_MODULES='python3 -mpip freeze > current.txt'
    #PIP_INSTALL='python3 -m pip install -r requirements.txt'
    print_info('Efisys- Migracion')
    print_info('start..')
    current_path=os.getcwd()
    if os.path.exists(HOME):
        os.system(f"rm -rf { HOME }")
    os.mkdir(HOME)
    os.chdir(HOME) # Specifying the path where the cloned project needs to be copied
    os.system(GIT_INIT)
    os.system(GIT_SET_BRANCH)
    os.system(GIT_SET_MODE)
    os.system(GIT_ADD_REMOTE)
    os.system(GIT_PULL)
    filter_modules = open(GIT_SPARSE_CHECKOUT, 'a')
    print_info('reading modules..')
    for module in MODULES:
        filter_modules.write('microfin/' + module)

    filter_modules.close()
    print_info('updating resources..')
    os.system(GIT_PULL)
    print_info('updating resources.. done')
    
    #os.system(GET_CURRENT_MODULES)

    #os.system(create_environment)
    #subprocess.check_call(['/.env/bin/activate'],executable='source')
    #subprocess.check_call([sys.executable, '-m', 'pip', 'install','-r', 'requirements.txt'])
    print_info('setting enviroment..')
    venv.create('env', with_pip=True)
    print_info('setting enviroment.. done')
    pip_path=os.getcwd() + PIP
    #pip_path=os.path.abspath('env') + ''

    #print(f'pip {pip_path} ')
    #pip_path=HOME + PIP
    print_info('install dependencies..')
    with urllib.request.urlopen(RAW_REQUIREMENTS) as f:
        modules_list = f.read().decode('utf-8').split("\n")
    
    modules_list = [i for i in modules_list if i]
    run([pip_path, "install", "--upgrade","pip"], cwd= 'env')
    for module in modules_list:
        run([pip_path, "install", module], cwd='env')
    
    print_info('install dependencies.. done')
    print_comment(pip_path)

    exit()
    
    env_dir = join(expanduser("~"), ".safi")
    print(f'env :{env_dir}')
    #dir='env2'
    env_dir
    pip_path=os.getcwd()
    pip_path=pip_path + '/env2/bin/pip'
    print(pip_path)
    venv.create(dir, with_pip=True)
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