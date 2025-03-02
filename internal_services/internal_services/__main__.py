from eks import EKS
from internal_services import Redshift
import logging

logging.basicConfig(level=logging.INFO)


def main():
    my_eks = EKS()
    my_eks.get_deployments()
    my_eks.get_nodes()


def redshift_function():
    my_redshift = Redshift()
    my_redshift.restore_cluster_from_snapshot()

if __name__ == "__main__":
    main()