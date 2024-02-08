import os

FILE_NAME = 'all_texts.txt'
seen_texts = set()

for filename in os.listdir('.'):
    if filename.endswith('.txt') and filename != FILE_NAME:
        with open(filename, 'r') as f:
            text = f.read()
        text = text[:text.rfind('\n')]
        text = text.replace('\n\n', ' ').replace('[wlǎn nú | wla nú ɖoɖo ɔ]',
                                                 '').replace(" ", " ")

        if text not in seen_texts:
            with open(FILE_NAME, 'a+') as f:
                f.write(text)
                f.write('\n\n')
            seen_texts.add(text)
