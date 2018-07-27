"""
Move all the files into the appropriate train/test folder.
"""

import os
import os.path


data_path = 'UCF-101'


def get_train_test_list(version='01'):

    train_file = os.path.join('ucfTrainTestlist', 'trainlist' + version + '.txt')
    test_file = os.path.join('ucfTrainTestlist', 'testlist' + version + '.txt')

    with open(test_file) as f:
        test_list = [row.strip() for row in list(f)]

    with open(train_file) as f:
        train_list = [row.strip() for row in list(f)]
        train_list = [row.split(' ')[0] for row in train_list]

    group_dict = {
        'train': train_list,
        'test': test_list
    }

    return group_dict



def move_files(group_dict):

    for group, video_list in group_dict.items():

        for video in video_list:

            classname = video.split(os.path.sep)[0]
            filename = video.split(os.path.sep)[1]

            # Create folders
            foldername = os.path.join(group, classname)
            if not os.path.exists(foldername):
                print('Creating folder for %s/%s' % (group, classname))
                os.makedirs(foldername)

            # move files
            src = os.path.join(data_path, video)
            dst = os.path.join(group, classname, filename)
            if os.path.exists(src):
                print('Moving %s to %s' % (src, dst))
                os.rename(src, dst)
    
    print('Done')



def main():
    group_dict = get_train_test_list()
    move_files(group_dict)



if __name__ == '__main__':
    main()    