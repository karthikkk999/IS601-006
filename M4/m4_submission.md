<table><tr><td> <em>Assignment: </em> M4-Simple-Calc</td></tr>
<tr><td> <em>Student: </em> Sai Karthik Kasumurthy (sk3374)</td></tr>
<tr><td> <em>Generated: </em> 2/27/2023 8:40:30 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/m4-simple-calc/grade/sk3374" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Make sure you're working in an up to date branch</p><ul><li><code>git checkout dev</code></li><li><code>git pull origin dev</code></li><li><code>git checkout -b M4-Simple-Calc</code></li></ul><p>This will likely be started in class.</p><p>Steps:</p><ol><li>Create a new Folder called M4</li><li>Create a new file called MyCalc.py inside this folder</li><li>Create a MyCalc Class</li><li>Define basic addition / subtraction / multiplication / division functions<ol><li>These functions should update an internal variable as a running total/value called&nbsp;<code><b>ans</b></code></li><li>All functions must properly handle the math given standard math scenarios (i.e., show proper messages when trying to divide by zero for example)</li><li>Since you'll likely be taking screenshots of the code, make sure you add a comment with your ucid and the date</li></ol></li><li>Define a "main" logic to run when the program runs</li><li>This logic should ask for user input<ol><li>The input can be any valid number, any valid math operator, and any valid number (i.e., 2 * 2)<ol><li>This will do an immediate calculation, print it, and store the answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li><li>Alternatively, the input can be&nbsp;<code>ans</code>, any valid math operator, any valid number (i.e.,&nbsp;<code>ans</code>&nbsp;* 2)<ol><li>This will use the previous answer (or 0 if not set) as part of the calculation, print it, and will store the new answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li></ol></li><li>Create a test case for each scenario that utilize functions to have expected input and compare against expected output, all cases should pass (test cases should have a series of data passed into them)<ol><li>Test number-add-number</li><li>Test ans-add-number</li><li>Test number-sub-number</li><li>Test ans-sum-number</li><li>Test number-mult-number</li><li>Test ans-mult-number</li><li>Test number-div-number</li><li>Test ans-div-number</li></ol></li><li>Create a new file called m4_submission.md inside the M4 folder</li><li>Fill out the below deliverables</li><li>Generate the markdown and paste it into the m4_submission.md</li><li><code>git add .</code></li><li><code>git commit -m "adding m4 hw"</code></li><li><code>git push origin M4-Simple-Calc</code></li><li>Create a pull request M4-Simple-Calc to dev</li><li>Create a pull request dev to prod (after the previous one is merged)</li><li>Navigate to the prod branch on github, go to the M4 folder, click the m4_submission.md</li><li>Submit this link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Snippets (Make sure each screenshot has a comment showing your ucid and the date it was written) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of valid Addition Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/221388165-fb5d13cf-3ac1-46cf-b0da-97f2a796dced.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>added the logic for the addition function along with comments explaining the code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/221388247-08f64230-8dc9-44de-a72c-9fc91c7684b0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>added the logic for the calculate() function which will be used to the<br>individual function that perform the math using the do_math dictionary<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/221389996-1b9f9066-3806-48c2-acc4-fb3b37a04f30.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output of add() function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of valid Subtraction Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/221388193-a62f9920-f0c0-4168-9193-866e6b336247.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>added the logic for the subtraction function along with comments explaining the code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/221390027-5b308c4f-eb68-4c97-954b-594c3411a691.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output of sub() function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of valid Multiplication Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/221388200-77a28731-fe41-4793-bd8b-301f6a003d59.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>added the logic for the multiplication function along with comments explaining the code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/221390057-f7286140-01ba-4caa-b76b-94a0d1f2ce6f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>added the output of the mul() function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of valid division Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/221388209-506ff491-3ce5-4c08-8b42-fcd34c18d7c6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>added the logic for the division function along with comments explaining the code.<br>Also added the divide by zero error.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/221390113-a9794275-6aa6-4669-8ed6-9953d2296005.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>added the output of the div() function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/221390139-079ef9a7-770f-4937-9eea-ab68c31f8511.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>added the output of divide by zero operation<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Test Case Validations </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of passing number-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/221389744-080f6a6e-c985-49fc-8f40-ac8c16707ae3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the function test_number_add_number which tests the addition using different data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/221729272-5f398424-ee01-42b9-b60f-fc352790ffbf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>added the output of the test case passing when pytest is used<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of passing ans-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/221729393-f1da19c0-7875-4163-9e22-fe93f444bc18.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the function test_ans_add_number which tests the addition when &quot;ans&quot; is used,<br>using different data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/221729467-deef6495-630a-4041-85fc-905aa9bf65f7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>added the output of the test case passing when pytest is used<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of passing number-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/221389807-211fe876-dcec-49ef-be24-e9b3be71ad6a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the function test_number_sub_number which tests the subtraction using different data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/221729533-00b8bd43-e22f-44f7-9744-bd133c56b916.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>added the output of the test case passing when pytest is used<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshots of passing ans-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/221729581-ea4e4caf-3cb8-417a-b88c-e53b31741fc9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the function test_ans_sub_number which tests the subtraction when &quot;ans&quot; is used,<br>using different data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/221729645-06031c8e-ce8f-445c-a06a-fe1a02129366.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>added the output of the test case passing when pytest is used<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Screenshots of passing number-mult-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/221389831-eeb17074-f38f-47f1-b49c-3b5860a1602d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the function test_number_mult_number which tests the multiplication using different data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/221729684-dc266fed-9ae7-4051-acb6-451c90057c7c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>added the output of the test case passing when pytest is used<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Screenshots of passing ans-multi-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/221729759-9c6c352c-29e9-4b6f-a0a5-2a5615d13d15.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the function test_ans_mult_number which tests the multiplication when &quot;ans&quot; is used,<br>using different data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/221729808-18048fcc-62fc-4c60-86c5-d6386c2e0688.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>added the output of the test case passing when pytest is used<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Screenshots of passing number-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/221389890-ccceb0e3-593e-49b3-84da-903feeb5e91f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the function test_number_div_number which tests the division using different data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/221729904-c2f24cc2-7ad0-46b3-ab83-6c5a8d5c4f52.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>added the output of the test case passing when pytest is used<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Screenshots of passing ans-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/221730323-7a73cf3e-8a78-4e80-bb26-3c682ccb3f4a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the function test_ans_div_number which tests the division when &quot;ans&quot; is used,<br>using different data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/221730048-094092bb-8e56-4f8b-8280-d8c2471d07a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>added the output of the test case passing when pytest is used<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Briefly talk about anything you learn during this assignment/module</td></tr>
<tr><td> <em>Response:</em> <p>Learned about writing test cases and using pytest to test them.&nbsp;<div>Got to know<br>about pytest and what is does.</div><div>Understood that dictionaries are a good tool in<br>python (I used them to store the operator as key and function reference<br>as value)</div><div><br></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Discuss how test cases work and anything new you learned about them while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>Test cases in python are used to test the expected behavior of the<br>program.<div>They are written like functions that can validate and compare with the expected<br>result using assert keyword.</div><div>These function should start with &#39;test_&#39; as the for the<br>pytest to execute/test them.</div><div>Test cases help to catch any issues in the code<br>even though it might be syntactically correct.</div><div>Also, got to know that we can<br>test the same function using different arguments which are called parameterized tests.</div><div><br></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the pull request of M4-Simple-Calc to Dev link</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/karthikkk999/IS601-006/pull/6">https://github.com/karthikkk999/IS601-006/pull/6</a> </td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/karthikkk999/IS601-006/pull/8">https://github.com/karthikkk999/IS601-006/pull/8</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/m4-simple-calc/grade/sk3374" target="_blank">Grading</a></td></tr></table>