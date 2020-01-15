# -*- coding: utf-8 -*-


from __future__ import absolute_import
from celery import Celery


app = Celery('FastCelery', include=['FastCelery.tasks'])
app.config_from_object('FastCelery.config')

if __name__ == "__main__":
    app.start()
