import json


def loads_posts() -> list[dict]:
    """Выгружает список json в формате python"""
    with open('posts.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_posts_by_word(word: str) -> list[dict]:
    """Получение нескольких постов по поиску по поиску"""
    result = []
    for post in loads_posts():
        if word.lower() in post['content'].lower():
            result.append(post)
    return result

def add_post(post: dict) -> dict:
    posts: list[dict] = loads_posts()
    posts.append(post)
    with open('posts.json', 'w', encoding='utf-8') as file:
        json.dump(posts, file)
    return post
