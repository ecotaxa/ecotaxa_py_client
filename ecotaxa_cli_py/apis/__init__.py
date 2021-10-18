
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.files_api import FilesApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from ecotaxa_cli_py.api.files_api import FilesApi
from ecotaxa_cli_py.api.taxonomy_tree_api import TaxonomyTreeApi
from ecotaxa_cli_py.api.wip_api import WIPApi
from ecotaxa_cli_py.api.acquisitions_api import AcquisitionsApi
from ecotaxa_cli_py.api.authentification_api import AuthentificationApi
from ecotaxa_cli_py.api.collections_api import CollectionsApi
from ecotaxa_cli_py.api.instrument_api import InstrumentApi
from ecotaxa_cli_py.api.jobs_api import JobsApi
from ecotaxa_cli_py.api.misc_api import MiscApi
from ecotaxa_cli_py.api.object_api import ObjectApi
from ecotaxa_cli_py.api.objects_api import ObjectsApi
from ecotaxa_cli_py.api.processes_api import ProcessesApi
from ecotaxa_cli_py.api.projects_api import ProjectsApi
from ecotaxa_cli_py.api.samples_api import SamplesApi
from ecotaxa_cli_py.api.users_api import UsersApi
