from django.http import Http404
from django.shortcuts import render

posts = [
    {
        'id': 0,
        'location': 'Остров отчаянья',
        'date': '30 сентября 1659 года',
        'category': 'travel',
        'text': '''Наш корабль, застигнутый в открытом море
                страшным штормом, потерпел крушение.
                Весь экипаж, кроме меня, утонул; я же,
                несчастный Робинзон Крузо, был выброшен
                полумёртвым на берег этого проклятого острова,
                который назвал островом Отчаяния.''',
    },
    {
        'id': 1,
        'location': 'Остров отчаянья',
        'date': '1 октября 1659 года',
        'category': 'not-my-day',
        'text': '''Проснувшись поутру, я увидел, что наш корабль сняло
                с мели приливом и пригнало гораздо ближе к берегу.
                Это подало мне надежду, что, когда ветер стихнет,
                мне удастся добраться до корабля и запастись едой и
                другими необходимыми вещами.''',
    },
    {
        'id': 2,
        'location': 'Остров отчаянья',
        'date': '25 октября 1659 года',
        'category': 'not-my-day',
        'text': '''Всю ночь и весь день шёл дождь и дул сильный
                порывистый ветер.''',
    },
]

posts_by_id = {post['id']: post for post in posts}


def index(request):
    template = 'blog/index.html'

    context = {
        'post_list': posts[::-1]
    }

    return render(request, template, context)


def post_detail(request, post_id):
    template = 'blog/detail.html'

    post = posts_by_id.get(post_id)

    if post is None:
        raise Http404(f'Пост с id={post_id} не найден')

    context = {
        'post': post
    }

    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'

    post_list = [
        post for post in posts
        if post['category'] == category_slug
    ]

    context = {
        'category_slug': category_slug,
        'post_list': post_list,
    }

    return render(request, template, context)
