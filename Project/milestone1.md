<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Sai Karthik Kasumurthy (sk3374)</td></tr>
<tr><td> <em>Generated: </em> 4/17/2023 11:21:17 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone1-deliverable/grade/sk3374" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/232263167-6a399651-7aac-4df8-9baf-1ebd3537067c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of invalid email validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/232263188-30fb2c96-d112-4cb4-b932-4324b33f9f31.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of invalid password validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/232263440-38674174-f398-4c05-8070-f9e2d57cc8a7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of passwords not much validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/232643179-d6ace20e-e915-41a0-8aa5-c6c348faa7cf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of email not available validation (already registered)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/232627893-8cf1698a-2e85-443b-a059-10c3972ba9e8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of username not available validation (username is already taken)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/232263883-47ab8f1e-9d8c-4905-8d73-42d9c8809138.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the form with valid data filled in before the form is<br>submitted<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/232263895-c1c71c6a-cde2-4ca3-b0e7-340e1da990cc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of form after submission<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/232263935-6f8764ed-3bca-45a0-b290-7cf8afcaabcf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Database of users table with data in it<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/karthikkk999/IS601-006/pull/18">https://github.com/karthikkk999/IS601-006/pull/18</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p><b style=""><font size="3">Explains how the form is handled and behaves:&nbsp;</font></b><div><font size="3">We use the<br>fill in the required data and click on register, the code inserts a<br>new user into the database with their email, username, and hashed password. The<br>code checks for any database constraint errors and displays a message to the<br>user if there is an error.</font></div><div><font size="3"><br></font></div><div><b><font size="3">Explains the validation logic (frontend and<br>backend):</font></b></div><div><font size="3">frontend:<br></font><div style=""><font size="3">The &quot;RegisterForm&quot; class in &quot;forms.py&quot; includes validators that are applied<br>on the frontend using JavaScript. These validators check for required fields, valid email<br>format, password length, and password complexity.&nbsp;If the user submits the form with invalid<br>data, the validators will prevent the form from being submitted and will display<br>error messages to the user.</font></div></div><div style=""><font size="3">backend:<br></font><div style=""><font size="3">When the user submits the<br>form, the Flask view function &quot;register()&quot; is called and it extracts the form<br>data. The form data is then validated using WTForms validators. These validators check<br>for required fields, valid email format, password length, and password complexity. If the<br>data is invalid, the user is redirected back to the registration form with<br>appropriate error messages displayed to them.</font></div><div style=""><font size="3"><br></font></div><div style=""><font size="3"><b>Explains how the password<br>is handled:</b><br></font></div><div style=""><font size="3">The password is hashed using the bcrypt library and the<br>resulting hash is stored in the database. When a user logs in, their<br>password is hashed and compared to the stored hash in the database to<br>verify the password&#39;s correctness.<br><br><b>Explains how the DB is utilized:</b><br>The DB object is instantiated<br>in the auth.py file and the insertOne method is used to execute an<br>INSERT statement to add a new user&#39;s data to the database. In case<br>of an error, the check_duplicate function is used to check whether the error<br>is due to a duplicate value violation, and an appropriate message is displayed<br>to the user.<br></font></div><div style=""><font size="3"><br></font></div><div style="font-size: 13px;"><br></div></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/232263989-e759c030-fdc0-4f24-b67a-c2f04d54db01.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>password doesnt match in DB (already existing)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/232264014-2642bc55-8fc1-4e95-af4d-107bbf886fef.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>invalid user(not there in DB)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/232264031-b8a5e860-885a-4797-8971-9d2054095406.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of successful login and flash message after redirecting to a landing page<br><br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/karthikkk999/IS601-006/pull/18">https://github.com/karthikkk999/IS601-006/pull/18</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p><font size="3"><b style="">Explains how the form is handled and behaves:</b><br>The LoginForm class is<br>used to generate the login form. The validate_on_submit() function is used to check<br>the form data after the user submits the form. The user&#39;s email address<br>or username and password are taken directly from the form if the data<br>is correct. The database is then searched for a user record using the<br>email or username. The user is authorized and logged in if they are<br>an existing user and their password matches one that is stored in the<br>database. The user is routed to the landing page if the login is<br>successful.</font><div><font size="3"><br></font></div><div><b><font size="3">Explains the validation logic (frontend and backend)<br></font></b></div><div><font size="3">frontend:<br></font><div style=""><font size="3">The Flask-WTF<br>extension and the WTForms library are used to validate forms on the front<br>end. All fields must pass their respective validators before the form can be<br>submitted, such as ensuring that the email address is formatted correctly and the<br>password is not empty.</font></div><div style=""><font size="3">backend:</font></div><div style=""><font size="3">The user&#39;s email address or username<br>and password are validated on the backend to make sure they are correct<br>after the form is submitted and passes frontend validation. The backend validation verifies<br>that the username or email address is maintained in the database and that<br>the password matches the hashed password that is also kept there. The user<br>is flashed the necessary error messages if any of the validations fail.</font></div></div><div style="">&lt;font<br>size=&quot;3&quot;&gt;<br></font></div><div style=""><font size="3"><b>Explains how the password is handled:</b><br></font></div><div style=""><font size="3">The password is first<br>hashed with the bcrypt algorithm when a user creates an account before being<br>saved in the database. The same bcrypt technique is used to compare the<br>entered password to the hashed password saved in the database when a user<br>logs in to see if they match. As a result, even if someone<br>gains access to the database, they will not be able to read the<br>passwords themselves.<br></font></div><div style=""><font size="3"><br></font></div><div style=""><font size="3"><b>Explains how the DB is utilized:</b><br></font></div><div style=""><font size="3">The<br>login function queries the database for a user with the provided email or<br>username, retrieves the hashed password, and uses the bcrypt library to verify the<br>entered password matches the stored hash. If the password is correct, the user<br>object is constructed and stored in the session as a JSON object. The<br>user&#39;s roles are also retrieved from the database and assigned to the user<br>object. Finally, the user is logged in via Flask-Login and Flask-Principal.<br></font></div><div style=""><span style="font-size:<br>13px;"><br></span></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/232264068-0451740d-b28b-4d41-897a-50ce5bb1d45a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the successful logout message <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/232265071-b3bd77e3-ac51-4425-a16e-ea3bb6e19000.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of an Unauthorized message when a logged out user tries to access<br>the landing page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/karthikkk999/IS601-006/pull/18">https://github.com/karthikkk999/IS601-006/pull/18</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div><font size="3"><b style="">Describe the session logic and how it's used for login:</b><br>In the<br>code provided, after a successful login, the user object is stored in the<br>session as a JSON string using the toJson() method of the User model.<br>This is done to persist the user's information across requests.&nbsp;To check if the<br>user is logged in or not on subsequent requests, the User object in<br>this instance is saved in the session.&nbsp;The session.pop() method is used to delete<br>the user object from the session during logout. This guarantees that the user<br>has logged out and that their data has been permanently deleted.</font></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/232265071-b3bd77e3-ac51-4425-a16e-ea3bb6e19000.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the logged out user can&#39;t access a login-protected page <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/232264997-306c47f8-be29-4c9c-83ef-b67a196a4f1d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of a non-admin user trying to access the roles which requries admin<br>access. He gets permission denied message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/232265017-087af5ec-7f18-48a1-896e-72f8c567a37d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the Roles table with valid data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/232265028-bc94e749-4de0-4222-b660-448bc9116588.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the UserRoles table with only one record which has admin access<br> <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/karthikkk999/IS601-006/pull/18">https://github.com/karthikkk999/IS601-006/pull/18</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <div><font size="3"><b style="">Explain how the session is used and any relevant helpers:<br></b></font></div><div><span style="font-size:<br>medium;">The session object is used to store the user object as a JSON<br>object after successful login. This is done using the user.toJson() method. The JSON<br>object can be retrieved later from the session object to be used to<br>display user-specific information.</span><font size="3"><b style=""><br></b></font></div><div><font size="3">We use the @login_required decorator from the flask_login<br>module to check if the user is authenticated. If not, the decorator redirects<br>them to the login page. After successful authentication, the user is redirected back<br>to the requested page. Authentication involves verifying the user's credentials against a database,<br>and creating a user object representing the authenticated user. The login() function handles<br>authentication by checking the user's credentials against the database, and creating a User<br>object. The landing_page() function is decorated with @login_required to restrict access.&nbsp;</font></div><div><font size="3"><br></font></div><div><font size="3"><br></font></div><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <div><font size="3"><b>Explain how the session is used and any relevant helpers<br></b>The session object<br>is used to store the user object as a JSON object after successful<br>login. This is done using the user.toJson() method. The JSON object can be<br>retrieved later from the session object to be used to display user-specific information.<br></font></div><font<br>size="3">The @permission_required decorator is defined in the roles package and is applied to<br>the landing_page() function in auth.py. The decorator checks if the user has the<br>admin role before allowing access to the page. If the user does not<br>have the admin role, they are redirected to the login page.</font><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/232555824-975888ac-355a-485d-8bfc-f73b08304dd5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot to show that navigation is styled<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/232555933-0333446d-d2a7-4fc9-b0c3-e4acb84f3060.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot to show that Forms are styled<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/232556124-cb363ed9-c0c7-4987-aada-067a505f6971.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot to a form with filled in data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/232654557-78b9952f-c48e-4519-b77a-d3df10a68ba7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of a Data output to show that it is in a clean<br>mannner<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/karthikkk999/IS601-006/pull/18">https://github.com/karthikkk999/IS601-006/pull/18</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <div><font size="3"><b style="">Highlight the basic styling you chose for the general elements like<br>nav, forms, etc:</b><br></font></div><font size="3">We did not add css for the elements from scratch.<br>We used Bootstrap to add pre-defined styles and layout options to the HTML.&nbsp;For<br>example, the "navbar" (navigation bar) in the layout.html is styled using Bootstrap classes<br>such as "navbar", "navbar-expand-lg", "navbar-light", "bg-light", and "rounded-bottom".&nbsp;</font><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/232643179-d6ace20e-e915-41a0-8aa5-c6c348faa7cf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of email already taken message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/232656184-c6114f6e-973c-4cba-b388-6535b09e24fd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Invalid username message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/232629806-432546a9-34c2-44b0-835b-0c03788b334c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of password mis-match message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/karthikkk999/IS601-006/pull/18">https://github.com/karthikkk999/IS601-006/pull/18</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <p><font size="3"><b style="">Describe what we&#39;ve been doing to handle technical messages and converting<br>them to being friendly to our users</b><br>We had handled technical messages and converted<br>them into user-friendly messages using Flask&#39;s flash messages. Whenever an error occurs during<br>user authentication, we use the flash() function to store an error message in<br>the session, which can be displayed to the user on the next page<br>load.</font><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/232265132-1d9b0685-ffbc-40c4-8c0b-729e7335aeef.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email and username prefilled properly<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/karthikkk999/IS601-006/pull/18">https://github.com/karthikkk999/IS601-006/pull/18</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <div><font size="3">By giving the user's information to the form object in the view<br>function, the email and username fields are pre-filled with the current user's information.<br>When the profile page is rendered, the view function retrieves the current user's<br>information, creates a ProfileForm object, and populates the form fields with the user's<br>information by calling the ProfileForm object's process() method and passing the user's information<br>as arguments. This pre-populates the form fields with the current user's information, allowing<br>the user to easily change their profile without having to re-enter their email<br>address and username.</font><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/232628190-99b5aa52-cde5-49e0-b32a-b1798955119d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of username already taken validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/232628093-ca757b1a-0b05-4d30-9440-9fca660d181b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of email already used validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/232565352-7217711b-0e94-4831-9bd5-f017eb19da14.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of password validation prompt for incorrect format <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/232628554-47f90c4a-08ea-441b-aed5-683acf5c000c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of email validation prompt for incorrect format <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/232629806-432546a9-34c2-44b0-835b-0c03788b334c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of password mismatch message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/232634313-b4ffffe1-d4b7-48e8-8002-73b7f01a6d8d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Invalid username<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/232658941-40514101-2c00-4a23-96a0-67c5571d1f3c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of record with user name &#39;karthik55&#39; before the update (Please note the<br>email)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/232659255-055fef0b-b0b0-4d26-a88b-2689ee467813.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of record with user name &#39;karthik55&#39; after the update with email changed<br>to  <a href="mailto:&#107;&#x61;&#114;&#116;&#x68;&#x69;&#107;&#57;&#x39;&#x40;&#x67;&#109;&#97;&#105;&#x6c;&#x2e;&#99;&#111;&#109;">&#107;&#x61;&#114;&#116;&#x68;&#x69;&#107;&#57;&#x39;&#x40;&#x67;&#109;&#97;&#105;&#x6c;&#x2e;&#99;&#111;&#109;</a> from <a href="mailto:&#x6b;&#97;&#x72;&#116;&#104;&#x69;&#x6b;&#53;&#53;&#64;&#x67;&#x6d;&#x61;&#x69;&#x6c;&#46;&#99;&#x6f;&#109;">&#x6b;&#97;&#x72;&#116;&#104;&#x69;&#x6b;&#53;&#53;&#64;&#x67;&#x6d;&#x61;&#x69;&#x6c;&#46;&#99;&#x6f;&#109;</a><br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/232659307-d999c16b-de13-423a-a8eb-1a8586382dfa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of successful update<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/karthikkk999/IS601-006/pull/18">https://github.com/karthikkk999/IS601-006/pull/18</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <p><font size="3">the profile() function first obtains the user ID of the currently logged-in<br>user, then creates an instance of the ProfileForm class, which is responsible for<br>handle the form for updating the user&#39;s profile information. Then we check for<br>a valid user name using a regex expression. Later we check if the<br>user name of email is assigned to another record using a function called<br>check_duplicate which flashes an error message if user name/email not available.&nbsp;Then we check<br>for invalid password in the form itself using wtf form validators (minimum 8<br>length, one upper, one lower case etc..). Then we compare the password with<br>the confirm password and if it does not match we flash an error<br>message. If it matches we use and Update query and update the record<br>with the passed data.</font><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>Learning:<div>I learned about wtf forms. how we can use the validators in them<br>and create constraints for our text fields like passwords and emails instead of<br>writing them from scratch.</div><div>Also, learned or got better at using using routes in<br>flask and define separate functions for different use cases.</div><div>Also, had a good practice<br>on regex expressions which I had used for valid password and user name<br>checks.</div><div>I had learned how to deploy&nbsp; and work with Heroku now, as I<br>had extensive practice with it in this milestone.&nbsp;</div><div><br></div><div>Issues:<br>I had with the invalid password<br>message not being shown. later when I had&nbsp; used correct validators like&nbsp;Regexp it<br>got fixed.<br></div><div>I also had to fix some error message not showing but the<br>app working correctly as the flash() was not called in the appropriate places.<br>I fixed this after debugging.&nbsp;</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sk3374-prod.herokuapp.com/login">https://is601-sk3374-prod.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone1-deliverable/grade/sk3374" target="_blank">Grading</a></td></tr></table>