import json

from django.test import TestCase

from questions.models import Question, Answer


class ApiTest(TestCase):
  """Test class for questions API

  Routes:
  GET /question/ - Returns JSON containing a question and associated answers
  PUT /question/:q_id/:a_id - Adds a one to the answer count on a_id
  """

  def setUp(self):
    """Create a test question and associated answer in the database
    """
    self.question_params = {
      'text': "How much wood would a woodchuck chuck?",
    }
    new_question = Question.objects.create(**self.question_params)
    new_question.save()

    self.answer_1_params = {
      'text': '42',
      'question': new_question,
    }
    new_answer = Answer.objects.create(**self.answer_1_params)
    new_answer.save()

    self.answer_2_params = {
      'text': 'too much!',
      'question': new_question,
    }
    new_answer = Answer.objects.create(**self.answer_2_params)
    new_answer.save()

  def tearDown(self):
    """Clear test database
    """
    Question.objects.all().delete()
    Answer.objects.all().delete()

  def _get_question(self, **kwargs):
    response = self.client.get(
      path='/question/',
      data=kwargs,
      HTTP_X_REQUESTED_WITH='XMLHttpRequest'
    )
    return json.loads(response.content.decode())

  def _put_answer(self, q_id=None, a_id=None, **kwargs):
    path = '/question/'
    if q_id:
      path += '%s/' % (q_id,)
    if a_id:
      path += '%s/' % (a_id,)

    response = self.client.put(
      path=path,
      data=kwargs,
      HTTP_X_REQUESTED_WITH='XMLHttpRequest'
    )
    return json.loads(response.content.decode())
    # return response

  ### Test Methods ###
  def test_get_question_returns_200(self):
    response = self.client.get(
      '/question/',
      HTTP_X_REQUESTED_WITH='XMLHttpRequest'
    )
    self.assertEqual(response.status_code, 200)

  def test_get_question_returns_question(self):
    data = self._get_question()
    self.assertIn('question', data.keys())

  def test_question_route_returns_answers(self):
    data = self._get_question()
    self.assertIn('answers', data.keys())

  def test_post_answer_returns_error_status_if_no_question_or_answer_provided(self):
    response = self._put_answer()
    self.assertEqual(response['status'], 'Error')
    self.assertEqual(response['msg'], 'No answer found')

  def test_post_answer_returns_success_status_if_question_found(self):
    response = self._put_answer(q_id=1, a_id=1)
    self.assertEqual(response['status'], 'Success')
    self.assertEqual(response['msg'], 'Found answer, incremented count')
