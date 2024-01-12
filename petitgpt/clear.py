# read all txt files in a directory and save them as a single txt file

import os

FILE_NAME = 'all_texts.txt'

for filename in os.listdir('.'):
    if filename.endswith('.txt'):
        with open(filename, 'r') as f:
            text = f.read()
        # remove the last line
        text = text[:text.rfind('\n')]
        text = text.replace('\n\n', ' ').replace('[wlǎn nú | wla nú ɖoɖo ɔ]', '').replace(" ", " ")
        # check if the file is in the all_texts.txt file
        if os.path.isfile(FILE_NAME):
            with open(FILE_NAME, 'r') as f:
                if text in f.read():
                    continue
        with open(FILE_NAME, 'a') as f:
            f.write(text)
            f.write('\n\n')
