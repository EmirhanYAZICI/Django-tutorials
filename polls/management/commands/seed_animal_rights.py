from django.core.management.base import BaseCommand
from polls.models import Question, Choice
from django.utils import timezone
import datetime

class Command(BaseCommand):
    help = 'Seeds the database with animal rights poll questions'

    def handle(self, *args, **options):
        # Clear existing data
        self.stdout.write('Clearing existing data...')
        Question.objects.all().delete()

        questions_data = [
            {
                'text': 'Sizce hayvan deneyleri tamamen yasaklanmalı mı?',
                'choices': ['Evet, her koşulda.', 'Hayır, tıp için gerekli.', 'Sadece kozmetik için yasaklanmalı.', 'Emin değilim.']
            },
            {
                'text': 'Sokak hayvanları için en iyi çözüm nedir?',
                'choices': ['Kısırlaştır, aşılat, yaşat.', 'Barınak kapasiteleri artırılmalı.', 'Sahiplendirme teşvik edilmeli.', 'Hepsi bir arada uygulanmalı.']
            },
            {
                'text': 'Kürk kullanımı hakkında ne düşünüyorsunuz?',
                'choices': ['Tamamen etik dışı.', 'Sadece suni kürk tercih edilmeli.', 'Geleneksel kullanım kabul edilebilir.', 'Önemsemiyorum.']
            },
            {
                'text': 'Hayvan hakları eğitimi okullarda zorunlu olmalı mı?',
                'choices': ['Evet, temel bir ders olmalı.', 'Seminerler yeterli.', 'Gerek yok.', 'Aileler vermeli.']
            }
        ]

        for q_data in questions_data:
            q = Question.objects.create(
                question_text=q_data['text'],
                pub_date=timezone.now()
            )
            for choice_text in q_data['choices']:
                Choice.objects.create(question=q, choice_text=choice_text, votes=0)
            self.stdout.write(f'Added question: {q_data["text"]}')

        self.stdout.write(self.style.SUCCESS('Successfully seeded animal rights questions!'))
