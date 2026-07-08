#!/bin/bash

SRC="$1"
DST="$2"

if [[ -z "$SRC" || -z "$DST" ]]; then
    echo "Usage: $0 <source-folder> <destination-folder>"
    exit 1
fi

ICONS=(
    apachecloudstack
    appeon
    application-platforms
    atos
    awsfirehose
    bulma
    circleci
    codecov
    codepen
    dotnetado
    filezilla
    fujitsu
    fullcalendar
    gatling
    ghostjs
    gitter
    gnucobol
    harshicorp
    hivemq
    hp
    illustrator
    jasmine
    ocelot
    payloadcms
    petapoco
    photoshop
    powerbi
    rubysinatra
    sea
    ubuntu
    unisys
    vms
    wt
    xd
)

for icon in "${ICONS[@]}"; do
    mkdir -p "$DST/$icon"
    cp "$SRC/$icon/${icon}-original.svg" "$DST/$icon/"
done

echo "Copied ${#ICONS[@]} icons from $SRC to $DST."