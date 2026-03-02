from google.cloud import bigquery
from google.oauth2 import service_account
from datasets.valid_states import VALID_STATES

class BigQueryService:
    def __init__(self, service_account_info):
        credentials = service_account.Credentials.from_service_account_info(
            service_account_info
        )
        self.client = bigquery.Client(
                credentials=credentials,
                project =service_account_info["project_id"]
                )
        self.df = None

    
    def query_border_states(self,state_name):
         if state_name.lower() not in VALID_STATES:
             raise ValueError(f"Invalid state: {state_name}")
         state_name = state_name.title()
         sql = """
            SELECT neighbors_state
            FROM `bigquery-public-data.geo_us_boundaries.adjacent_states`
            WHERE  state_name = @state_name
        """
         job_config = bigquery.QueryJobConfig(
                 query_parameters=[
                            bigquery.ScalarQueryParameter("state_name" , "STRING", state_name) 
                     ]
                 )
         self.df =  self.client.query(sql,job_config = job_config).to_dataframe()

