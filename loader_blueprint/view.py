"""для загрузки фото"""
from flask import Blueprint, render_template,request

from utils import save_picture
from utils import add_post
from utils import search_posts

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates', url_prefix='/')

@loader_blueprint.route('/post')
def create_post():
    return render_template('post_form.html')

@loader_blueprint.route('/post', methods=['POST'])
def upload_post():
    picture = request.files.get('picture')
    post_content = request.form.get('content')

    picture_url = save_picture(picture)
    if not picture_url:
        return 'Не правильный формат изображения'

    add_post({'pic': picture_url, 'content': post_content})

    #return f'Content:{post_content}, picture: {picture.filename}, Path:{picture_url}, type='
    return render_template('post_uploaded.html', post_content=post_content, picture=picture_url)

