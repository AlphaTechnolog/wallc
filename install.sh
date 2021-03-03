#!/bin/bash

cd $HOME
mkdir -p $HOME/repo
cd $HOME/repo
echo "Cloning pytrogen..."

if [ -d $HOME/repo/pytrogen ]; then
    echo "Pytrogen already cloned... stoping"
    echo "[SOLUTION]: Remove the folder $HOME/repo/pytrogen"
    exit 1
fi

git clone https://github.com/AlphaTechnolog/pytrogen.git pytrogen > /dev/null 2>&1
cd $HOME/repo/pytrogen
echo "Installing pytrogen in /opt/pytrogen"

if [ -d /opt/pytrogen ]; then
    echo "Pytrogen already installed in /opt/pytrogen... stoping"
    echo "[SOLUTION]: Remove the folder /opt/pytrogen"
    exit 1
fi

sudo mkdir /opt/pytrogen
sudo cp -r ./* /opt/pytrogen

echo "Creating the symlink..."

if [ -f $HOME/.local/bin/pytrogen ]; then
    echo "Pytrogen already installed... stoping"
    echo "[SOLUTION]: Remove the file $HOME/.local/bin/pytrogen and exec:"
    echo "  >> $ sudo ln -s /opt/pytrogen/src/main.py $HOME/.local/bin/pytrogen"
    exit 1
fi

sudo ln -s /opt/pytrogen/src/main.py $HOME/.local/bin/pytrogen

echo "Pytrogen is now installed!"
