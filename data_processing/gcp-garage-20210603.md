### LAB I : Orchestrate workflow using Cloud Composer

```python
# advanced_analytics_composer_lab.py
"""An example Composer workflow integrating GCS and BigQuery.

A .csv is read from a GCS bucket to a BigQuery table; a query is made, and the
result is written back to a different BigQuery table within a new dataset.
"""

from datetime import datetime, timedelta
from airflow import DAG
from airflow.contrib.operators.bigquery_operator import BigQueryOperator
from airflow.contrib.operators.gcs_to_bq import GoogleCloudStorageToBigQueryOperator
from airflow.operators.bash_operator import BashOperator

YESTERDAY = datetime.combine(
   datetime.today() - timedelta(days=1), datetime.min.time())
BQ_DATASET_NAME = 'composer_lab_dataset'

default_args = {
   'owner': 'airflow',
   'depends_on_past': False,
   'start_date': YESTERDAY,
   'email_on_failure': False,
   'email_on_retry': False,
   'retries': 1,
   'retry_delay': timedelta(minutes=5),
}

with DAG('composer_lab', default_args=default_args) as dag:
 create_bq_dataset_if_not_exist = """
   bq ls {0}
   if [ $? -ne 0 ]; then
     bq mk {0}
   fi
 """.format(BQ_DATASET_NAME)

 # Create destination dataset.
 t1 = BashOperator(
     task_id='create_destination_dataset',
     bash_command=create_bq_dataset_if_not_exist,
     dag=dag)

 # Create a bigquery table from a .csv file located in a GCS bucket
 # (gs://example-datasets/game_data_condensed.csv).
 # Store it in our dataset.
 t2 = GoogleCloudStorageToBigQueryOperator(
     task_id='gcs_to_bq',
     # CHANGE BELOW
     bucket='garage-yzhou',
     # DOUBLE-CHECK CORRECT FILE IN GCS
     source_objects=['products.csv'],
     destination_project_dataset_table='{0}.products_table'
     .format(BQ_DATASET_NAME),
     schema_fields=[
         {
             'name': 'SKU',
             'type': 'string',
             'mode': 'nullable'
         },
         {
             'name': 'name',
             'type': 'string',
             'mode': 'nullable'
         },
         {
             'name': 'orderedQuantity',
             'type': 'integer',
             'mode': 'nullable'
         },
         {
             'name': 'stockLevel',
             'type': 'integer',
             'mode': 'nullable'
         },
         {
             'name': 'restockingLeadTime',
             'type': 'integer',
             'mode': 'nullable'
         }    
     ],
     skip_leading_rows=1,
     write_disposition='WRITE_TRUNCATE')

 # Run example query (http://shortn/_BdF1UTEYOb) and save result to the
 # destination table.
 t3 = BigQueryOperator(
     task_id='bq_example_query',
     bql="""
       SELECT
         name, orderedQuantity
       FROM
         [{0}.products_table];
     """.format(BQ_DATASET_NAME),
     destination_dataset_table='{0}.products_table_subset'
     .format(BQ_DATASET_NAME),
     write_disposition='WRITE_TRUNCATE')

 t1 >> t2 >> t3
```


Q: What are primary differentiators of BigQuery Data Warehouse? [Pick 2]

A: Batch + Streaming and BigQuery ML


### Vertex AI
We can deploy models on edge, i.e. phone, connected vehicles.

Kubeflow is now pipelines on Vertex AI.