from click import BaseCommand

from users.models import User


def create_user(email, first_name, last_name, is_staff, is_superuser, password, tg_username):
    """
    Функция для создания или поиска пользователя по указанным параметрам

    """
    user, created = User.objects.get_or_create(
        email=email,
        defaults={
            'first_name': first_name,
            'last_name': last_name,
            'is_staff': is_staff,
            'is_superuser': is_superuser,
            "telegram_user_name": tg_username,
        }
    )
    user.set_password(password)
    user.save()
    return user


class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        Создание пользователей
        """
        simple_user_A = create_user(
            email="test_a@email.aid",
            first_name="Test_A_first_name",
            last_name="Test_A_last_name",
            is_staff=False,
            is_superuser=False,
            password="12345",
            tg_username="Test_A_tg_name"
        )
        simple_user_B = create_user(
            email="test_b@email.aid",
            first_name="Test_B_first_name",
            last_name="Test_B_last_name",
            is_staff=False,
            is_superuser=False,
            password="67890",
            tg_username="Test_B_tg_name"
        )

        users_list = [simple_user_A, simple_user_B]

        User.objects.bulk_create(*users_list)
