import json

from django.http import JsonResponse
from django.core import serializers
from django.db.models import Q

from questions.models import Question, Answer


def questions(request, q_id=None, a_id=None):
  """
  """
  if request.method == 'POST':
    try:
      answer = Answer.objects.get(pk=a_id)
      print(answer)
    except:
      return JsonResponse({
        'status': 'Error',
        'msg': 'No answer found'
      })
    else:
      if answer:
        answer.count += 1
        answer.save()

      print(answer)
      return JsonResponse({
        'status': 'Success',
        'msg': 'Found answer, incremented count'
      })

  # Query for some question
  question = Question.objects.order_by('?')[0]
  answers_qs = question.answer_set.all()

  question_json = serializers.serialize('json', [question])
  answers_json = serializers.serialize('json', answers_qs)

  resp = {
    'question': question_json,
    'answers': answers_json
  }

  return JsonResponse(resp)
