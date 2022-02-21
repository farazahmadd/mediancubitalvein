


full_path_to_images = '/home/admin/Downloads/video-to-annotate'

c = 0

with open(full_path_to_images + '/' + 'classes.names', 'w') as names, \
     open(full_path_to_images + '/' + 'classes.txt', 'r') as txt:

    # Going through all lines in txt file and writing them into names file
    for line in txt:
        names.write(line)  # Copying all info from file txt to names

        # Increasing counter
        c += 1


with open(full_path_to_images + '/' + 'labelled_data.data', 'w') as data:


    data.write('classes = ' + str(c) + '\n')

    data.write('train = ' + full_path_to_images + '/' + 'train.txt' + '\n')

    data.write('valid = ' + full_path_to_images + '/' + 'test.txt' + '\n')

    data.write('names = ' + full_path_to_images + '/' + 'classes.names' + '\n')

    data.write('backup = backup')
