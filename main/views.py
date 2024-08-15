from django.shortcuts import render

from goods.models import Categories


def index(request):

    categories = Categories.objects.all()

    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
        'categories': categories,
    }

    return render(request, 'main/index.html', context)


def about(request):
     context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Магазин мебели HOME предлагает высококачественную мебель, которая сочетает в себе стиль, комфорт и долговечность. В нашем ассортименте вы найдете широкий выбор товаров для дома: удобные диваны и кресла, функциональные столы и стулья, просторные шкафы и комоды. Каждый предмет мебели выполнен с вниманием к деталям и из качественных материалов, что гарантирует их долговечность и прочность. Мы стремимся предложить нашим клиентам лучшие решения для создания уютного и стильного интерьера, который будет радовать вас долгие годы.'

    }
     return render(request, 'main/about.html', context)
