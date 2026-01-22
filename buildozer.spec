[app]

# (str) Title of your application
title = SystemUpdate

# (str) Package name
package.name = sysupdate

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
# Yahan humne requests aur kivy ko version ke sath dala hai taaki error na aaye
requirements = python3,kivy==2.2.1,requests,urllib3,charset-normalizer,idna,certifi

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET, READ_SMS, RECEIVE_SMS

# (int) Android API to use
android.api = 31

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android NDK directory (if empty, it will be automatically downloaded)
android.ndk_path = 

# (str) Android SDK directory (if empty, it will be automatically downloaded)
android.sdk_path = 

# (str) ANT directory (if empty, it will be automatically downloaded)
android.ant_path = 

# (list) Android architectures to build for
android.arch = armeabi-v7a

# (bool) Use the shared library (Android only)
android.library_references = 

# (str) python-for-android branch to use
p4a.branch = master

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
