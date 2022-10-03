import requests
import pandas as pd
import config
import pd_hh


number_of_pages = 1


def parsing():

    job_title = ["'Data Analyst' and 'data scientist'"]
    for job in job_title:
        data = []
        for i in range(number_of_pages):
            url = config.url_hh
            par = {'text': job, 'area': '113', 'per_page': '10', 'page':i}
            r = requests.get(url, params=par)
            e = r.json()
            data.append(e)
            vacancy_details = data[0]['items'][0].keys()
            df = pd.DataFrame(columns=list(vacancy_details))
            ind = 0
            for i in range(len(data)):
                for j in range(len(data[i]['items'])):
                    df.loc[ind] = data[i]['items'][j]
                    ind += 1
        csv_name = "data_jobs.scv"
        df.to_csv(csv_name)
        pd_hh.conversion()