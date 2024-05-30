from django.db import migrations

from apps.core.utils.keycloak_client import KeyCloakClient
from apps.system_mgmt.constants import ADMIN
from apps.system_mgmt.utils.keycloak import get_realm_roles


def default_set_superior_role(apps, schema_editor):
    GradedRole = apps.get_model("system_mgmt", "GradedRole")
    result = get_realm_roles(KeyCloakClient().realm_client)
    graded_roles = [
        GradedRole(
            role=role_info["name"],
            superior_role=ADMIN,
        )
        for role_info in result
    ]
    GradedRole.objects.bulk_create(graded_roles, batch_size=100)


class Migration(migrations.Migration):

    dependencies = [
        (
            "system_mgmt",
            "0003_gradedrole",
        ),
    ]

    operations = [
        migrations.RunPython(default_set_superior_role)
    ]
