# lakeception

Aww yeah, boats!

## Installation

```
# On CentOS
$ sudo yum install SDL-devel libv4l-dev SDL_ttf SDL_ttf-devel
$ cd /usr/include/linux
$ sudo ln -s ../libv4l1-videodev.h videodev.h

$ virtualenv .
$ source bin/activate
$ pip install -r requirements.txt
```
