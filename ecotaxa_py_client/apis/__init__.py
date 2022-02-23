
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
from ecotaxa_py_client.api.files_api import FilesApi
from ecotaxa_py_client.api.taxonomy_tree_api import TaxonomyTreeApi
from ecotaxa_py_client.api.wip_api import WIPApi
from ecotaxa_py_client.api.acquisitions_api import AcquisitionsApi
from ecotaxa_py_client.api.admin_api import AdminApi
from ecotaxa_py_client.api.authentification_api import AuthentificationApi
from ecotaxa_py_client.api.collections_api import CollectionsApi
from ecotaxa_py_client.api.instruments_api import InstrumentsApi
from ecotaxa_py_client.api.jobs_api import JobsApi
from ecotaxa_py_client.api.misc_api import MiscApi
from ecotaxa_py_client.api.object_api import ObjectApi
from ecotaxa_py_client.api.objects_api import ObjectsApi
from ecotaxa_py_client.api.processes_api import ProcessesApi
from ecotaxa_py_client.api.projects_api import ProjectsApi
from ecotaxa_py_client.api.samples_api import SamplesApi
from ecotaxa_py_client.api.users_api import UsersApi
