<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 2 - Burgers</td></tr>
<tr><td> <em>Student: </em> Sai Karthik Kasumurthy (sk3374)</td></tr>
<tr><td> <em>Generated: </em> 3/20/2023 2:42:53 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-2-burgers/grade/sk3374" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Create a new branch per the desired branch name below</li><li>Add the baseline files from the following link:&nbsp;<a href="https://gist.github.com/MattToegel/028db0e3fd2b20c1fb8e284b341292bb">https://gist.github.com/MattToegel/028db0e3fd2b20c1fb8e284b341292bb</a>&nbsp;</li><li>Put them into a subfolder in your repository folder (I called my folder BurgerMachine)</li><li>git add .</li><li>git commit -m "baseline files"</li><li>git push origin (name of desired branch below)</li><li>You can go to github and open the pull request for evidence capturing later (don't close/merge the pull request until you're done with the assignment)</li><li>Do the below tasks and fill in the below entries</li><ol><li>git add/commit after any significant changes to build up history</li></ol><li>Save the input and generate the submission markdown file (copy to clipboard or download the file)</li><li>Name it something relevant to the assignment if it's not named already</li><li>git add the submission file</li><li>git commit the submission file</li><li>git push the submission file</li><li>Complete the pull request to dev</li><li>Create a pull request from dev to prod</li><li>Go to the prod branch on github, navigate to the submission file</li><li>Paste that link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Changes - Add the calculate_cost() implementation </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of the updated method calculate_cost()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/226425946-5609c40e-5bc0-4ba6-afeb-49689ed98d71.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Added the screenshot of the logic implemented for calculate_cost()  function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/226123923-4882133d-df55-4d99-9b97-d675667f0399.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Added the screenshot of the logic in the input message to show the<br>currency in proper format<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/226426301-d9bc5043-9776-4441-ad37-dd1c616d6799.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Added the screenshot of handle_pay() function to handle the currency format<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain the approach to implementing the calculation</td></tr>
<tr><td> <em>Response:</em> <p>Logic for calculate_cost:<br><div>To sum up the costs of each item, we use a<br>for loop that iterates over each element in the inprogress_burger list and then<br>we used an in-built function: sum() to sum up the items that were<br>fetched. We stored this result in total_cost and returned it.&nbsp;Rounded the total to<br>two decimal places for consistency and to reflect the currency format</div><div><br></div><div>handling the currency<br>format:</div><div>For handling the currency format in the input message we used a format<br>specifier .2f to show the calculated cost with 2 decimal places and also<br>added $ before the amount to show the amount in USD</div><div><br></div><div>Also in handle_pay()<br>function we removed the &#39;$&#39; if it has been entered by user. This<br>gives user more flexibility.</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Exception Handling </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of adjusted code to handle exceptions</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/226132787-d6e2b857-a91f-408e-9fb7-3f805373df85.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Adding the screenshot of the handled exceptions in the run(self) <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each exception handling process</td></tr>
<tr><td> <em>Response:</em> <div><b>OutOfStockException:</b>&nbsp;</div><div>I have used a print statement to show the out of stock message<br>(used the value in self.currently_selecting.name to show the current state)</div><div><b>NeedsCleaningException:</b>&nbsp;</div><div>I have used a<br>print to let user know machine needs cleaning. I then used input and<br>a message to ask user to type 'clean' to clean the machine</div><div>If user<br>enters clean, we print a message the machine was cleaned</div><div>If user enters any<br>other word other than clean we say machine was not cleaned</div><div><b>InvalidChoiceException:</b></div><div>I have used<br>a print statement to show an invalid choice message (used the value in<br>self.currently_selecting.name to show the current state)</div><div><b>ExceededRemainingChoicesException:</b></div><div>I had used a print statement to show<br>the choices exceeded at that particular stage (used the value in self.currently_selecting.name to<br>show the current state)</div><div>And then check the current stage using an if elif<br>and stored the next state in self.currently_selecting</div><div><b>InvalidPaymentException:</b></div><div>I have used a print statement to<br>show that Invalid payment amount had entered and ask to try again</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Test Cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of test cases per the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/226427156-038b2c4f-9f60-4712-80cc-489bceec29d5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Added Screenshot of TestCase1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/226429894-ef9af806-1b3e-4bb3-89fe-7c6cd9d985a0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Added Screenshot of TestCase2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/226430033-999a966a-8dbb-4809-b60f-1bc6111664ea.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Added Screenshot of TestCase3<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/226430101-627ce4e0-5754-4a3b-bfa1-3a482b095a3e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Added Screenshot of TestCase4<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/226430208-d626a594-c6a5-42dd-9809-c21cce239be2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Added Screenshot of TestCase5<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/226430472-dba6d7fe-620d-48c8-998d-32d3ea6f1845.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Added Screenshot of TestCase6<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/226430570-a63d59d1-f08c-4443-a613-178878b89826.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Added Screenshot of TestCase7<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/226430634-4bc57df5-7b20-4cdf-8131-8d3aeaf248a1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Added Screenshot of TestCase8<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/226431151-9c30ea08-d6d5-432e-839a-003491e84067.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of all the test cases (1 to 8) passing<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each test case logic</td></tr>
<tr><td> <em>Response:</em> <p><b>Test1 - bun must be the first selection (can&#39;t add patties/toppings without a<br>bun choice):</b><div>We reset the state of the machine object. and use it for<br>all the test cases<div><div>Then I have used context manager - pytest.raises to check<br>if an InvalidStageException is raised when we selected a patty without a bun<br>choice.</div><div>Used context manager to check if an Exception is raised when we selected<br>a toppings without a bun choice and a patty first</div></div></div><div><br></div><div><b>Test 2 - can<br>only add patties if they&#39;re in stock:<br></b><div>First made made the quantity value of<br>all patties to 0 using a for ...in and iterating over the patties<br>in the object.<br></div><div>Then we see if we get an OutOfStockException when we try<br>to pick a patty when the quantity of all patties is 0.</div><div>We use<br>context manager - pytest.raises() to check if an expected Exception has raised</div><div>Then we<br>restock all the patties (i.e. change back the quantity value of all the<br>patties)</div></div><div><br></div><div><b>Test 3 - can only add toppings if they&#39;re in stock:</b></div><div><div style="">First made<br>made the quantity value of all toppings to 0 using a for ...in<br>and iterating over the toppings in the object<br></div><div style="">&nbsp;Then we see if we<br>get an OutOfStockException when we try to pick a topping when the quantity<br>of all toppings is 0.</div><div style="">We use context manager - pytest.raises() to check<br>if an expected Exception has raised</div><div style="">Then we restock all the toppings (i.e.<br>change back the quantity value of all the toppings)</div></div><div style=""><br></div><div style=""><b>Test 4 -<br>Can add up to 3 patties of any combination:<br></b><div>First we select a bun<br>using handle_bun function and passing the &quot;no bun&quot; option.</div><div>Then we select Beef as<br>patty 3 times using for - in range(3). This means we already used<br>3 patties.</div><div>And then when we select the 4th patty, we check if the<br>system is throwing an ExceededRemainingChoicesException using the context manager pytest.raises.</div><div><br></div><div><b>Test 5 - Can<br>add up to 3 toppings of any combination:</b></div><div><div style="">First we select a bun<br>using handle_bun function and passing the &quot;no bun&quot; option.</div><div style="">And then we select<br>lettuce as topping 3 times using for - in range(3). This means we<br>already used 3 toppings.</div><div style="">Then when we select the 4th topping, we check<br>if the system is throwing an ExceededRemainingChoicesException using the context manager pytest.raises.</div><div style=""><br></div>&lt;div<br>style=&quot;&quot;&gt;<b>Test 6 - cost must be calculated properly based on the choices:<br></b><div>We add<br>the bun, patties and toppings using the appropriate handle_bun(), handle_patty() and handle_toppings() functions&nbsp;</div><div>After<br>the burger has been made, we use handle_toppings(&quot;done&quot;) to mark the burger as<br>done</div><div>Then assert the calculate_cost with the expected amount to see if it is<br>calculating the cost accurately</div><div>Then we call handle_pay by passing the calculated amount and<br>the amount the user gives manually&nbsp;</div><div>The above step is to check the currency<br>formatting&nbsp;&nbsp;</div><div>We repeat this process 3 times.&nbsp;</div><div>In the 2nd burger while while in handle_pay<br>we give an amount without the &#39;$&#39; sign and it should work</div><div>In the<br>3rd burger while while in handle_pay we involuntarily pass an incorrect amount and<br>so an InvalidPaymentException is raised</div><div><br></div><div><b>Test 7 - Total Sales (sum of costs) must<br>be calculated properly:<br></b><div>Then we add the bun, patties and toppings using the appropriate<br>handle_bun(), handle_patty() and handle_toppings() functions&nbsp;<br></div><div>After the burger has been made, we use handle_toppings(&quot;done&quot;)<br>to mark the burger as done</div><div>The calculate the cost of the burger and<br>send it to the handle_pay function</div><div>Later we assert the value of the the<br>total_sales.</div><div>We repeat this process 3 times.&nbsp;</div><div>2nd time the total_sales should include the cost<br>of the first burger and the second burger.</div><div>And in the 3rd time the<br>assert of total_sales would include the total cost of the 3 burgers.</div></div><div><br></div><div><b>Test 8<br>- Total number of burgers that were made should be stored accurately:</b></div><div>We choose<br>the bun, patty and topping using the handle_bun(), handle_patty() and handle_toppings functions.<div>After the<br>burger is made, we mark it as done using the handle_toppings() function</div><div>Later we<br>calculate the cost of the burger and send it to the handle_pay() function</div><div>In<br>handle_pay() function we increment the value of the total_burgers by 1 everytime it<br>is called</div><div>Then we assert the value of total_burger witht he expected value.</div><div>We repeat<br>this process 3 times.</div><div>Each time a new burger is made the value of<br>total_burgers should be incremented by 1.&nbsp;&nbsp;</div></div></div><div style="font-weight: bold;"><br></div></div><div><b><br></b><br></div></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request for the assignment</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/karthikkk999/IS601-006/pull/14">https://github.com/karthikkk999/IS601-006/pull/14</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain any issues/difficulties or something you learned while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <div>Issues:</div>1) I forgot to add __init__.py in the tests folder. So ran into<br>an issue while running the pytest but later fixed it.<div>2) I had an<br>issue while running all the test cases at once because in one of<br>the test cases I had changed the quantity of all the patties and<br>toppings to 0.</div><div>Fixed this by changing back the quantity to 10 (restocking) for<br>patties and toppings once I had used the scenario for testing.</div><div>3)&nbsp; Also forgot<br>to add the necessary intermediate steps while making a buger ('next' and 'done')<br>in test cases and spent some time figuring this out.&nbsp;</div><div><br></div><div>Learnings:</div><div>1) I learned how<br>to fixtures properly</div><div>2) Got to know how use the objects in pytest multiple<br>times for test cases.</div><div>3) Also learned how we can use Exception to handle<br>several errors that can be realized while developing the code itself</div><div>4) Learned about<br>the pytest.raises context manager in pytest which we can use to test the<br>Exceptions handlers that we created&nbsp;</div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of successful output</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/226433824-fd03d0a8-c8a2-4e52-80d8-c7ddd17d27d0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the output for Burger Combination 1 <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/226434134-2c41b15b-0bfa-43d5-8f65-1621417a916a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the output for Burger Combination 2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/226434396-227c021e-7928-4fda-9f7d-453d40bb0ef8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the output for Burger Combination 3<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/226434765-70bf8b10-a1db-427e-8009-f2075697c2bb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the output of the InvalidChoiceException<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/226435007-c5e2a36a-0b19-48d4-b1f4-eb111fe531b8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the output of the  ExceededRemainingChoicesException<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/226435428-4bdb82d6-268b-4b7f-96ec-f52b5f2be5b8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the output of the OutOfStockException<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/226435884-402b6d08-5b0a-4c8e-87d1-f55fe6a637ce.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the output of the NeedsCleaningException<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/226435990-2566fcf4-019a-442c-9433-1414597de56b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the output of the InvalidPaymentException<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-2-burgers/grade/sk3374" target="_blank">Grading</a></td></tr></table>