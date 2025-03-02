from internal_services import Elasticache
import logging

logging.basicConfig(level=logging.INFO)

def main():
    myredis = Elasticache()

    myredis.is_cluster_exists()
    myredis.promote_secondary_to_primary()


if __name__ == '__main__':
    main()