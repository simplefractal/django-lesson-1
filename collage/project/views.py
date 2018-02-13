import time

from .serializers import ProjectSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

from account.models import Account
from client.models import Client
from task.models import Task, TaskTag

from .models import Project


class ProjectList(APIView):
    """
    List all projects, e.g.

    {
        "id": 321,
        "name": "szOsmJnOgVbhWEsoEPCltbiNrLHZTobyAnZsjMwwYrFIdYpMiEQFBoATqzdSrMPbmrDpRUhsnQNZwqBjXoVSrCIKhvqTwCfdZMiK",
        "client": {
            "id": 157,
            "name": "NpSsShuBaTGWVNXgehWfBUNnPmmnLTCKYlQfCOAuifIUVqeokczqxCXSxkRFvKREbwFZsoAwjwLABlXPcztkFqvHpJzBiVmkrwkb",
            "email": "enZgyVMJwZ@example.com",
            "industry": "GWyevlpHQUuTddpIygbNHaoNgmUkGqCGGrajtuuwflCcWBsaCU",
            "code": "CODE-NpSsShuBaTGWVNXgehWfBUNnPmmnLTCKYlQfCOAuifIUVqeokczqxCXSxkRFvKREbwFZsoAwjwLABlXPcztkFqvHpJzBiVmkrwkb",
            "industry_code": "INDUS-GWyevlpHQUuTddpIygbNHaoNgmUkGqCGGrajtuuwflCcWBsaCU",
            "needs_attention": true
        },
        "members": [
            {
                "id": 257,
                "name": "eSIBFyBFGSvruFqPNcpDfllHYcNLxBcZVUwjUZNvkvZUoPwlWszQufAZzpcxBKJZTntqqWFywkQvxQHJDHEmibrcSsuiLenyWhkVBiaItowyJcHGWTUzWJANaotkTqWHDPOlzIyWZphexOKJkvlzaYFKIiWNlJFjOpinVdsnIfyKuUdGRacCKzuRDsYGGacyeLZhnLhNLWifUcqcOTtHMApHiBxDmzfCZwoTcQBCdQHuRipOouZsLrmSHT",
                "initials": "E"
            },
            {
                "id": 259,
                "name": "QqAPpYpHkDWQbRCmlVDZnRsrkWSLLgBIxPdvtVHGdZHCdouzwtYuVKvwNAqBVNuejrlqOQOOPoJVzUHakQjNAfqYifAEqgsFtOTaIyzRbSZHXkjevthOFzBtlBSKXeuPFqwpiFqKlFETDKZWWsmSFTvpptwFSsWjDbrMobJjGZlkYGiACmnqFGVglyRFMMGPrmCEuECEhparMEvhfoFcGVldTymIXkHoJgWgCKAbmVKQtzouzDVCioMrFS",
                "initials": "Q"
            },
            {
                "id": 261,
                "name": "nbYuPMxlzyAoLYalNLkLjqHHhvRHAXFcCFqNMmChOqMRTgtKipnjaAkgvcOeKdNgkaxjDbONQCpUsfPriGmmKYGvEmtoQpfeYFBqSCnaWvgwaHsbNgpGJHMlqenohUxnggJuRpIJlMhJaEXxXiZnFffqUfkJPqGTOtuJWeaCLXmxffxcQbgwVvZwMfcHWcnswpZpruszpCXoZojGokWZCNFynHbFyZfgPPzTpGxpulzLLEidiJgMCBRDkC",
                "initials": "N"
            }
        ]
    },
    """

    def get_members(self):
        account_dicts = Account.objects.all().values('id', 'name')
        for acc in account_dicts:
            acc['initials'] = "".join([
                word[0].upper()
                for word in acc['name'].split()
            ])
        return {acc['id']: acc for acc in account_dicts}

    def get_clients(self, urgent_client_ids):
        clients = Client.objects.all().values('id', 'name')
        for cli in clients:
            cli['needs_attention'] = cli['id'] in urgent_client_ids
        return {cli['id']: cli for cli in clients}

    def smart_get_projects(self, clients, members):
        projects = Project.objects.values('id', 'name', 'client_id', 'member')
        project_map = {}

        for proj in projects:
            proj_dict = project_map.get(proj['id'])
            if proj_dict:
                proj_dict['member_ids'].append(proj['member'])
            else:
                project_map[proj['id']] = {
                    'id': proj['id'],
                    'name': proj['name'],
                    'client_id': proj['client_id'],
                    'member_ids': [proj['member']]
                }

        final_projects = project_map.values()
        for proj in final_projects:
            proj['client'] = clients[proj['client_id']]
            member_dicts = [members[member_id] for member_id in proj['member_ids']]
            proj['members'] = member_dicts
        return final_projects

    """

        # projects = []
        # for proj in Project.objects.all().prefetch_related('member'):
        #     member_ids = proj.member.values_list('id', flat=True)
        #     member_dicts = [members[member_id] for member_id in member_ids]
        #     projects.append(
        #         {
        #             'id': proj.id,
        #             'client': clients[proj.client_id],
        #             'members': member_dicts,
        #             'name': proj.name
        #         }
        #     )
    """

    def get(self, request, format=None):
        start = time.time()
        members = self.get_members()
        urgent = TaskTag.objects.get(name='Urgent')
        urgent_client_ids = urgent.task_set.all().values_list('client_id', flat=True)
        clients = self.get_clients(urgent_client_ids)

        projects = self.smart_get_projects(clients, members)
        end = time.time()
        print("Took {}s".format(end - start))
        return Response(projects)
