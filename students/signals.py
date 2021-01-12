# from django.db.models.signals import post_save
# from django.contrib.auth.models import User
# from django.dispatch import receiver
# from .models import Student


# @receiver(post_save, sender=Student)
# def send_mail(sender, instance, created, **kwargs):
#     if created:
#         # first_name = instance.first_name
#         print('-'*100)
#         print(instance)
#         print(type(instance))
#         print(dir(instance))
#         print(instance.email)
#         # email = instance.email
#         tuber = instance.tuber_name
#         print(tuber)
#         print('-'*100)

#         subject = f'''
#         Hi,
#         We have received your request, you will receive another confirmation mail soon.

#         Happy learning :)
#         Tutorvita team
#         '''

#         send_mail(
#             f'TutorVita: Confirmation mail for reaching our {tuber}',
#             subject,
#             [email],
#         )
