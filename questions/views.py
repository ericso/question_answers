import json

from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.db.models import Q

from questions.models import Question, Answer


def questions(request):

  # Query for some question
  question = Question.objects.order_by('?')[0]
  answers_qs = question.answer_set.all()

  # question = question.__dict__
  # question.pop('_state')

  # question_json = json.dumps(question)
  # print(question_json)

  question_json = serializers.serialize('json', [question])
  # print(question_json)

  answers_json = serializers.serialize('json', answers_qs)
  # print(json.dumps(answers_json))

  resp = {
    'question': question_json,
    'answers': answers_json
  }

  return JsonResponse(resp, safe=False)


def answer(request, q_id, a_id):
  """
  """
  if request.method == 'POST':
    # Query database for question
    # question = Question.objects.get(pk=q_id)

    print(q_id)
    print(a_id)
    try:
      answer = Answer.objects.get(pk=a_id)
      print(answer)
    except:
      return HttpResponse(404)
    else:
      if answer:
        answer.count += 1
        answer.save()

      print(answer)
      return HttpResponse(200)
