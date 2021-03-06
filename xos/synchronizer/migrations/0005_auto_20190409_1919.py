# Copyright 2017-present Open Networking Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-09 23:19
from __future__ import unicode_literals

import core.models.xosbase_header
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onos', '0004_auto_20190312_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onosservice_decl',
            name='rest_hostname',
            field=core.models.xosbase_header.StrippedCharField(help_text=b'Hostname of ONOS Service REST endpoint', max_length=256),
        ),
        migrations.AlterField(
            model_name='onosservice_decl',
            name='rest_password',
            field=core.models.xosbase_header.StrippedCharField(default=b'karaf', help_text=b'Password to use when authenticating to ONOS', max_length=256),
        ),
        migrations.AlterField(
            model_name='onosservice_decl',
            name='rest_username',
            field=core.models.xosbase_header.StrippedCharField(default=b'karaf', help_text=b'Username to use when authenticating to ONOS', max_length=256),
        ),
    ]
