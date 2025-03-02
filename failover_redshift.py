from internal_services import Redshift

def main():
    redshift = Redshift()
    redshift.restore_cluster_from_snapshot()


if __name__ == '__main__':
    main()


