
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eauth', '0005_alter_signup_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='passphrase',
            field=models.CharField(default='', max_length=500),
        ),
    ]
