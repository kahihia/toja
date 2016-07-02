from __future__ import unicode_literals

from django.db import models


class Call(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    num_people = models.CharField(max_length=3, blank=False, default='')
    datetime = models.DateTimeField()
    date = models.CharField(max_length=100, blank=True, default='')
    time = models.CharField(max_length=100, blank=True, default='')
    res_num = models.CharField(max_length=100, blank=False, default='')

    READY = 911
    ON_CALLING = 5
    ACCEPTED = 1
    DECLINED = 0
    FAILED = -1

    _STATUS_CHOICES = (
        (ON_CALLING, 'We are in the middle of the call to the restaurant.'),
        (ACCEPTED, 'Reservation has been accepted.'),
        (DECLINED, 'Reservation has been declined.'),
        (FAILED, 'The call is not successful.'),
        (READY, 'We are ready to make the call.')
    )

    STATUS_CHOICES = {}
    for status in _STATUS_CHOICES:
        STATUS_CHOICES[status[0]] = status[1]

    ENGLISH = 0
    JAPANESE = 1

    LANGUAGE_CHOICE = (
        (ENGLISH, 'English'),
        (JAPANESE, 'Japanse')
    )

    status = models.IntegerField(
        choices=_STATUS_CHOICES,
        default=READY
    )

    language_opt = models.IntegerField(
        choices=LANGUAGE_CHOICE,
        default=ENGLISH
    )