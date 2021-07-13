# Wallc

A full cli program to manage your wallpaper, i'm creating a marketplace for this project.

# Deprecated

See also: [wl](https://github.com/AlphaTechnolog/wl)

## Installing

```sh
curl -sL https://raw.githubusercontent.com/AlphaTechnolog/wallc/main/install.sh | bash
```

## Uninstalling

```sh
sudo rm -rf /opt/wallc ~/.local/bin/wallc ~/repo/wallc
```

## Instructions

Execute wallc using the next commands sequence:

```sh
wallc config --wallpaper-path ~/Images # -> Indicate the url of wallpapers folder
wallc set -w <WALLPAPER_NAME> -e <WALLPAPER_EXTENSION, jpg, png...> # -> Indicate the name and extension of wallpaper, extension default is: jpg
wallc manage --restore # -> Restore the wallpaper
```

### Profundizing

**First: wallc config**

This command indicate the folder of wallpapers images
if you not indicate the folder, wallc does not know where the image is!
This is the first command you should run

**Syntax:**

```sh
wallc config -wp ~/Images
```

**Second: wallc set**

The `wallc set` command change the wallpaper using the wallpaper_path variable in the config file: `~/.wallc.conf.json`
This command change inmediately your background using the cli program `feh` as subdependecy, **install it!**.
This is the second command you should run!

**Syntax**

```sh
wallc set -w <WALL_NAME> -e <WALL_EXTENSION> # -> default extension: jpg
```

**Third: wallc manage**

The `wallc manage` command is used to restore the wallpaper in your `wm` autostart, example:
in qtile, my autostart is in: `~/.config/qtile/autostart` in it file, i place the next command:

**Syntax**

```sh
wallc manage --restore
```

## Other commands

**show**

Show the available wallpapers in the configurated path

```sh
wallc show
```

**rm**

Remove a wallpaper file

```sh
wallc rm 02 # -> Remove CONFIG_PATH/02.jpg
wallc rm 01 -e png # -> Remove CONFIG_PATH/01.png
```

## Enjoy

Thanks for use wallc.
