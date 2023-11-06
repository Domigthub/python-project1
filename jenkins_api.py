# import jenkins

# jen_server = jenkins.Jenkins('http://192.168.56.177:8080', username='utrains-root', password='school1')
# user = jen_server.get_whoami()
# jobs = jen_server.get_jobs()
# #for i in jobs:
#     # print(i['name'],"url:",i['url'], "job_status:", i['color'])
#     # print("*******************************************")
# Job_stats = []
# for i in jobs:
#         Job_name = i['name']
#         Job_url = i['url']
#         Job_status = i['color']
#         Job_stats.append([Job_name, Job_url, Job_status])

# print(Job_stats)
import csv
def List_job(jenkins_url,jenkins_user,jenkins_pass):
        
    import jenkins

    jen_server = jenkins.Jenkins(jenkins_url, username=jenkins_user, password=jenkins_pass)
    user = jen_server.get_whoami()
    jobs = jen_server.get_jobs()
    #for i in jobs:
        # print(i['name'],"url:",i['url'], "job_status:", i['color'])
        # print("*******************************************")
    
    Job_stats = []
    for i in jobs:
            Job_name = i['name']
            Job_url = i['url']
            job_status = i['color']
            Job_stats.append([Job_name, Job_url, job_status])
    return Job_stats
#c=List_job('http://192.168.56.177:8080','utrains-root','school1')
# print(c)
# with open("example.txt", 'a') as f:
#       content = "adding data into file, jdddjsjf\n"
#       f.write(content)
# with open("example.txt", 'r') as file:
#       cont = file.read()
#       print(cont)

data = List_job('http://192.168.56.177:8080','utrains-root','school1')
with open("jenkins_object.csv",'w')as j:
     write_row = csv.writer(j)
     write_row.writerow(['JOB_NAME','JOB_URL', 'JOB_STATUS'])
     for item in data:
         write_row.writerow(item)


    
