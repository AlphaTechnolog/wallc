# Pytrogen

Nitrogen writed in python

## Installing

```sh
curl -sL https://raw.githubusercontent.com/AlphaTechnolog/pytrogen/main/install.sh | bash
```

## Uninstalling

```sh
sudo rm -rf /opt/pytrogen ~/.local/bin/pytrogen ~/repo/pytrogen
```

## Instructions

Execute pytrogen using the next commands sequence:

```sh
pytrogen config --wallpaper-path ~/Images # -> Indicate the url of wallpapers folder
pytrogen set -w <WALLPAPER_NAME> -e <WALLPAPER_EXTENSION, jpg, png...> # -> Indicate the name and extension of wallpaper, extension default is: jpg
pytrogen manage --restore # -> Restore the wallpaper
```

### Profundizing

**First: pytrogen config**

This command indicate the folder of wallpapers images
if you not indicate the folder, pytrogen does not know where the image is!
This is the first command you should run

**Syntax:**

```sh
pytrogen config -wp ~/Images
```

**Second: pytrogen set**

The `pytrogen set` command change the wallpaper using the wallpaper_path variable in the config file: `~/.pytrogen.conf.json`
This command change inmediately your background using the cli program `feh` as subdependecy, **install it!**.
This is the second command you should run!

**Syntax**

```sh
pytrogen set -w <WALL_NAME> -e <WALL_EXTENSION> # -> default extension: jpg
```

**Third: pytrogen manage**

The `pytrogen manage` command is used to restore the wallpaper in your `wm` autostart, example:
in qtile, my autostart is in: `~/.config/qtile/autostart` in it file, i place the next command:

**Syntax**

```sh
pytrogen manage --restore
```

## Enjoy

Thanks for use pytrogen.
