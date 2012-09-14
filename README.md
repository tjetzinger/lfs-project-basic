# lfs-project-basic

Is an installation template for the [LFS - Lightning Fast Shop](http://www.getlfs.com) online shop.

Now that Django 1.4 supports the notion of project templates, there is no longer a need for LFS's version of the [django-lfs-installer](http://pypi.python.org/pypi/django-lfs/0.7.6#downloads).

To give you an example of how one would use [django-lfs](https://github.com/diefenbach/django-lfs) to start a new online shop follow these steps in your shell:

    $ mkvirtualenv mysite
    $ pip install Django==1.4.1
    $ django-admin.py startproject --template=https://github.com/tjetzinger/lfs-project-basic/zipball/master mysite
    $ cd mysite
    $ pip install -r requirements.txt
    $ python manage.py syncdb
    $ python manage.py runserver