> to my 'mates'

# Things to remember :

1.  After project is created, **create an app** with the following command :
  'python manage.py startapp [appname]'

1.  Create a **urls.py** file inside the recently created app folder (see urls.py for example).
1.  Register the application urls.py onto the urls.py of the directory with the same name of the project.
    In this case, sbtemplates/sbtemplates/urls.py. (see the urls.py inside the mentioned directory for example of
      registration).
1.  Define application inside settings.py (see settings.py for instruction).

# Adding the templates

1. Create these following directories inside the application ("store" in this case) :
   'store/templates/store' and 'store/static/store'
1. Inside **static/store** copy the template files, inside **templates/store** create two html files like
   layout.html and index.html and insert the html codes from the index.html that came with the startbootstrap template files. (see layout.html and index.html to see structure).
1. Inside layout.html, add following line of code at very first line :
   '{% load static %}'
1. At every link reference, replace the directory in the href with the following format :
   '{% static '[appname]/.../sample.css' %}'

   in this case as example :

   '{% static 'store/vendor/bootstrap/css/bootstrap.min.css' %}'

   (see layout.html for further example).
1. Go to urls.py add an index url/route :
   'urlpatterns = [
       path('', views.index, name='index'),
   ]'

   then, render html from views.index inside **views.py**

   'def index(request):
       return render(request, 'store/index.html')'

    (see urls.py and views.py for further example).
1. Run project server via command :
   'python manage.py runserver'

# Resources Used

https://startbootstrap.com/template-overviews/small-business/
