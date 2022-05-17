from datetime import datetime
from random import randint
from django.shortcuts import redirect, render
from news.utils import add_news, get_data_news, get_sorted_news, group_news_by_date


def index(request):
    data = get_sorted_news(get_data_news())

    if request.GET.get('q'):
        q = request.GET.get('q')
        filtered_data = [n for n in data if n['title'].find(q) >= 0]
        news = group_news_by_date(filtered_data)
        context = {'news': news}
    else:
        news = group_news_by_date(data)
        context = {'news': news}
    return render(request, 'news/index.html', context)


def detail(request, news_link: int):
    data = get_data_news()
    for i in data:
        if i['link'] == news_link:
            context = {'news': i}
    return render(request, 'news/detail.html', context)


def create_news(request):
    if request.method == 'POST':
        data = get_data_news()

        links = [i['link'] for i in data]

        while True:
            new_link = randint(0, 1_000_000)
            if new_link not in links:
                links.append(new_link)
                break
        news = {
                'created': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'text': request.POST.get('text'),
                'title': request.POST.get('title'),
                'link': new_link
            }
        add_news(data, news)

        return redirect('/news/')
    return render(request, 'news/create.html')