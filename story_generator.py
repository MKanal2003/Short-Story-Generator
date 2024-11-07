import os

def get_user_input():
    name = input("Enter the character's name: ")
    setting = input("Enter the setting: ")
    weather = input("Enter the weather: ")
    object = input("Enter the mysterious object: ")
    return name, setting, weather, object

def generate_story(name, setting, weather, object):
    with open("story_template.txt", "r") as f:
        template = f.read()
    story = template.replace("{name}", name).replace("{setting}", setting).replace("{weather}", weather).replace("{object}", object)
    return story

def main():
    name, setting, weather, object = get_user_input()
    story = generate_story(name, setting, weather, object)
    print(story)

if __name__ == "__main__":
    main()