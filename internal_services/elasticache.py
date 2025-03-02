import logging

logger = logging.getLogger(__name__)

class Elasticache:
    def __init__(self):
        pass

    def is_cluster_exists(self):
        logger.info("Checking if cluster is exists")
        print("is redis cluster exits")

    def promote_secondary_to_primary(self):
        logger.info("promote secondary redis cluster to primary")
        print("promote secondary redis cluster to primary")


# if __name__ == "__main__":
#     my_custer = Redshift()
#     my_custer.restore_cluster_from_snapshot()