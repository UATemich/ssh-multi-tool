[app]

title = SSH Multi-Tool

package.name = sshmultitool
package.domain = local

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3==3.10.11,kivy==2.3.0,kivymd==1.1.1,paramiko,cryptography,bcrypt,pynacl

orientation = portrait

fullscreen = 0

android.permissions = INTERNET,WAKE_LOCK

android.archs = arm64-v8a

[buildozer]

log_level = 2
warn_on_root = 1
