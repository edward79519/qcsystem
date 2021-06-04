from django import template
from qc.models import AnsSingle, AnsFilled

register = template.Library()


@register.filter(name='ans')
def ans(q_obj, task):
    if q_obj.type == 0:
        return AnsSingle.objects.get(task=task, question=q_obj).choice.desc
    elif q_obj.type == 2:
        return AnsFilled.objects.get(task=task, question=q_obj).ans
