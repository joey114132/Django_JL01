import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .models import Question

# 모델 메서드 테스트: Question.was_published_recently()
class QuestionModelTests(TestCase):
    # def test_was_published_recently_with_future_question(self):
    #     """
    #     미래 날짜의 질문은 최근 게시된 것이 아니므로 False를 반환해야 함
    #     """
    #     time = timezone.now() + datetime.timedelta(days=30)
    #     future_question = Question(pub_date=time)
    #     self.assertIs(future_question.was_published_recently(), False)
        


    # def was_published_recently(self):
    #     now = timezone.now()
    #     return now - datetime.timedelta(days=1) <= 
    #     self.pub_date <= now

    def test_was_published_recently_with_old_question(self):
        """
        1일 넘은 과거 질문은 최근 게시된 것이 아니므로 False를 반환해야 함
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)
        
    def test_was_published_recently_with_recent_question(self):
        """
        1일 이내의 질문은 최근 게시된 것이므로 True를 반환해야 함
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)