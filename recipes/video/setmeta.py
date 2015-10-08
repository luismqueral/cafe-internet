NAME = "video.setmeta"

import subprocess
from tempfile import NamedTemporaryFile

from recipe import recipes


# ffmpeg -i [input] -i [metadata input] -map_metadata 1 -codec copy [output]

class SetMeta(object):
    def __init__(self, **metadata):
        self.metafile = NamedTemporaryFile('w')
        meta = ";FFMETADATA1\n"
        for i in metadata:
            meta += "{key}={value}\n".format(key=str(i), value=str(metadata[i]))
        self.metafile.write(meta)
        self.metafile.flush()

    def run(self, input):
        processedvideos = []
        for video in input:
            try:
                path = video.name
            except AttributeError:
                path = video

            processedvideo = NamedTemporaryFile('r')
            subprocess.call(['ffmpeg', '-i', path, '-i', self.metafile.name, '-map_metadata', '1', '-codec', 'copy',
                             processedvideo.name])
            processedvideos.append(processedvideo)

        return processedvideos


recipes[NAME] = SetMeta
