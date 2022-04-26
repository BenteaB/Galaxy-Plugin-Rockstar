# NOTICE: If you are getting issues regarding the plugin crashing upon logging in, please refer to issue [#158][tagIssue] before creating a new one.

# Rockstar Games Integration for GOG Galaxy 2.0

This plugin adds unofficial integration with the Rockstar Games Social Club and the Rockstar Games Launcher for GOG Galaxy 2.0.

## Windows Installation:
Extract the plugin.zip directory from [the releases section of this repository][rel] and place the entire Rockstar folder within the plugins directory. If the plugin was installed correctly, then your directory tree will look like this:

```sh
C:\Users\[Your-Username]\AppData\Local\GOG.com\Galaxy\plugins\installed\Rockstar
```

In the above directory listing, [Your-Username] is the name of your current user profile. If you are unsure of your computer user name, this directory is the same as the one above:

```sh
%LOCALAPPDATA%\GOG.com\Galaxy\plugins\installed\Rockstar
```

## Mac Installation:
Extract the plugin.zip directory from [the releases section of this repository][rel] and place the entire Rockstar folder within the plugins directory. If the plugin was installed correctly, then your directory tree will look like this:

```sh
~/Library/Application Support/GOG.com/Galaxy/plugins/installed/Rockstar
```

#### NOTE: The Rockstar Games Launcher is only available on Windows. As such, the Mac version of the plugin only includes features relating to the Rockstar Games Social Club. Namely, Mac users will not be able to install, uninstall, or launch games purchased on the Rockstar Games Launcher. In addition, only the games which have been played on a Windows device will be listed in the games library.

## Additional Notes:
  - There is currently no support for achievements, although it will be implemented later. However, friend recommendations are supported, and with the release of v0.3, basic game time tracking is also available. **Please note that game time is only tracked if the user launches the game through Galaxy 2.0.**
  - To get the user's games library, the plugin seeks the authenticated user's list of played games from the Rockstar website and, if possible, filters the list using the log file generated by the Rockstar Games Launcher. (On the Mac version of the plugin, only the list of played games from the Rockstar website is used.)
  - Please report any bugs that you find at [the issues section of this repository][issues], especially those regarding the Mac version of the plugin. Make sure to specify which operating system family (Windows or Mac) you are using.

[rel]: <https://github.com/tylerbrawl/Galaxy-Plugin-Rockstar/releases>
[issues]: <https://github.com/tylerbrawl/Galaxy-Plugin-Rockstar/issues>
[tagIssue]: <https://github.com/tylerbrawl/Galaxy-Plugin-Rockstar/issues/158>
