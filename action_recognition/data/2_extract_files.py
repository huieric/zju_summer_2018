"""
1. Extract the images from the videos.
2. Create a csv file recording data of train and test.
"""

import csv
import glob
import os
import os.path
from subprocess import call


def extract_images():
    rows = []
    group_list = ['train', 'test']

    for group in group_list:
        classname_list = glob.glob(os.path.join(group, '*'))
        classname_list = [classname.split(os.path.sep)[1] for classname in classname_list]
        for classname in classname_list:
            video_list = glob.glob(os.path.join(group, classname, '*.avi'))
            for video in video_list:
                filename = video.split(os.path.sep)[2]
                filename_no_ext = filename.split('.')[0]

                # extract images from videos
                if not os.path.exists(os.path.join(group, classname, filename_no_ext + '-0001.jpg')):
                    dst = os.path.join(group, classname, filename_no_ext + '-%04d.jpg')
                    call(['ffmpeg', '-i', video, dst])

                n_frames = len(glob.glob(os.path.join(group, classname, filename_no_ext + '*.jpg')))
                rows.append([group, classname, filename_no_ext, n_frames])
                print('Generated %d frames for %s' % (n_frames, filename_no_ext))

    with open('extract.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    print('Extracted and wrote %d video files' % (len(rows)))



def main():
    extract_images()



if __name__ == '__main__':
    main()        
