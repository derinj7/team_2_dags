from datetime import datetime
from airflow.decorators import dag, task

@dag(schedule='@daily', start_date=datetime(2025, 8, 14), catchup=False, tags=["team_2"])
def team_2_dag():
    """
    This is a simple decorator DAG that demonstrates how to use the @dag decorator.
    """

    @task()
    def my_task():
        print("Hello from my_task!")

    my_task()
team_2_dag_instance = team_2_dag()