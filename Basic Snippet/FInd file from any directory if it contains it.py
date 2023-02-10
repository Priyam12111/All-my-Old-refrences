from pathlib import Path

dirloc = 'img\diree\dec'
path_of_the_directory = dirloc
paths = Path(path_of_the_directory).glob('**/*.mp4')
for path in paths:
    print(path)  
