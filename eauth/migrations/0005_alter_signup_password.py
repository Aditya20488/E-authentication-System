

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eauth', '0004_fileupload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='password',
            field=models.CharField(default='', max_length=500),
        ),
    ]
