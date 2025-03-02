from internal_services import Redshift

import logging

logging.basicConfig(level=logging.INFO)

my_redshift = Redshift()

my_redshift.restore_cluster_from_snapshot()