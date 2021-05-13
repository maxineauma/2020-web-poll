import pandas as pd
import numpy as np
import datetime

# Primary Polling Data
polls_csv = pd.read_csv("https://projects.fivethirtyeight.com/polls-page/president_primary_polls.csv")
polls = polls_csv.sort_values(by=["poll_id","pct"],ascending=False)

# General Polling Data
gen_polls_csv = pd.read_csv("https://projects.fivethirtyeight.com/polls-page/president_polls.csv")
gen_polls = gen_polls_csv.sort_values(by=["poll_id","question_id"],ascending=False)

candidates = ['Biden','Bloomberg','Buttigieg','Gabbard','Klobuchar','Sanders','Steyer','Warren','Yang']

polling = {}
gen_polling = {}

today = datetime.datetime.now().date()
pd_corr = {}
pollIds = pd.Series()

# Democratic Primary
for guy in candidates:
    
    approved = ['Emerson College','NBC News/Wall Street Journal','Morning Consult','ABC News/Washington Post','SSRS','Quinnipiac University','IBD/TIPP','Monmouth University','SurveyUSA','YouGov','Ipsos']
    n_polls = len(approved)
    
    condition = (
        (polls['answer'] == guy) 
        # Polling Conditions
        & (polls['stage'] == 'primary')
        & (polls['state'].isnull()) # national
        & (polls['party'] == 'DEM') 
        & (polls['cycle'] == 2020)
        & (polls['fte_grade'].notnull())
        #& (polls['pollster'].isin(approved))
    )
    
    #dates = polls.loc[condition]['start_date']
    
    #realDates = []
    #daysAgo = []
    #for d in dates.values:
    #    realDates.append(datetime.datetime.strptime(str(d),"%m/%d/%y").date())
    #for d in realDates:
    #    daysAgo.append((today - d).days)
    
    # Last n polls:
    avg = 0
    for x in range(0,n_polls):
        condition_p = condition & (polls['pollster'] == approved[x])
        avg += np.mean(polls.loc[condition_p].head(1)['pct'])
        pollIds = pollIds.append(polls.loc[condition_p].head(1)['question_id'])
        
    avg = round(avg/n_polls,2)
    polling.update({guy:avg})
    #pd_corr.update({guy:{avg:str(daysAgo[-1])}})
    
print(pollIds.head(13))
### Sorting ###
pollsSorted = sorted(polling.items(), key=lambda x: x[1], reverse=True)
frontRunners = pollsSorted[:4]
everyoneElse = pollsSorted[4:len(pollsSorted)]
###############

front = []
for key, value in frontRunners:
    front.append(key)

# General Election
for guy in front:
    gen_condition_dem = (
        (gen_polls['answer'] == guy) 
        # Polling Conditions
        & (gen_polls['stage'] == 'general')
        & (gen_polls['state'].isnull()) # national
        & (gen_polls['candidate_party'] == 'DEM') 
        & (gen_polls['cycle'] == 2020)
        & (gen_polls['fte_grade'].notnull())
    )
    gen_pollIds = gen_polls.loc[gen_condition_dem].head(1)['question_id']
    for g in gen_pollIds:
        gen_condition_trump = (
            (gen_polls['answer'] == 'Trump') 
            # Polling Conditions
            & (gen_polls['stage'] == 'general')
            & (gen_polls['state'].isnull()) # national
            & (gen_polls['candidate_party'] == 'REP') 
            & (gen_polls['cycle'] == 2020)
            & (gen_polls['question_id'] == g)
            & (gen_polls['fte_grade'].notnull())
        )
    person = gen_polls.loc[gen_condition_dem].head(1)['pct'].values[0]
    vstrump = gen_polls.loc[gen_condition_trump].head(1)['pct'].values[0]
    print(guy + " vs Trump: based on " + gen_polls.loc[gen_condition_dem].head(1)['display_name'].values[0] + " poll.")
    gen_polling.update({guy:{round(person):round(vstrump)}})
print(gen_polling)

allpolling = []
for i in pollIds.values[:n_polls]:
    condition = (polls['question_id'] == i)
    
    # Top Value
    allpolling.append("<tr>:<span class='badge badge-pill badge-primary'>"+polls.loc[condition]['fte_grade'].values[0]+"</span> " + polls.loc[condition]['display_name'].values[0] + "; :" + polls.loc[condition]['start_date'].values[0] + " to " + polls.loc[condition]['end_date'].values[0] + "; :" + str(polls.loc[condition]['answer'].values[0]) + "; :" + str(polls.loc[condition]['pct'].values[0]) + "; :" + str(polls.loc[condition]['answer'].values[0]) + " +" + str(round(polls.loc[condition]['pct'].values[0] - polls.loc[condition]['pct'].values[1],1)) + "; :<button class='btn btn-primary' type='button' data-toggle='collapse' data-target='#collapse"+str(i)+"' aria-expanded='false' aria-controls='collapse"+str(i)+"'>Expand</button></tr>")

    # All Others
    for x in range(1,len(polls.loc[condition].values)):
        allpolling.append("<tr class='collapse' id='collapse"+str(i)+"'>: ; : ; :" + str(polls.loc[condition]['answer'].values[x]) + "; :" + str(polls.loc[condition]['pct'].values[x]) + "; : ;</tr>")
