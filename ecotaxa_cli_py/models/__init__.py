# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from ecotaxa_cli_py.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from ecotaxa_cli_py.model.acquisition_model import AcquisitionModel
from ecotaxa_cli_py.model.body_export_object_set import BodyExportObjectSetObjectSetExportPost
from ecotaxa_cli_py.model.bulk_update_req import BulkUpdateReq
from ecotaxa_cli_py.model.classify_auto_req import ClassifyAutoReq
from ecotaxa_cli_py.model.classify_req import ClassifyReq
from ecotaxa_cli_py.model.collection_model import CollectionModel
from ecotaxa_cli_py.model.constants import Constants
from ecotaxa_cli_py.model.create_collection_req import CreateCollectionReq
from ecotaxa_cli_py.model.create_project_req import CreateProjectReq
from ecotaxa_cli_py.model.directory_entry_model import DirectoryEntryModel
from ecotaxa_cli_py.model.directory_model import DirectoryModel
from ecotaxa_cli_py.model.emo_dnet_export_rsp import EMODnetExportRsp
from ecotaxa_cli_py.model.export_req import ExportReq
from ecotaxa_cli_py.model.export_rsp import ExportRsp
from ecotaxa_cli_py.model.export_type_enum import ExportTypeEnum
from ecotaxa_cli_py.model.group_definitions import GroupDefinitions
from ecotaxa_cli_py.model.http_validation_error import HTTPValidationError
from ecotaxa_cli_py.model.historical_classification import HistoricalClassification
from ecotaxa_cli_py.model.historical_last_classif import HistoricalLastClassif
from ecotaxa_cli_py.model.image_model import ImageModel
from ecotaxa_cli_py.model.import_req import ImportReq
from ecotaxa_cli_py.model.import_rsp import ImportRsp
from ecotaxa_cli_py.model.job_model import JobModel
from ecotaxa_cli_py.model.limit_methods import LimitMethods
from ecotaxa_cli_py.model.login_req import LoginReq
from ecotaxa_cli_py.model.merge_rsp import MergeRsp
from ecotaxa_cli_py.model.minimal_user_bo import MinimalUserBO
from ecotaxa_cli_py.model.object_header_model import ObjectHeaderModel
from ecotaxa_cli_py.model.object_model import ObjectModel
from ecotaxa_cli_py.model.object_set_query_rsp import ObjectSetQueryRsp
from ecotaxa_cli_py.model.object_set_revert_to_history_rsp import ObjectSetRevertToHistoryRsp
from ecotaxa_cli_py.model.object_set_summary_rsp import ObjectSetSummaryRsp
from ecotaxa_cli_py.model.process_model import ProcessModel
from ecotaxa_cli_py.model.project_filters import ProjectFilters
from ecotaxa_cli_py.model.project_model import ProjectModel
from ecotaxa_cli_py.model.project_summary_model import ProjectSummaryModel
from ecotaxa_cli_py.model.project_taxo_stats_model import ProjectTaxoStatsModel
from ecotaxa_cli_py.model.project_user_stats_model import ProjectUserStatsModel
from ecotaxa_cli_py.model.sample_model import SampleModel
from ecotaxa_cli_py.model.sample_taxo_stats_model import SampleTaxoStatsModel
from ecotaxa_cli_py.model.simple_import_req import SimpleImportReq
from ecotaxa_cli_py.model.simple_import_rsp import SimpleImportRsp
from ecotaxa_cli_py.model.subset_req import SubsetReq
from ecotaxa_cli_py.model.subset_rsp import SubsetRsp
from ecotaxa_cli_py.model.taxa_search_rsp import TaxaSearchRsp
from ecotaxa_cli_py.model.taxon_model import TaxonModel
from ecotaxa_cli_py.model.taxon_usage_model import TaxonUsageModel
from ecotaxa_cli_py.model.taxonomy_tree_status import TaxonomyTreeStatus
from ecotaxa_cli_py.model.user_activity import UserActivity
from ecotaxa_cli_py.model.user_model import UserModel
from ecotaxa_cli_py.model.user_model_with_rights import UserModelWithRights
from ecotaxa_cli_py.model.validation_error import ValidationError
