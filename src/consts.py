import sys

ARE_ACHIEVEMENTS_IMPLEMENTED = False

LOG_SENSITIVE_DATA = False

MANIFEST_URL = r"https://gamedownloads-rockstargames-com.akamaized.net/public/title_metadata.json"

IS_WINDOWS = (sys.platform == 'win32')

ROCKSTAR_LAUNCHERPATCHER_EXE = "LauncherPatcher.exe"
ROCKSTAR_LAUNCHER_EXE = "Launcher.exe"  # It's a terribly generic name for a launcher.

USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 "
              "Safari/537.36")

WINDOWS_UNINSTALL_KEY = "SOFTWARE\\WOW6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\"

AUTH_PARAMS = {
    "window_title": "Login to Rockstar Games Social Club",
    "window_width": 700,
    "window_height": 600,
    "start_uri": "https://www.rockstargames.com/auth/scauth-login",
    "end_uri_regex": r"https://scapi.rockstargames.com/profile/getbasicprofile"
                    # r"https://www.rockstargames.com/auth/get-user.json.*"
}


class NoLogFoundException(Exception):
    pass


class NoGamesInLogException(Exception):
    pass
