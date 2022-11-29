from diagrams import Diagram
from diagrams.c4 import (
    Person,
    Container,
    Database,
    System,
    SystemBoundary,
    Relationship,
)

FILENAME = "system_overview"

graph_attr = {
    "splines": "spline",
}

with Diagram(
    "System Architecture (C4 Format)",
    direction="TB",
    graph_attr=graph_attr,
    filename=FILENAME,
    show=False,
):
    user = Person(
        name="External & Internal User",
        description="Sales, Finance, HR, Purchasing, Inventory, Customer",
    )

    airflow = System(
        name="Airflow",
        description="Workflow & Schedule Orchestration",
    )

    with SystemBoundary("CUSTOM"):
        fronted_ex = Container(
            name="Web & Mobile",
            technology="React, React Native, Tailwind",
            description="CMS, B2C, SFA, DELIVERY, CHATBOT",
        )

        backend_ex = Container(
            name="REST API",
            technology="FastAPI, Directus, Supabase",
            description="Business Logic & Workflow",
        )

        database_ex = Database(
            name="Database",
            technology="PostgreSQL & Redis",
            description="Persistent Database",
        )

    with SystemBoundary("ERP"):
        fronted_in = Container(
            name="Odoo Web",
            technology="Odoo",
            description="ERP, HRIS, B2B",
        )

        backend_in = Container(
            name="Odoo Backend",
            technology="Odoo ORM & RPC",
            description="Business Logic & Workflow",
        )

        database_in = Database(
            name="Database",
            technology="PostgreSQL, Redis",
            description="Persistent & Caching",
        )

    with SystemBoundary("IOT ", direction="LR"):
        aws_cloud = Container(
            name="Cloud Storage",
            technology="AWS IoT, AWS S3",
            description="Storage Pool",
        )

        iot_device = Container(
            name="IoT Device",
            technology="Arduino",
            description="Sensor, Log",
        )

    with SystemBoundary(
        "ANALYTICS & ML",
    ):
        data_pipeline = Container(
            name="Data Pipeline",
            technology="dbt, Spark",
            description="ETL",
        )

        data_warehouse = Container(
            name="Data Warehouse",
            technology="PostgreSQL, Redshift",
            description="Data Model, Metric",
        )

        reporting = Container(
            name="Business Intelligence",
            technology="Metabase & Jaspersoft",
            description="Report & Dashboard",
        )

        ml_api = Container(
            name="Machine Learning",
            technology="Tensorflow, Scikit-Learn, FastAPI",
            description="Machine Learning API",
        )

    (
        fronted_in
        >> Relationship("request")
        >> backend_in
        >> Relationship("save")
        >> database_in
    )

    (
        fronted_in
        << Relationship("response")
        << backend_in
        << Relationship("retrieve")
        << database_in
    )

    (
        fronted_ex
        >> Relationship("request")
        >> backend_ex
        >> Relationship("save")
        >> database_ex
    )

    (
        fronted_ex
        << Relationship("response")
        << backend_ex
        << Relationship("retrieve")
        << database_ex
    )

    user >> fronted_in
    user >> fronted_ex

    (
        backend_ex
        >> Relationship("Sync: gRPC,JSON-RPC, Async: RabbitMQ, Kafka")
        >> backend_in
    )
    (
        backend_ex
        << Relationship("Sync: gRPC,JSON-RPC, Async: RabbitMQ, Kafka")
        << backend_in
    )

    airflow >> database_ex
    airflow >> database_in
    airflow >> aws_cloud

    airflow >> data_pipeline >> data_warehouse >> reporting
    data_warehouse >> ml_api

    iot_device >> aws_cloud >> data_pipeline
