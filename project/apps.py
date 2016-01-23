from django.apps import AppConfig

from django.contrib import sites
from django.conf import settings

class ProjectConfig(AppConfig):
    name = 'project'

    def ready(self):
        # ready is called twice on startup
        if hasattr(self, "ready_run_once"): return
        self.ready_run_once = True

        conf_sites = getattr(settings, "SITES", [("example.com", "Example"), ])

        print("Setting sites in DB to:", conf_sites)

        sites.models.Site.objects.all().delete()

        for id, conf_site in enumerate(conf_sites, 1):
            sites.models.Site.objects.create(id = id, domain = conf_site[0], name = conf_site[1])