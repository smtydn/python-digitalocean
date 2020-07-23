from .baseapi import BaseAPI


class Database(BaseAPI):
    """Database management

    Attributes returned by API:
    * id (str): A unique ID that can be used to identify and reference a database cluster.
    * name (str): A unique, human-readable name referring to a database cluster.
    * engine (str): A slug representing the database engine used for the cluster.
                    The possible values are: "pg" for PostgreSQL, "mysql" for MySQL, and "redis" for Redis.
    * version (str): A string representing the version of the database engine in use for the cluster.
    * connection (obj): An object containing the information required to connect to the database.
    * private_connection (obj): An object containing the information required to connect to the database via the private.
    * users (list(obj)): An array containing objects describing the database's users.
    * db_names (list(str)): An array of strings containing the names of databases created in the database cluster.
    * num_nodes (int): The number of nodes in the database cluster.
    * size (str): The slug identifier representing the size of the nodes in the database cluster.
    * region (str): The slug identifier for the region where the database cluster is located.
    * status (str): A string representing the current status of the database cluster.
                    Possible values include creating, online, resizing, and migrating.
    * maintenance_window (obj): An object containing information about any pending maintenance for the database cluster and when it will occur.
    * created_at (str): A time value given in ISO8601 combined date and time format that represents when the database cluster was created.
    * tags (list(str)): An array of tags that have been applied to the database cluster.
    * private_network_uuid (str): A string specifying the UUID of the VPC to which the database cluster is assigned.
    """

    def __init__(self, *args, **kwargs):
        self.id = None
        self.name = None
        self.engine = None
        self.version = None
        self.connection = []
        self.private_connection = []
        self.users = []
        self.db_names = []
        self.num_nodes = None
        self.size = None
        self.region = None
        self.status = None
        self.maintenance_window = {}
        self.created_at = None
        self.tags = []
        self.private_network_uuid = None

        super(Database, self).__init__(*args, **kwargs)
