# encoding: utf-8
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    depends_on = (
        ("main", "0003_migrate_maintainer"),
    )

    def forwards(self, orm):
        "Write your forwards methods here."
        # search by pkgbase first and insert those records
        qs = orm['main.Package'].objects.exclude(maintainer=None).exclude(
                pkgbase=None).distinct().values('pkgbase', 'maintainer_id')
        for row in qs:
            pr, created = orm.PackageRelation.objects.get_or_create(
                    pkgbase=row['pkgbase'], user__id=row['maintainer_id'],
                    defaults={'user_id': row['maintainer_id']})

        # next search by pkgname first and insert those records
        qs = orm['main.Package'].objects.exclude(maintainer=None).filter(
                pkgbase=None).distinct().values('pkgname', 'maintainer_id')
        for row in qs:
            pr, created = orm.PackageRelation.objects.get_or_create(
                    pkgbase=row['pkgname'], user__id=row['maintainer_id'],
                    defaults={'user_id': row['maintainer_id']})

    def backwards(self, orm):
        "Write your backwards methods here."
        if not db.dry_run:
            orm.PackageRelation.objects.all().delete()
        pass

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'main.altforum': {
            'Meta': {'object_name': 'AltForum', 'db_table': "'alt_forums'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'main.arch': {
            'Meta': {'object_name': 'Arch', 'db_table': "'arches'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'main.donor': {
            'Meta': {'object_name': 'Donor', 'db_table': "'donors'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'main.externalproject': {
            'Meta': {'object_name': 'ExternalProject'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'main.mirror': {
            'Meta': {'object_name': 'Mirror'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'admin_email': ('django.db.models.fields.EmailField', [], {'max_length': '255', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isos': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'rsync_password': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'rsync_user': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'tier': ('django.db.models.fields.SmallIntegerField', [], {'default': '2'}),
            'upstream': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Mirror']", 'null': 'True'})
        },
        'main.mirrorprotocol': {
            'Meta': {'object_name': 'MirrorProtocol'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'protocol': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'})
        },
        'main.mirrorrsync': {
            'Meta': {'object_name': 'MirrorRsync'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '24'}),
            'mirror': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rsync_ips'", 'to': "orm['main.Mirror']"})
        },
        'main.mirrorurl': {
            'Meta': {'object_name': 'MirrorUrl'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mirror': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'urls'", 'to': "orm['main.Mirror']"}),
            'protocol': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'urls'", 'to': "orm['main.MirrorProtocol']"}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'main.news': {
            'Meta': {'object_name': 'News', 'db_table': "'news'"},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'news_author'", 'to': "orm['auth.User']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'postdate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'main.package': {
            'Meta': {'object_name': 'Package', 'db_table': "'packages'"},
            'arch': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'packages'", 'to': "orm['main.Arch']"}),
            'build_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'compressed_size': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'files_last_update': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'installed_size': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'license': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'maintainer': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'maintained_packages'", 'null': 'True', 'to': "orm['auth.User']"}),
            'needupdate': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'pkgbase': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'pkgdesc': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pkgname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'pkgrel': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pkgver': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'repo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'packages'", 'to': "orm['main.Repo']"}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'main.packagedepend': {
            'Meta': {'object_name': 'PackageDepend', 'db_table': "'package_depends'"},
            'depname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'depvcmp': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pkg': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Package']"})
        },
        'main.packagefile': {
            'Meta': {'object_name': 'PackageFile', 'db_table': "'package_files'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pkg': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Package']"})
        },
        'main.press': {
            'Meta': {'object_name': 'Press', 'db_table': "'press'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'main.repo': {
            'Meta': {'object_name': 'Repo', 'db_table': "'repos'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'testing': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'})
        },
        'main.signoff': {
            'Meta': {'object_name': 'Signoff'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'packager': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'pkg': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Package']"}),
            'pkgrel': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pkgver': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'main.todolist': {
            'Meta': {'object_name': 'Todolist', 'db_table': "'todolists'"},
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'main.todolistpkg': {
            'Meta': {'unique_together': "(('list', 'pkg'),)", 'object_name': 'TodolistPkg', 'db_table': "'todolist_pkgs'"},
            'complete': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Todolist']"}),
            'pkg': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Package']"})
        },
        'main.userprofile': {
            'Meta': {'object_name': 'UserProfile', 'db_table': "'user_profiles'"},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'allowed_repos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['main.Repo']", 'blank': 'True'}),
            'favorite_distros': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interests': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'languages': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'notify': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'other_contact': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'picture': ('django.db.models.fields.files.FileField', [], {'default': "'devs/silhouette.png'", 'max_length': '100'}),
            'public_email': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'roles': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'userprofile_user'", 'unique': 'True', 'to': "orm['auth.User']"}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'yob': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'packages.packagerelation': {
            'Meta': {'unique_together': "(('pkgbase', 'user', 'type'),)", 'object_name': 'PackageRelation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pkgbase': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'package_relations'", 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['main', 'packages']
