
# Laboratorium 7 Python + Redis + Django


Sprawdzenie połączenia z redis:
![App](https://github.com/EllwartDawid/aplikacje-internetowe-21788-185ic/blob/master/Laboratorium7/ss/przyklad1.PNG)

Przypisanie wartości:
![App](https://github.com/EllwartDawid/aplikacje-internetowe-21788-185ic/blob/master/Laboratorium7/ss/przyklad2.PNG) 

Dodanie ``decode-responses=True``:
![App](https://github.com/EllwartDawid/aplikacje-internetowe-21788-185ic/blob/master/Laboratorium7/ss/przyklad2a.PNG) 

Append (dodaje wartość do klucza), delete (usuwa klucz)
![App](https://github.com/EllwartDawid/aplikacje-internetowe-21788-185ic/blob/master/Laboratorium7/ss/przyklad2b.PNG) 

Dodanie i odejmowanie: set (usuwa wartość klucza), incr (zwiększa wartość klucza), decr (zmniejsza wartość klucza)
![App](https://github.com/EllwartDawid/aplikacje-internetowe-21788-185ic/blob/master/Laboratorium7/ss/przyklad2c.PNG)  


## Listy

rpush (dodaje elementy do listy), lrange (zwraca elementy listy)
![App](https://github.com/EllwartDawid/aplikacje-internetowe-21788-185ic/blob/master/Laboratorium7/ss/przyklad3.PNG) 

Drugi przykład:
![App](https://github.com/EllwartDawid/aplikacje-internetowe-21788-185ic/blob/master/Laboratorium7/ss/przyklad3a.PNG) 

brpop (zwraca ostatni element listy), robi to w pętli do momentu kiedy skończy się lista
![App](https://github.com/EllwartDawid/aplikacje-internetowe-21788-185ic/blob/master/Laboratorium7/ss/przyklad3b.PNG) 

db (połączenie z bazą danych). Zapisujemy dane na bazie zerowej (domyślnej), a odczytujemy na pierwszej 
![App](https://github.com/EllwartDawid/aplikacje-internetowe-21788-185ic/blob/master/Laboratorium7/ss/przyklad3c.PNG) 

setex (ustawia wartość klucza i jego czas życia)
![App](https://github.com/EllwartDawid/aplikacje-internetowe-21788-185ic/blob/master/Laboratorium7/ss/przyklad3d.PNG) 

Niżej przedstawiony kod działa tak samo jak ten wyżej, z tym że teraz użyliśmy poleceń set i expire:
![App](https://github.com/EllwartDawid/aplikacje-internetowe-21788-185ic/blob/master/Laboratorium7/ss/przyklad3e.PNG) 


## Zbiory

Uruchamiamy program kilka razy, za każdym razem elementy zbioru są wyświetlane w innej kolejności
![App](https://github.com/EllwartDawid/aplikacje-internetowe-21788-185ic/blob/master/Laboratorium7/ss/przyklad4.PNG) 

zrange (sortuje klucze według wartości), `withscores=True` (klucze wyświetlają się z wartościami)
![App](https://github.com/EllwartDawid/aplikacje-internetowe-21788-185ic/blob/master/Laboratorium7/ss/przyklad4a.PNG) 

hash (mapy, słowniki)
![App](https://github.com/EllwartDawid/aplikacje-internetowe-21788-185ic/blob/master/Laboratorium7/ss/przyklad4b.PNG) 
![App](https://github.com/EllwartDawid/aplikacje-internetowe-21788-185ic/blob/master/Laboratorium7/ss/przyklad4b1.PNG) 


## Pubsub

Tworzenie użytkownika z kluczem "testowy_kanal":
![App](https://github.com/EllwartDawid/aplikacje-internetowe-21788-185ic/blob/master/Laboratorium7/ss/przyklad5.PNG) 

`_*` (Podłączanie się do kanałów)
![App](https://github.com/EllwartDawid/aplikacje-internetowe-21788-185ic/blob/master/Laboratorium7/ss/przyklad5a.PNG) 


## Strumienie

Utworzenie strumienia. Pierwsze liczby do milisekundy od 1 stycznia 1970
![App](https://github.com/EllwartDawid/aplikacje-internetowe-21788-185ic/blob/master/Laboratorium7/ss/przyklad6.PNG) 

Dodanie elemntu do strumienia:
![App](https://github.com/EllwartDawid/aplikacje-internetowe-21788-185ic/blob/master/Laboratorium7/ss/przyklad6a.PNG)
![App](https://github.com/EllwartDawid/aplikacje-internetowe-21788-185ic/blob/master/Laboratorium7/ss/przyklad6a1.PNG) 

Kod który sprawia że elementy nie giną:
![App](https://github.com/EllwartDawid/aplikacje-internetowe-21788-185ic/blob/master/Laboratorium7/ss/przyklad6b.PNG) 


## Pipelining

Sprawdzenie czy klucz się nie zmienił. Błąd oznacza że klucz się zmienił
![App](https://github.com/EllwartDawid/aplikacje-internetowe-21788-185ic/blob/master/Laboratorium7/ss/przyklad7.PNG) 


## Lua

eval (przekazuje script do Redisa). Redis wykonuje kod i zwraca rezultat.  Drugi argument eval to 0, określa ilość argumentów które można przekazać do skryptu.
![App](https://github.com/EllwartDawid/aplikacje-internetowe-21788-185ic/blob/master/Laboratorium7/ss/przyklad8.PNG) 

Pierwsze dwa parametry to klucze następne to wartości. Skrypt przekazuje dane i zwraca je jako tablicę
![App](https://github.com/EllwartDawid/aplikacje-internetowe-21788-185ic/blob/master/Laboratorium7/ss/przyklad8a.PNG) 

Kod, który zwraca tablice 10-elementową
![App](https://github.com/EllwartDawid/aplikacje-internetowe-21788-185ic/blob/master/Laboratorium7/ss/przyklad8b.PNG) 

Kod, który dodaje dwie liczby przy wykorzystaniu json
![App](https://github.com/EllwartDawid/aplikacje-internetowe-21788-185ic/blob/master/Laboratorium7/ss/przyklad8c.PNG)

Dodanie 10 i 5:
![App](https://github.com/EllwartDawid/aplikacje-internetowe-21788-185ic/blob/master/Laboratorium7/ss/przyklad8d.PNG)

sha (uruchamia skrypt w sieci)
![App](https://github.com/EllwartDawid/aplikacje-internetowe-21788-185ic/blob/master/Laboratorium7/ss/przyklad8e.PNG)



Nasłuchiwanie zmiany klucza:
![App](https://github.com/EllwartDawid/aplikacje-internetowe-21788-185ic/blob/master/Laboratorium7/ss/przyklad9.PNG)

Powiadomienia o użyciu komendy set:
![App](https://github.com/EllwartDawid/aplikacje-internetowe-21788-185ic/blob/master/Laboratorium7/ss/przyklad9a.PNG)


# Django-Redis-Celery

### Wygląd strony
Przed wyszukaniem obrazka:
![App](https://github.com/EllwartDawid/aplikacje-internetowe-21788-185ic/blob/master/Laboratorium7/ss/thumbnailer.PNG)

Po wyszukaniu obrazka:
![App](https://github.com/EllwartDawid/aplikacje-internetowe-21788-185ic/blob/master/Laboratorium7/ss/thumbnailer1.PNG)

Wynik: 
Obrazek w wersji podstawowej, nowo utworzony obrazek w formacie 128x128 oraz plik zip
![App](https://github.com/EllwartDawid/aplikacje-internetowe-21788-185ic/blob/master/Laboratorium7/ss/thumbnailer2.PNG)


Aby osiągnąć powyższy rezultat należy: 
zmodyfikować plik settings.py:

```javascript
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'thumbnailer.apps.ThumbnailerConfig',
    'widget_tweaks',
]
```

oraz na samym dole:

```javascript
MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'media'))
IMAGES_DIR = os.path.join(MEDIA_ROOT, 'images')

if not os.path.exists(MEDIA_ROOT) or not os.path.exists(IMAGES_DIR):
    os.makedirs(IMAGES_DIR)

# celery
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
```

Następnie należy utworzyć plik tasks.py (kod poniżej), który zawiera import narzędzia zip. W pliku tworzymy zadania w ``@shared_task``.
W ``try`` umieszczamy próbę otwarcia obrazu i przy wykorzystaniu zaimportowanych elementów zapisywanie nowych elementów i kopiowanie starych 

```javascript
import os
from zipfile import ZipFile
from celery import shared_task
from PIL import Image
from django.conf import settings

@shared_task
def make_thumbnails(file_path, thumbnails=[]):
    os.chdir(settings.IMAGES_DIR)
    path, file = os.path.split(file_path)
    file_name, ext = os.path.splitext(file)

    zip_file = f"{file_name}.zip"
    results = {'archive_path': f"{settings.MEDIA_URL}images/{zip_file}"}
    try:
        img = Image.open(file_path)
        zipper = ZipFile(zip_file, 'w')
        zipper.write(file)
        for w, h in thumbnails:
            img_copy = img.copy()
            img_copy.thumbnail((w, h))
            thumbnail_file = f'{file_name}_{w}x{h}.{ext}'
            img_copy.save(thumbnail_file)
            zipper.write(thumbnail_file)

        img.close()
        zipper.close()
    except IOError as e:
        print(e)

    return results
```

W plik views.py deklarujemy klasy, które odpowiadają za wyświetlanie strony głownej, sprawdzanie statusu make_thumbnails oraz tworzy formularz do przesyłania elementów

```javascript
import os

from celery import current_app

from django import forms
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from .tasks import make_thumbnails

class FileUploadForm(forms.Form):
    image_file = forms.ImageField(required=True)

class HomeView(View):
    def get(self, request):
        form = FileUploadForm()
        return render(request, 'thumbnailer/home.html', { 'form': form })
    
    def post(self, request):
        form = FileUploadForm(request.POST, request.FILES)
        context = {}

        if form.is_valid():
            file_path = os.path.join(settings.IMAGES_DIR, request.FILES['image_file'].name)

            with open(file_path, 'wb+') as fp:
                for chunk in request.FILES['image_file']:
                    fp.write(chunk)

            task = make_thumbnails.delay(file_path, thumbnails=[(128, 128)])

            context['task_id'] = task.id
            context['task_status'] = task.status

            return render(request, 'thumbnailer/home.html', context)

        context['form'] = form

        return render(request, 'thumbnailer/home.html', context)


class TaskView(View):
    def get(self, request, task_id):
        task = current_app.AsyncResult(task_id)
        response_data = {'task_status': task.status, 'task_id': task.id}

        if task.status == 'SUCCESS':
            response_data['results'] = task.get()

        return JsonResponse(response_data)
```

## Tworznie tasków

W pliku task.py dodajemy zadania:

```javascript
@shared_task(name='test')
def send_notifiction():
     print('Hello World')
     # Another trick


@shared_task(name='summary') 
def send_import_summary():
    print('Hello every 10 sec')
```

Następnie w pliku settings.py wprowadzamy ustawianie do tasków

```javascript
from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
'beat co 10 sekund': { 
       'task': 'summary',
       'schedule': 10.0
    },
    
    'Witaj o 15:05': {  
         'task': 'test', 
         'schedule': crontab(hour=15, minute=5), 
    },
}
```


