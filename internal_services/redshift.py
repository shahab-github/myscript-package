import logging

logger = logging.getLogger(__name__)

class Redshift:
    def __init__(self):
        pass

    def is_cluster_exists(self):
        logger.info("Checking if cluster is exists")
        print("is cluster exits")

    def enable_cross_region_replication(self):
        logger.info("Enabling cross region replication")
        print("enable cross region replication")


    def create_snapshot(self):
        self.is_cluster_exists()
        self.enable_cross_region_replication()
        logger.info("Creating snapshot")
        print("creating snapshot")


    def restore_cluster_from_snapshot(self):
        self.create_snapshot()
        logger.info("Restoring cluster from snapshot")
        print("restoring cluster from snapshot")


    def delete_snapshot(self):
        logger.info("Deleting snapshot")
        print("deleting snapshot")


# if __name__ == "__main__":
#     my_custer = Redshift()
#     my_custer.restore_cluster_from_snapshot()