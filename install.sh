#!/bin/bash

cd $HOME
mkdir -p $HOME/repo
cd $HOME/repo
echo "Cloning wallc..."

if [ -d $HOME/repo/wallc ]; then
    echo "Pytrogen already cloned... stoping"
    echo "[SOLUTION]: Remove the folder $HOME/repo/wallc"
    exit 1
fi

git clone https://github.com/AlphaTechnolog/wallc.git wallc > /dev/null 2>&1
cd $HOME/repo/wallc
echo "Installing wallc in /opt/wallc"

if [ -d /opt/wallc ]; then
    echo "Pytrogen already installed in /opt/wallc... stoping"
    echo "[SOLUTION]: Remove the folder /opt/wallc"
    exit 1
fi

sudo mkdir /opt/wallc
sudo cp -r ./* /opt/wallc

echo "Creating the symlink..."

if [ -f $HOME/.local/bin/wallc ]; then
    echo "Pytrogen already installed... stoping"
    echo "[SOLUTION]: Remove the file $HOME/.local/bin/wallc and exec:"
    echo "  >> $ sudo ln -s /opt/wallc/src/main.py $HOME/.local/bin/wallc"
    exit 1
fi

sudo ln -s /opt/wallc/src/main.py $HOME/.local/bin/wallc

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

echo "Pytrogen is now installed!"
