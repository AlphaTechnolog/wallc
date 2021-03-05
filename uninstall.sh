#!/bin/bash

cd $(dirname $0)

echo "[INFO]: Comprobations..."

wallc_not_installed() {
    echo "[ERROR]: Wallc is not installed!"
    echo "[SOLUTION]: Install it running (second command or third command)"
    echo "$ cd $(dirname $0)"
    echo "$ ./install.sh"
    echo "$ ./local_install.sh"
    exit 1
}

if [[ ! -d /opt/wallc || ! -f $HOME/.local/bin/wallc ]]; then
    wallc_not_installed
fi

echo "[SUCCESS]: System is healty"
echo "[INFO]: Deleting source code in '/opt/wallc'"

sudo rm -rf /opt/wallc

echo "[SUCCESS]: Deleted source code"

if [[ $1 == '--purge' || $1 == '-p' ]]; then
    echo "[INFO]: Purging config file in '$HOME/.wallc.conf.json'"
    
    if [ -f $HOME/.wallc.conf.json ]; then
        rm $HOME/.wallc.conf.json
        echo "[SUCCESS]: Purged the config file!"
    else
        echo "[ERROR]: The configuration file does not exists"
        echo "  > Did you not use it?"
        echo "  > Passing..."
    fi
fi

echo "[INFO]: Removing symlink"
sudo rm $HOME/.local/bin/wallc
echo "[SUCCESS]: Removed symlink"

echo "[SUCCESS]: Wallc is removed successfully!"
