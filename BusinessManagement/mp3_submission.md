<table><tr><td> <em>Assignment: </em> IS601 Mini Project 3  Business Management</td></tr>
<tr><td> <em>Student: </em> Sai Karthik Kasumurthy (sk3374)</td></tr>
<tr><td> <em>Generated: </em> 4/11/2023 12:38:14 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-3-business-management/grade/sk3374" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <div>Initial Preperation:</div><div><ol><li>Create two new dynos/VMs in Heroku:</li><ol><li>is601-ucid-mp3-dev</li><li>is601-ucid-mp3-prod</li></ol><li>Configure the heroku config vars and github secrets similar to how dev/prod were setup</li><li>Create two new secrets for github and set the values per the machine names in step 1</li><ol><li>HEROKU_APP_MP3_DEV</li><li>HEROKU_APP_MP3_PROD</li></ol><li>Duplicate your dev/prod yml files and have it listen to the mp3-dev and mp3-prod branches respectively</li><ol><li>Make sure you refer to the proper app secrets from step 3</li><li>You can merge these into regular dev/prod later but you'll want your final project to deploy over it (overwrite) on the normal dev/prod dynos/VM</li></ol><li>You can add this HW branch to the dev yml to test your deployments prior to the pull request to dev from step 4</li></ol></div><div><br></div><div><br></div><ol><li>checkout dev and pull any latest changes</li><li>Create a branch called mp3-prod and immediately push it</li><li>Create a branch called mp3-dev and immediately push it</li><li>Create a branch called MiniProject-3</li><li>Add all the baseline files first under a folder called BusinessManagement (included below)</li><li>Don't forget to copy your .env file from flask_sample into BusinessManagement</li><li>source the venv and pip install the requirements.txt</li><li>Run the BusinessManagement/sql/init_db.py script</li><li><b>Immediate add/commit/push to github</b></li><li>Open a pull request to mp3-dev and keep it open until you're done adding the submission file</li><li>Make your code changes per the following requirements</li><ol><li>Important: run the test files indiviudally as you're working/testing to save on query quota usage</li><li>&nbsp;pytest BusinessManagement/test/name_of_test.py -rA</li></ol><li>Add/commit periodically (recommended after you implement a TODO item or checlist item and add a related commit message for clarity)<br></li><ol><li>Do not delete any provided comments</li></ol><li>Anywhere relevant add your ucid and the date you added the code (best to do this as you go)</li><li>You'll be capturing website screenshots from dev and code snippet screenshots (ensure you upload these properly as pull request comments to the pull request from step 10</li><ol><li>Note: You don't need separate screenshots for each checklist item, when possible it's recommended to try to capture multiple items together and reuse the image</li><li>Ensure all screenshots are properly captioned in the deliverable section so it's clear what part you're trying to show</li></ol><li>Once done, copy the markdown or download the md file and save it under the BusinessManagement folder</li><li>Do a final add/commit/push</li><li>Verify everything looks ok in the pull request</li><li>Merge the pull request</li><li>Make a new pull request from mp3-dev to mp3-prod and merge it</li><ol><li>If you want to keep original dev/prod up to date you can merge the changes into those, but they will cause a deploy to occur for each so be mindful</li></ol><li>Navigate to the submission file under the BusinessManagement folder from mp3-prod</li><li>Copy the github url to the exact file and submit it to Canvas</li></ol><div>You'll be implementing a basic Business Management site.</div><div>There will be some provided files fully working as-is and some skeleton files you'll need to fill in.</div><div>The files you need to fill in will have TODO items or comments mentioning what's expected.</div><div>Some files will have "DO NOT EDIT" mentioned, please don't edit these. If there's a doubt about any of them ask.</div><div>There are provided test case files too that all must be passing for full credit. Do not edit these test case files.</div><div>If a test case isn't possible to complete, capture the failed test case locally via `pytest BusinessManagement -rA` first, then you can rename the function to `off_original_name`.</div><div>The site will handle CRUD operations for Companies and Employees as well as allowing import of Company/Employee data via a csv file.</div><div>Note: db.py has been updated to use pymysql instead of mysql-connector-python to aid in easier queries.</div><div><br></div><div>Baseline files:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F23-MiniProject-3">https://github.com/MattToegel/IS601/tree/F23-MiniProject-3</a>&nbsp;</div><div>May want to download branch as a zip, then copy/paste the files into your repo (if/when you do, please immediately do a git add/commit to record the baseline items)</div><div><br></div><div>Provided files you don't need to edit:</div><div><ul><li>000_create_table_companies.sql</li><li>001_create_table_employees.sql</li><li>db.py</li><li>init_db.py</li><li>flash.html</li><li>company_dropdown.html</li><li>country_state_selector.html</li><li>upload.html</li><li>sort_filter.html</li><li>all test files</li><li>geography.py</li><li>__init__.py (remains empty)</li><li>Dockerfile</li><li>main.py</li><li>index.py</li></ul><div>All other files likely have requirements to fill in.</div></div><div><br></div></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Identity Edits and Setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the index page being displayed (from dev)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231019649-35070010-446a-4f9a-ae52-64f8a37dac5b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of nav.html - updated DIAR-mt85 to DIAR-sk3374,  also added correct Relavent<br>URL references <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231019115-d192e3b2-9cb7-4d0c-9d46-ce1c18f030ab.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Index page from the heroku dev along with the URL<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot from the DB extension of vs code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231020040-a90cc522-3331-40aa-a05c-24e77f8b1966.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of IS601_MP3_Companies table along with first few records of data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231020081-2ad8cb66-7adf-45ca-95c8-228eff528aee.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of IS601_MP3_Employees table along with first few records of data<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Upload / Import CSV File (provided data.csv) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of /import route (code)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231023171-1a96f65a-52a0-475a-9e6e-1aad131066ed.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of /import route, PIECE: 1 (does the csv check )<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231021045-b48b76cc-7db6-48e5-8f68-528f89c5758d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of /import route, PIECE: 2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231021201-54089f00-e608-4d8c-8e79-b4f3e11b7f0f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of /import route, PIECE: 3<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of the website when uploading the data.csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231021758-e05c4985-4344-40c0-9ee3-8e51feacde61.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Added screenshot of the import page after the import done with proper success<br>and count messages<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231023425-f044015e-2d4b-4e05-815c-9a1d256487a4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Added screenshot of import page when no file is selected (no file selected<br>msg)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231024418-6cd7a1a4-de59-4663-b1c4-c9917bca657c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Added screenshot of import page when a file which is not a csv<br>is selected (Invalid msg)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data (basic summary/view)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231024608-6a4b9254-5830-4135-9c41-295540a84c23.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing some company data was uploaded<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231024743-1bb8b431-7db9-4acf-9829-500bebd1a033.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing some company data was uploaded<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Add Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231029111-7bf890eb-abbb-4a77-8c51-5635e4d88024.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of code for /add route of employee. PIECE 1 (Shows retrieval of<br>fields, proper flash message for required fields, and checks for valid email)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231029315-ad39ffe6-b1a2-4922-b9f4-6b37f4252683.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of is_valid_email function which validates the email format using regex<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231029417-2f94b076-b7f3-4c3a-843f-492503890c99.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of code for /add route of employee. PIECE 2 (Shows proper INSERT<br>query and if record successfully created or failed)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231030903-b76dafa6-ff2b-482e-a7ea-aed3a3de3c25.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Add Employee page with filled in data prior to submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231030931-902f8404-ed03-43c1-925c-a72060f00baa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of success message saying created record<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231030975-f579a98b-b4b9-479f-a381-f17091fd8da3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of first name required error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231031029-b8e821e2-47ee-4635-92b6-57ad864b6d90.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of last name required error message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new employee DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231031229-ce73d474-5fa1-400e-bc7c-b98742f296f0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the DB from VS code which shows Bad Pit in the<br>table IS601_MP3_Employees (Used a select query so better visibility)<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> List/search Employees </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231026259-148c1e82-82d1-486b-8c53-8b68d052afb1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of code for /add route of employee: PIECE: 1 (shows the query<br>to pull the fields and code to fetch from from request args)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231026335-a25fc795-17a2-47cc-a0ac-a42cb9a955c3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of code for /add route of employee: PIECE: 2 (shows code for<br>checking if args exist; appending them to the query with appropriate condition; also<br>showed appending Order and Limit and limit out of bounds msg) )<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231029011-c092dd6f-f495-48f3-8134-f078f0a5b2ea.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of code for /add route of employee: PIECE: 3 (shows code for<br>error prompt when searching for employee failed )<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231032520-95dfda54-8541-46f2-ae87-b369d4918b83.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot from Website of Employee search records with first_name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231032742-4da901db-750c-4016-8e1a-91e51166f0f0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot from Website of Employee search records with with last_name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231033126-c4085602-7ec5-47b0-ade1-40a2511bb220.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot from Website of Employee search records with with email filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231033235-f784bdad-5c98-48b0-819e-06e326d9e6da.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot from Website of Employee search records with with company filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231033540-eb68cf25-cbdc-48dd-9d55-ebd600e7135a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot from Website of Employee search showing records when sorted in Ascending order<br>of the First Name of employees<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231033704-0a892482-e9e1-4f76-8025-5f1e59e4d9cf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot from Website of Employee search showing records when sorted in Descending order<br>of the First Name of employees<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231035125-87980047-f6a2-41cc-828a-7f059cc5d934.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshots of code for /edit route of employee, PIECE: 1 (Shows retrieval of<br>fields, field required checks, email validation and prompt messages)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231035805-2e13e47b-9219-465d-bfb3-6a1b53a53ed7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshots of code for /edit route of employee, PIECE: 2 (Shows update query,<br>sucess msg, error occured popup, fetch updated data query and fetch error message))<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231036739-99be625f-69ef-444a-8f66-2c9decee1c78.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Data before edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231036788-6be32716-3c84-4832-8756-e8acb9e65f93.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of sucess message after edit of first name from &#39;Bad&#39; to &#39;Broad&#39;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231036854-190b0e66-5319-42ac-a309-5e6a6fade42a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Data after edit<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of employee data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231036716-e7f18545-5a07-4e32-9baf-4beab605ebb2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Screenshots of DB data before edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231036891-b29c6f18-17a8-4472-b66d-1276fe99b15d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Screenshots of DB data after edit<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231054082-42a41f65-dc94-46d4-b1a8-1afbc3ba1e45.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of code for /add route of company: PIECE: 1 (Shows retrival of<br>fields using form.get)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231057433-1ce797bc-bc66-4d4e-8c3a-6384a1f398ab.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of code for /add route of company: PIECE: 2 (Showed  the<br>checks done for required fields and displayed prompts, also handled invalid state/country)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231054294-d85d217b-0293-4884-9aab-e56e35fb7808.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of code for /add route of company: PIECE: 3 (the add query,<br>success and failure messages)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231039338-d55b43e1-9fe0-4a90-8257-66a24d20db6f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of filled in valid data prior to submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231039370-f10c381f-98ba-4756-bb5f-fcf61949ed11.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of success message after updating<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231041308-83dcce65-4e35-4581-a8ff-b8a1df27c67e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231041438-481ba452-9d10-4349-b24d-b6d0633547cd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing address required error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231041508-484919c7-5745-429a-a560-68893668a571.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing  city required error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231041687-bb837e8e-3d68-45bc-b34a-7dee2be7610f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing country required error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231041757-c17504ce-33cc-40e8-bf63-52ac74bb6d66.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing state required  error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231041816-b8414cbc-8724-4944-b0be-a8d1889c5471.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing zip code required error message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new company DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231041999-b2bfbbcc-1dd6-4d56-a389-9bd21910a809.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the newly added DB record from VScode<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> List/Search Comapny </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231042913-a2c6fc35-7808-4c94-9c37-e0eacd965929.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshots of code for /search route of company: PIECE: 1 (Shows SELECT query,<br>fetched fields using args.get)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231054633-e74b1818-aefe-43b3-ae68-a4991154dbff.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshots of code for /search route of company: PIECE: 2 (Shows appending fields<br>to the query and handling limit)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231045001-72de61d9-5d2f-4525-9f26-8c7f67cb4da4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshots of code for /search route of company: PIECE: 3 (Shows the error<br>prompt if search failed)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231045549-5e5cd042-bcb1-45e1-a452-7dd4d15ca4f6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Employee search with name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231045700-642eb91b-6eab-429b-b50c-15fa0075b1cb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Employee search with country filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231045804-f4f1b854-5283-4905-9eb6-95f6a4743c4d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Employee search with state filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231046209-10a01a7c-a34c-4791-a9c8-29cfe3c71da9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Employee search showing records in Ascending order of Name<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231046304-7d642528-a39f-4019-a23c-0c3de8be21b0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Employee search showing records in Descending order of Name<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Edit Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231047616-87476907-fe04-4a47-a5d5-12241447f183.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshots of code for /edit route of company: PIECE 1 (Shows the retrieval<br>of fields)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231056411-548fef45-4dbd-4493-ba3e-7660ae4d89b5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshots of code for /edit route of company: PIECE 2 (Shows the checks<br>done for required fields and the prompts)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231048032-3020c6b8-3ec4-4f62-acca-b0b5d080d0a2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshots of code for /edit route of company: PIECE 3 (shows the update<br>query, success/ failure prompt, updated record retrieval query and promt)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231048451-7f3a7a7a-a6ea-4891-ace7-783292d53937.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of data before an edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231048528-9e8db68e-ea9a-46c3-9ac4-832eb30e1f3d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of success message after edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231048610-e891070d-ade4-4c1d-890e-0b48975c7d09.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of data after the edit<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of company  data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231048964-03782114-732b-474d-bf33-10e6a364f9e6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of DB data before the edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231049085-cb7e178c-ec1a-40fe-bdc8-753e4d1ce9cb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of DB data after the edit<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Delete Employee and Delete Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /delete route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231049288-d277b682-3b37-48e6-a67c-2d8e6392db82.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of code for /delete route of employee (shows deleting of employee using<br>id through a DELETE query and success/failed prompts of delete)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after website screenshot of deleting an employee (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231049980-eb549c06-c06c-487e-9fbc-289fa5f7992b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Employee &#39;Mighty thor&#39; before deleting<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231050049-1ee880a4-a1f6-40bc-a589-d8ba3496392b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success message of Employee deleted <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231050130-0ba7da09-dab4-4439-b925-7d5a6a6e3b9e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of after deleting (no records shown for &#39;Mighty thor&#39;)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of code for /delete route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231050354-6373adc2-2fc2-4e74-979d-0f95b81e3728.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of code for /delete route of company (shows deleting of company using<br>id through a DELETE query and success/failed prompts of delete)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after website screenshot of deleting a company (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231050553-46bb7b98-1182-4801-9495-55a3a8656e03.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Company &#39;Abc Enterprises Inc&#39; before deleting<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231050632-e6ac4a6d-04d9-411d-b027-21a7d9833469.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success message of Company deleted <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231050679-e97dc64c-930a-4490-acd6-15b0e3e95cfd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of after deleting (no records shown for &#39;Abc Enterprises&#39;)<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Test Cases and Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot Test case Results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231050942-532447e8-378d-4089-afdc-19fd5a887762.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of test_add_company test case Results<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231051056-f3fb1d0c-cec4-41ff-b235-601139385293.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of test_add_employee test case Results<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231051128-706c801f-a70c-4942-921c-dc0397b6267c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of test_edit_company test case Results<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231051207-930af653-c7d3-4534-94c6-24b56f059edd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of test_edit_empoyee test case Results<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231051395-974979ad-6400-4add-b749-d2931d80f50d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of test_search_company test case Results: PIECE: 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231051498-833291c2-ffd9-494a-b8e9-58586661357f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of test_search_company test case Results: PIECE: 2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231051532-c9ecc71e-0778-44fd-9a43-0c33a3f3d23e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of test_search_company test case Results: PIECE: 3<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231051657-14e56613-2bfe-4735-9034-6fd0acd425e0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of test_search_company test case Results: PIECE: 4<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231051748-de5b04b0-c6f0-4568-b3c0-9e04f0e137e9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of test_search_employee test case Results: PIECE: 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231051807-feed0d27-a4aa-4a54-809b-9f084ca47881.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of test_search_employee test case Results: PIECE: 2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231051885-e066a480-63f8-4979-a61a-400925edce31.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of test_search_employee test case Results: PIECE: 3<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231052024-431929fe-6163-4fde-be2b-3853974a0b06.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of test_upload_csv test case Results: PIECE: 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/231052092-94fec493-00a6-4292-aa0a-5d3f7a8dd26b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of test_upload_csv test case Results: PIECE: 2<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Issues / Learnings / Interesting things to note</td></tr>
<tr><td> <em>Response:</em> <p>Learning:<br>1. I learned about creating routes in flask and how they are used<br>to map URLs to the function which handle the request. Also learned about<br>differnt HTTP methods like GET and POST and how we used them to<br>retrieve from the web page or post data.<div><br></div><div>2. Learned how to use the<br>Jinga template which allowed us to create dynamic HTML pages so that we<br>can reuse the created fields (like the country and the state dropdown that<br>we had created)</div><div><br></div><div>Issues:<br>1. Even though my code was correct, the test cases were<br>failing. After debugging I got to know that this was due to incorrect<br>data. After deleting those records the test cases ran fine.</div><div><br></div><div>2. Also I had<br>incorrect database connection string in&nbsp; the .env file and so was not getting<br>the records in the web page after giving the correct connection string I<br>was able to see the records on the webpage.</div><div>&nbsp;</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-3-business-management/grade/sk3374" target="_blank">Grading</a></td></tr></table>