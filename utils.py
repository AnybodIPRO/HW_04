import json


def load_posts(path='posts.json'):
    posts = []
    with open(path, 'r', encoding="utf-8") as file:
        posts = json.load(file)
    return posts


def search_posts(substr):
    found_posts = []
    json_posts = load_posts()
    for post in json_posts:
        if substr in post['content']:
            found_posts.append(post)
       # else:
         #   print('По запросу ничего не найдено')
    return found_posts


def save_picture(picture):
    filename = picture.filename
    filetype = filename.split('.')[-1]
    if filetype not in ['jpg', 'jpeg', 'svg', 'png']:
        exit
    picture.save(f'./uploads/images/{filename}')
    return f'/uploads/images/{filename}'


def add_post(post):
    posts = load_posts()
    posts.append(post)
    posts_load_to_json(posts)
    return posts



def posts_load_to_json(post, path='posts.json'):
    with open(path, 'w', encoding="utf-8") as file:
        json.dump(post, file, ensure_ascii=False)
