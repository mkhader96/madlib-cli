
import re

print(
'''☆☆☆ Welcome to Madlib Creation Game ☆☆☆
☆☆☆ Madlib is a game where you decide the parts of the story ☆☆☆
☆☆☆ You will be asked to input multiple values for the game ☆☆☆
☆☆☆ Make your answers creative to make the game entertaining ☆☆☆
''')

def read_template(test):
    if test == 'assets/make_me_a_video_game_template.txt' or test == 'assets/dark_and_stormy_night_template.txt':
        with open(test) as f:
            content = f.read()
            return content
    
    else:
        raise FileNotFoundError

            

def parse_template(test):
    
        stripped = re.sub(r'[^{\}]+(?=})', '', test)
        parts = re.findall(r'[^{\}]+(?=})', test)
        return stripped, tuple(parts)
        

def  merge(stripped, parts):
    return stripped.format(*parts)

def madlib():
    test = 'assets/dark_and_stormy_night_template.txt'
    content = read_template(test)
    stripped, parts = parse_template(content)
    values = []
    for part in parts:
        value = input(f'Please enter a {part}: ')
        values.append(value)
    story = merge(stripped, values)
    
    print(story)
    return story


def save(story):
    path = 'assets/madlib.txt'
    with open(path, 'w') as f:
        f.write(story)
        print('Your madlib has been saved')

save(madlib())


    
   

