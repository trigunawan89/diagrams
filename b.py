from diagrams import Diagram, Cluster
from diagrams.programming.flowchart import Database, Action

with Diagram("odoo", show=False, direction="TB"):
    database1 = Database("Postgresql")
    proses1 = Action("API")

    database1 >> proses1
