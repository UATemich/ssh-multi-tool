[app]

title = SSH Multi-Tool

package.name = sshmultitool
package.domain = local

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy==2.3.0,kivymd==1.1.1,paramiko

orientation = portrait

fullscreen = 0

android.permissions = INTERNET,WAKE_LOCK

android.api = 33
android.minapi = 24
android.sdk = 33
android.ndk = 25b

android.accept_sdk_license = True

android.archs = arm64-v8a

p4a.branch = master

[buildozer]

log_level = 2
warn_on_root = 1
