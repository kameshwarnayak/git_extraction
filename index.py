from pydriller import Repository
import datetime
import csv  

repo = 'https://github.com/kubernetes/kubernetes'
since_date = datetime.datetime.now() - datetime.timedelta(days=2*365)

csv_fields = ['Commit Hash', 'Commit Message', 'Author Name', 'Modified File Count', 'Modified Files', 'Commit Date']
csv_rows = [] 
filename = "commit_records.csv"

print("Extraction data from " + repo)

for commit in Repository(repo, since=since_date).traverse_commits():
    print(".", end="")
    modified_files = ''
    modified_files_count = 0
    for file in commit.modified_files:
        modified_files += ',' + file.filename
        modified_files_count += 1
    row = [commit.hash, commit.msg, commit.author.name, modified_files_count, modified_files, commit.committer_date]
    csv_rows.append(row)

print(".")
print("Repository data read")
print("Writing to file")
with open(filename, 'w') as file:  
    filewriter = csv.writer(file)  
    filewriter.writerow(csv_fields)  
    filewriter.writerows(csv_rows) 

print("Extraction complete. Data written to " + filename)
