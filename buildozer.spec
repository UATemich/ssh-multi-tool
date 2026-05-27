[app]

title = SSH Multi Tool
package.name = sshmultitool
package.domain = org.temich

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,json

version = 1.0

requirements = python3==3.10.11,kivy==2.2.1,kivymd==1.1.1,paramiko,cryptography,bcrypt,pynacl

orientation = portrait
fullscreen = 0

# ---------- ANDROID ----------

android.api = 33
android.minapi = 24
android.sdk = 33
android.ndk = 25b

android.archs = arm64-v8a

android.accept_sdk_license = True

android.permissions = INTERNET

android.release_artifact = apk

# ---------- PYTHON-FOR-ANDROID ----------

p4a.branch = develop

osx.python_version = 3

# ---------- BUILD ----------

build_dir = .buildozer

log_level = 2

warn_on_root = 1

# ---------- OPTIONAL ----------

# icon.filename = %(source.dir)s/data/icon.png
# presplash.filename = %(source.dir)s/data/presplash.png

# ---------- END ----------
