from diagrams import Diagram, Cluster
from diagrams.programming.flowchart import Action, StartEnd


with Diagram("Sales Order", show=False, direction="LR"):

    with Cluster("Customer Services", direction="TB"):
        d = Action("Request Validation")
        StartEnd("Start") >> Action("Input Sales Order") >> d

    with Cluster("Warehouse Staff"):
        d1 = Action("Receipt")

    d >> d1
