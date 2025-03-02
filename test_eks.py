from internal_services import EKS

import logging

logging.basicConfig(level=logging.INFO)

def main():
    my_eks = EKS()
    my_eks.get_pods()
    my_eks.get_nodes()
    my_eks.get_deployments()


if __name__ == "__main__":
    main()
