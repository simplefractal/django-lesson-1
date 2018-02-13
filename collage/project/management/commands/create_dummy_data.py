import random

from django.core.management.base import BaseCommand, CommandError
from model_mommy import mommy

from client.models import Client


class Command(BaseCommand):
    help = 'Generates dummy data for us to play with'

    def clean_up(self):
        Client.objects.all().delete()

    def create_clients(self):
        return mommy.make(Client, _quantity=15)

    def create_task_tags(self):
        tags = mommy.make('task.TaskTag', _quantity=19)
        urgent = mommy.make('task.TaskTag', name='Urgent')
        return tags + [urgent]

    def create_accounts(self):
        return mommy.make('account.Account', _quantity=10)

    def handle(self, *args, **options):
        self.clean_up()

        tags = self.create_task_tags()
        clients = self.create_clients()

        for client in clients:
            tasks = mommy.make('task.Task', client=client, _quantity=5)
            for task in tasks:
                number_of_tags = random.randint(1, 3)
                tags_for_task = random.sample(tags, number_of_tags)
                task.tags.add(*tags_for_task)

        accounts = self.create_accounts()

        for i in range(300):
            project = mommy.make(
                'project.Project', 
                client=random.choice(clients),
            )
            project.member.add(*random.sample(accounts, 3))
