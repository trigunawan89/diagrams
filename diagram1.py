# diagram.py
from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("Web Service", show=False, direction="TB"):

    with Cluster("Internal APP"):
        a = EC2("A")
        b = EC2("B")
        a >> b

    ELB("lb") >> EC2("web") >> RDS("userdb") >> a
