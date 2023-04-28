

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eauth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='password',
        ),
    ]
