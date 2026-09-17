[app]
title = Dino Runner 2 Ultimate
package.name = dinorunner2
package.domain = org.dino.runner

source.dir = .
source.include_exts = py,png,jpg,jpeg,wav,ogg,mp3,ttf,json,txt

version = 2.0

# numpy solo se usa para la musica y los efectos; si la compilacion falla, dejalo en: python3,pygame
requirements = python3,pygame,numpy

orientation = landscape
fullscreen = 1

android.presplash_color = #0A1428
android.archs = arm64-v8a,armeabi-v7a
android.allow_backup = True
android.api = 33
android.minapi = 21

# Descomenta y apunta a tus archivos si agregas icono/splash propios:
# icon.filename = %(source.dir)s/icon.png
# presplash.filename = %(source.dir)s/presplash.png

[buildozer]
log_level = 2
warn_on_root = 1
