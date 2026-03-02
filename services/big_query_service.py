from google.cloud import bigquery

class BigQueryService:
    def __init__(self, project_id ,api_key):
        self.client = bigquery.Client(
                project = project_id,
                client_options = {"api_key":api_key}
                )
        self.df = None


