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

echo "[INFO]: Installing requirements (requirements.txt)"

cd /opt/wallc

if python3 > /dev/null 2>&1; then
    python3 -m pip install -r requirements.txt > /dev/null 2>&1
else
    python -m pip install -r requirements.txt > /dev/null 2>&1
fi

cd $(dirname $0)

if ! [[ $? == 1 ]]; then
    echo "[SUCCESS]: Installed the requirements"
else
    echo "[FATAL]: Unknown error at install the requirements"
    echo "[PSOLUTION]: Install python as 'python3' on your \$PATH"
    echo "  > And in it, install pip"
    exit 1
fi

sleep 1
echo "[SUCCESS]: Wallc is installed now!"
echo "[INFO]: To start use:"
echo "$ wallc --help"
