## SkinReaper

Python module that can be used to gather a list of skins or one random Minecraft skin from [minecraftskins.com](https://minecraftskins.com) website. It has more featuers like getting preview link for the random skin or saving data to a file.

### Warning!

The default max limit for downloading pages with list of skins is set to **10**.
Why? You don't want to send to many requests - owners of this website would not enjoy watching their website lag because you are downloading millions of skins.

> **I am not responsible for damage caused by it! Use it wisely and don't send too many requests!**

### Requirements

You need to have *selenium* module installed:

    pip install selenium

Also in the same directory that the module is located you should have geckodriver.exe which can be downloaded [here](https://github.com/mozilla/geckodriver/releases).

Make sure that Firefox is added to the PATH.