import logging

from django.core.management import BaseCommand, CommandError
from dotenv import load_dotenv
from keycloak import KeycloakAdmin

from weops_lite.components.keycloak import KEYCLOAK_ADMIN_USERNAME, KEYCLOAK_URL, KEYCLOAK_ADMIN_PASSWORD, \
    KEYCLOAK_REALM, KEYCLOAK_CLIENT_ID


class Command(BaseCommand):
    help = '创建KeyCloak用户'

    def add_arguments(self, parser):
        parser.add_argument("--username", type=str)
        parser.add_argument("--password", type=str)
        parser.add_argument("--email", type=str)
        parser.add_argument("--lastname", type=str)
        parser.add_argument("--role_type", nargs="?", default='normal', type=str)

    def handle(self, *args, **options):
        load_dotenv()
        logger = logging.getLogger(__name__)

        if not options['username']:
            raise CommandError("参数 'username' 是必填的")
        username = options.get('username')

        if not options['password']:
            raise CommandError("参数 'password' 是必填的")
        password = options.get('password')

        if not options['email']:
            raise CommandError("参数 'email' 是必填的")
        email = options.get('email')

        if not options['lastname']:
            raise CommandError("参数 'lastname' 是必填的")
        lastname = options.get('lastname')

        role_type = options.get('role_type')

        keycloak_admin = KeycloakAdmin(server_url=KEYCLOAK_URL, username=KEYCLOAK_ADMIN_USERNAME,
                                       password=KEYCLOAK_ADMIN_PASSWORD, realm_name=KEYCLOAK_REALM,
                                       client_id="admin-cli", user_realm_name="master")
        clients = keycloak_admin.get_clients()
        client_id = None
        for client in clients:
            if client['clientId'] == KEYCLOAK_CLIENT_ID:
                client_id = client['id']
        if client_id is None:
            raise CommandError(f"没有找到[{KEYCLOAK_CLIENT_ID}]对应的client_id")
        logger.info(client_id)
        role = keycloak_admin.get_client_role(client_id, role_type)
        user = {
            'username': username,
            'credentials': [{"value": password, "type": 'password', 'temporary': False}],
            'email': email,
            'lastName': lastname,
            'enabled': True
        }
        user_id = keycloak_admin.create_user(user, exist_ok=True)
        keycloak_admin.assign_client_role(user_id, client_id, role)
        logger.info(f"用户[{username}]创建成功")
