from django.apps import AppConfig

from django.contrib import sites
from django.conf import settings
from django.apps import apps
from django.db.utils import ProgrammingError


class ProjectConfig(AppConfig):
    name = 'project'

    def ready(self):
        # ready is called twice on startup
        if hasattr(self, "ready_run_once"): return
        self.ready_run_once = True

        try:
            Site = apps.get_model('sites', 'Site')
        except LookupError:
            return

        conf_sites = getattr(settings, "SITES", [("example.com", "Example"), ])

        try:
            Site.objects.all().delete()
        except ProgrammingError:
            print("Sites configuration has an unapplied migration. Sites SETTINGS will not be used until the migration is executed.")
            return

        print("Setting sites in DB to:", conf_sites)

        for id, conf_site in enumerate(conf_sites, 1):
            Site.objects.create(id=id, domain=conf_site[0], name=conf_site[1])
