#!/bin/bash

cd $HOME
mkdir -p $HOME/repo
cd $HOME/repo
echo "Cloning wallc..."

if [ -d $HOME/repo/wallc ]; then
    echo "Wallc already cloned... stoping"
    echo "[SOLUTION]: Remove the folder $HOME/repo/wallc"
    exit 1
fi

git clone https://github.com/AlphaTechnolog/wallc.git wallc > /dev/null 2>&1
cd $HOME/repo/wallc
echo "Installing wallc in /opt/wallc"

if [ -d /opt/wallc ]; then
    echo "Wallc already installed in /opt/wallc... stoping"
    echo "[SOLUTION]: Remove the folder /opt/wallc"
    exit 1
fi

sudo mkdir /opt/wallc
sudo cp -r ./* /opt/wallc

echo "Creating the symlink..."

if [ -f $HOME/.local/bin/wallc ]; then
    echo "Wallc already installed... stoping"
    echo "[SOLUTION]: Remove the file $HOME/.local/bin/wallc and exec:"
    echo "  >> $ sudo ln -s /opt/wallc/src/main.py $HOME/.local/bin/wallc"
    exit 1
fi

sudo ln -s /opt/wallc/src/main.py $HOME/.local/bin/wallc

echo "Installing requirements"

python3 -m pip install -r /opt/wallc/requirements.txt > /dev/null 2>&1

if [[ $? == 0 ]]; then
    echo "Installed the requirements"
else
    echo "Could'nt install requirements!"
    echo "If you want have the python libs: requests, cli-app, colorama all is good!"
    echo "else see the solution:"
    echo "[SOLUTION]: run:"
    echo "  > $ cd $HOME/repo/wallc/"
    echo "  > $ python3 -m pip install -r requirements.txt"
    exit 1
fi

echo "Wallc is now installed!"
