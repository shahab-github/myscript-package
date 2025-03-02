from .elasticache import logger
from .internal_services import EKS

from .redshift import Redshift

import logging

logger = logging.basicConfig(level=logging.INFO)

def main():
    my_eks = EKS()
    my_eks.get_deployments()
    my_eks.get_nodes()


def redshift():
    redshift = Redshift()
    redshift.restore_cluster_from_snapshot()