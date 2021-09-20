from django.shortcuts import render
from .models import icecream_db


# Вторым аргументом эта функция должна принять переменную pk из path()
def icecream_detail(request, pk):
    # Получите из icecream_db отдельно название
    # и отдельно описание запрошенного мороженого.
    # Сохраните их, соответственно, в переменные name и description
    name = icecream_db[pk]["name"]
    description = icecream_db[pk]["description"]
    context = {
        'name': name,
        'description': description,
    }
    return render(request, 'icecream/icecream-detail.html', context)
