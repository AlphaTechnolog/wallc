#!/bin/bash

cd `dirname $0`

echo "[INFO]: Copying source code to '/opt/wallc'"

if [ -d /opt/wallc ]; then
    echo "[ERROR]: Wallc already installed..."
    echo "[SOLUTION]: Remove the folder '/opt/wallc'"
    exit 1
fi

sudo mkdir -p /opt/wallc
sudo cp -r ./* /opt/wallc

echo "[SUCCESS]: Copied the source code to '/opt/wallc'"
echo "[INFO]: Creating symlink"

sudo ln -s /opt/wallc/src/main.py $HOME/.local/bin/wallc
sudo chmod -R 777 $HOME/.local/bin/wallc

echo "[SUCCESS]: Created the symlink..."

sleep 1
echo "[SUCCESS]: Wallc is installed now!"
echo "[INFO]: To start use:"
echo "$ wallc --help"
