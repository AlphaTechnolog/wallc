#!/bin/bash

cd $HOME
mkdir -p $HOME/repo
cd $HOME/repo
echo "Cloning wllc..."

if [ -d $HOME/repo/wllc ]; then
    echo "Pytrogen already cloned... stoping"
    echo "[SOLUTION]: Remove the folder $HOME/repo/wllc"
    exit 1
fi

git clone https://github.com/AlphaTechnolog/wllc.git wllc > /dev/null 2>&1
cd $HOME/repo/wllc
echo "Installing wllc in /opt/wllc"

if [ -d /opt/wllc ]; then
    echo "Pytrogen already installed in /opt/wllc... stoping"
    echo "[SOLUTION]: Remove the folder /opt/wllc"
    exit 1
fi

sudo mkdir /opt/wllc
sudo cp -r ./* /opt/wllc

echo "Creating the symlink..."

if [ -f $HOME/.local/bin/wllc ]; then
    echo "Pytrogen already installed... stoping"
    echo "[SOLUTION]: Remove the file $HOME/.local/bin/wllc and exec:"
    echo "  >> $ sudo ln -s /opt/wllc/src/main.py $HOME/.local/bin/wllc"
    exit 1
fi

sudo ln -s /opt/wllc/src/main.py $HOME/.local/bin/wllc

echo "Pytrogen is now installed!"
