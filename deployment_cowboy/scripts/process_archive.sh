#!/bin/sh
unzip archive.zip -d archive
mv archive/build/libs/WebProjectTelerik-0.8.0.jar ./
rm -r archive.zip
rm -r archive