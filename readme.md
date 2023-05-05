# py amazfit tool
An python port of valeronm's amazfitbiptools(v.1.0.3.1) adapted for Bip S.

All credit goes to Валерий Миронов(https://bitbucket.org/valeronm/amazfitbiptools/src/master/)

## what is...
* can pack/unpack .bin file for amazfit Bip S / Bip S lite

## requirements
* python3(tested on 3.7.4)
* pillow(tested on 6.1.0)

## usage
* to unpack
  * python main.py WATCH_FACE_FILE.bin
* to pack
  * python main.py WATCH_FACE_FILE.json
* to disable dithering and color conversion to EGA64 palette use --nodither param
  * python main.py --nodither WATCH_FACE_FILE.json
* to pack / unpack files for / from old Bip use --old param
  * python main.py --old WATCH_FACE_FILE.json