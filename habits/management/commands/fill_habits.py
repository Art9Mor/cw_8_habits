import random

from django.core.management import BaseCommand
from django.utils import timezone

from habits.models import Habit


class Command(BaseCommand):
    """
    Заполняет базу данныхпривычками в количестве 5 экземпляров
    """

    def handle(self, *args, **kwargs):
        """
        Создаём новую привычку или получаем уже существующую
        """
        for _ in range(5):
            action = f"Какое-то действие {_}"
            place = "Какое-то место"

            habit, created = Habit.objects.get_or_create(
                action=action,
                place=place,
                defaults={
                    'owner_id': None,  # назначается вручную
                    'time': timezone.now().time(),
                    'is_pleasant': random.choice([True, False]),
                    'link_pleasant': None,  # указывается вручную
                    'frequency': random.choice([choice[0] for choice in Habit.HabitFrequency.choices]),
                    'award': f"Какая-то награда {_}",
                    'duration': 30,
                    'is_public': random.choice([True, False]),
                }
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Новая привычка: {habit}'))
            else:
                self.stdout.write(
                    self.style.WARNING(f'Привычка с действием "{action}" и местом "{place}" уже существует'))