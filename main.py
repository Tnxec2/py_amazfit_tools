import os
import logging

from watchFaceParser.config import Config

if __name__ == '__main__':
    import sys
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--nodither', action='store_true', help='convert images to 64 RGB with dithering')
    parser.add_argument('--old', action='store_true', help='unpack old bip watchface bin')
    parser.add_argument('filename', nargs='+', help='''watchface.bin - unpacks watchface images and config
    watchface.json - packs config and referenced images to bin file''')
    args = parser.parse_args()

    Config.setDither(args.nodither)
    Config.setOldBip(args.old)

    for inputFileName in args.filename:
        isDirectory = os.path.isdir(inputFileName)
        isFile = os.path.isfile(inputFileName)
        if not isDirectory and not isFile:
            print("File or direcotry %s doesn't exists." % (inputFileName, ))
            continue
        if isDirectory:
            print("Not supported yet.")
            sys.exit(1)
        _, inputFileExtension = os.path.splitext(inputFileName)
        try:
            import program
            if inputFileExtension == '.bin':
                program.Parser.unpackWatchFace(inputFileName)
            elif inputFileExtension == '.json':
                if Config.isDither(): 
                    print(f'Image are to {Config._ditherDepth} Bit color coverted. Set --nodither argument to do not dither images.')
                program.Parser.packWatchFace(inputFileName)
            else:
                print("The app doesn't support file with extension %s." % (inputFileExtension, ))
            print("Done")
        except Exception as e:
            print('[Fatal] %s' % (e, ))
            import traceback
            traceback.print_stack()
            logging.exception(e)

