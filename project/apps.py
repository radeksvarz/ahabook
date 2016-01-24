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

        conf_sites = getattr(settings, "SITES", [(1, "example.com", "Example"), ])

        # We should not delete sites if correctly configured (loosing relationship to the social auths)
        try:
            db_sites = Site.objects.order_by("pk")
            if len(db_sites) == len(conf_sites):
                for db_site, conf_site in zip(db_sites, conf_sites):
                    if(  db_site.pk != conf_site[0] or
                         db_site.domain != conf_site[1] or
                         db_site.name != conf_site[2]):
                        break
                else: # non break
                    # we checked the equality of the whole set of sites
                    print("Sites already in DB:", conf_sites)
                    return

            # Set Sites only if different to current situation in DB
            Site.objects.all().delete()
        except ProgrammingError:
            print("Sites configuration has an unapplied migration. Sites SETTINGS will not be used until the migration is executed.")
            return

        print("Setting sites in DB to:", conf_sites)

        for conf_site in conf_sites:
            Site.objects.create(id=conf_site[0], domain=conf_site[1], name=conf_site[2])
