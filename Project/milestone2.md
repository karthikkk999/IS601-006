<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 Shop Project</td></tr>
<tr><td> <em>Student: </em> Sai Karthik Kasumurthy (sk3374)</td></tr>
<tr><td> <em>Generated: </em> 4/24/2023 3:07:50 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone-2-shop-project/grade/sk3374" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone2 branch</li><li>Create a new markdown file called milestone2.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone2.md</li><li>Add/commit/push the changes to Milestone2</li><li>PR Milestone2 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 3</li><li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on github and everywhere else. Images are only accepted from dev or prod, not local host. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Users with admin or shop owner will be able to add products </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of admin create item page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/234051007-d83ee7b0-f67e-4600-84a2-c9e0cf8c5baa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Create item page with valid data filled in<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/234051702-772ea085-34f2-4c8f-92a4-01fbc90cecd6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Create item page after submitting the form<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of populated Products table clearly showing the columns</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/234051337-80f76c1f-44ad-4f10-b257-b41dbd81f2b9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Products table with the required columns along with the &#39;Lays&#39; record that we<br>have inserted earlier<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly describe the code flow for creating a Product</td></tr>
<tr><td> <em>Response:</em> <p>We use ItemForm object which creates a&nbsp; forma for adding and editing a<br>product when in the /admin/item route. After filling the data and submitting the<br>data.&nbsp;<div>Then, we try to fetch the &#39;id&#39; from the form.&nbsp;</div><div>If id is fetched<br>we do an edit to the existing product using an UPDATE query with<br>the fields that we got from the form.</div><div>else, if id is None we<br>create a new object using and INSERT query the fields that we got<br>from the form.</div><div>After Inserting or Updating is done, we fetch the id on<br>which the action is done and populate the form with the product data</div><div>Then<br>we user render template which displays the form and any error messages</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/karthikkk999/IS601-006/pull/20">https://github.com/karthikkk999/IS601-006/pull/20</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sk3374-prod.herokuapp.com/admin/item">https://is601-sk3374-prod.herokuapp.com/admin/item</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Any user can see visible products on the Shop Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the Shop page showing 10 items without filters/sorting applied</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/234062459-508c4515-33ee-4ee1-a7b3-f503de160c45.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Added screenshot of shop page with 10 items without filters/sorting applied<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Shop page showing both filters and a different sorting applied (should be more than 1 sample product)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/234063403-b3e0b4f0-53b3-430d-8f85-1b61be9e58df.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Added screenshot of  filter (Food) and a sorting (Price High to Low)<br>applied.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the filter/sort logic from the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/234064128-3ac659f2-6692-4d0c-a77d-cdfa8aa0e513.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the filter/sort logic from the code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Briefly explain how the results are shown and how the filters are applied</td></tr>
<tr><td> <em>Response:</em> <p>In the shop_list() function we fetch the arguments name, category and price from<br>the form if supplied.<div>Later we use a SLELECT query to fetch the products<br>using these the fetched arguments.&nbsp;</div><div>If name is given we use it in the<br>WHERE clause and fetch only the products whose name matches with the name<br>argument.</div><div>If category argument is fetched from the form we use it in the<br>WHERE clause to get the products whose category matches.</div><div>Later we use the value<br>of price only if present which would be either ASC (ascending if Low<br>to High) or DESC (descending if High to Low) and use it to<br>order the records.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/karthikkk999/IS601-006/pull/20">https://github.com/karthikkk999/IS601-006/pull/20</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sk3374-prod.herokuapp.com/shop">https://is601-sk3374-prod.herokuapp.com/shop</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Show Admin/Shop Owner Product List (this is not the Shop page and should show visibility status) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of the Admin List page/results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/234066530-d8578367-2667-4e41-8247-b9169a27f225.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the Product List for admin where we can see non-visible products<br>too.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how the results are shown</td></tr>
<tr><td> <em>Response:</em> <p>In order to have access to the admin/items route we check if the<br>user is an admin using the Flask-Principal permission requirement.<div>If the user is an<br>admin we fetch all the records from the&nbsp;IS601_S_Products table and display it to<br>the screen using a SELECT query with no filters applied.</div><div>And thus we get<br>both visible and non-visible records.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/karthikkk999/IS601-006/pull/20">https://github.com/karthikkk999/IS601-006/pull/20</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sk3374-prod.herokuapp.com/admin/items">https://is601-sk3374-prod.herokuapp.com/admin/items</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Admin/Shop Owner Edit button </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the edit button visible to the Admin on the Shop page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/234067609-49a9a3a2-27ad-46af-ad2c-539721869c57.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the edit button visible to the Admin on the Shop page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the edit button visible to the Admin on the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/234067861-d8284034-8f61-4f46-9a84-a062f3c21465.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the edit button visible to the Admin on the Product Details<br>Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot showing the edit button visible to the Admin on the Admin Product List Page (The admin page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/234067950-c228b46b-bda9-46a6-9279-6f463972635a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the edit button visible to the Admin on the Admin Product<br>List Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after screenshot of Editing a Product via the Admin Edit Product Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/234068201-8a4cfb7e-a002-4082-be1b-7d3b8339ba92.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Admin Edit Product Page before changing the stock of Sofa (90)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/234068767-fbe2d61a-45e0-46cf-a236-23a114bc7155.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Admin Edit Product Page after changing the stock of Sofa to<br>9<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <p>We use /admin/item route to perform the product details update actions. First we<br>fetch the id for the product which we want to edit.&nbsp;<br>Then we use<br>an UPDATE query with id fetched to update the details of the product<br>with the form data which would have the updated data.<div>On successful update we<br>display a Updated message using flash and if the update failed we show<br>the same using a flash message.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/karthikkk999/IS601-006/pull/20">https://github.com/karthikkk999/IS601-006/pull/20</a> </td></tr>
<tr><td> <em>Sub-Task 7: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sk3374-prod.herokuapp.com/shop">https://is601-sk3374-prod.herokuapp.com/shop</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Product Details Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the button (clickable item) that directs the user to the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/234071945-eb5bda8b-66bc-4e3a-baa8-f51a12839401.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the button that directs the user to the Product Details Page<br>(Before clicking on &#39;Pen&#39;)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the result of the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/234072074-60da80d2-b2d3-4113-9931-803d233ef524.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the Product Details Page (after clicking on &#39;Pen&#39;)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <p>In the shop page we had a href to shop/itemdetails route on the<br>text on every product that is displayed.&nbsp;<div>If the user clicks on the product<br>name the shop/itemdetails would handle the action.</div><div>In itemdetails() we get the id and<br>fetch the feilds of the details of the product using a SELECT query.</div><div>Then<br>we pass these fields that were fetched using the SELECT query to item_details.html<br>using render_template and display them on the screen</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/karthikkk999/IS601-006/pull/20">https://github.com/karthikkk999/IS601-006/pull/20</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file (can be any specific item)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sk3374-prod.herokuapp.com/itemdetails?id=1">https://is601-sk3374-prod.herokuapp.com/itemdetails?id=1</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add to Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the success message of adding to cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/234073386-fccfd8f4-8897-4b1d-864c-906623a236c1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the success message of adding to cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the error message of adding to cart (i.e., when not logged in)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/234074118-ee9cec5e-8e1b-4006-8563-dd2428c20941.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the error message of adding to cart after user logged out<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Cart table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/234074298-3cac8e5e-768a-4756-a285-8460c34ab142.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the Cart table with data in it<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Tell how your cart works (1 cart per user; multiple carts per user)</td></tr>
<tr><td> <em>Response:</em> <p>Each user has his own cart. Products added to a card for one<br>user cannot be viewed/edited by another.<div>We had implement this rule by creating a<br>composite key of product_id and user_id for the IS601_S_Cart. So every product that<br>a user adds to this table gets stored along with his user_id.</div><div>So we<br>use this composite key to get only the products which are linked to<br>the user that is currently logged in.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Explain the process of add to cart</td></tr>
<tr><td> <em>Response:</em> <p>User needs to be logged in to add items to the cart.<div>When user<br>clicks on ADD button, the route shop/cart handles the functionality.</div><div>We fetch the id,<br>set quantity of the item to 1, and current_user_id form the form.&nbsp;</div><div>Then we<br>get the cost and name of the product using a SELECT query.</div><div>Then we<br>add the item to the cart using an INSERT query. Here we insert<br>the user_id to along with the product details.</div><div>For successful insert we flash a<br>message saying Added success and for fails it says Error adding to cart.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/karthikkk999/IS601-006/pull/20">https://github.com/karthikkk999/IS601-006/pull/20</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> User will be able to see their Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the Cart View</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/234082968-3b000ae4-a35a-4441-ae61-600a2c802086.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Cart View which shows the subtotal for each line, cart<br>total, link to product details on the name of the each product<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain how the cart is being shown from a code perspective along with the subtotal and total calculations</td></tr>
<tr><td> <em>Response:</em> <p>In the shop/cart route we use a SELECT query to display the products<br>in the cart for a specific user. We use user_id in the WHERE<br>clause to fetch only the items liked to the user.<div>In order to get<br>the cost we JOIN the&nbsp;&nbsp;IS601_S_Cart table with IS601_S_Products.<div>And To get the subtotal for<br>each record we multiple the quantity of each item with the cost of<br>each product.</div><div>We calculate the total in the html by summing up all the<br>subtotal fields that are passed to the page.</div></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/karthikkk999/IS601-006/pull/20">https://github.com/karthikkk999/IS601-006/pull/20</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sk3374-prod.herokuapp.com/cart">https://is601-sk3374-prod.herokuapp.com/cart</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> User can update cart quantity </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a before and after screenshot of Cart Quantity update</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/234085241-d11dbeb3-e430-448c-9965-794060759b78.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Cart before updating the quantity of Pen<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/234085378-55399238-55c3-4280-b48a-d29f04f7e423.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Cart after updating the quantity of Pen to 8 from 0<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show a before and after screenshot of setting Cart Quantity to 0</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/234085510-f9505f5d-d11e-4cb0-8817-80ebfc4422d0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> screenshot Cart before updating the quantity of Lays to 0<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/234085650-b5e0c609-57db-44ed-b602-e21e066c2750.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot Cart after updating the quantity of Lays to 0. It gets removed<br>from the cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show how a negative quantity is handled</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/234086846-e95520c9-b75f-4540-b9f5-711a4ccd5974.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the validation when the quantity is negative for an item in<br>the cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain the update process including how a value of 0 and negatives are handled</td></tr>
<tr><td> <em>Response:</em> <div>For quantity 0:</div><div>We only update or insert the records in to the Cart<br>table when the value of quantity of cart is greater than 0. We<br>included an if condition for this.</div>So, when value of quantity is 0, it<br>goes to the else block and there we delete the item from the<br>cart and show a flash message saying that item was removed from the<br>cart.<div><br></div><div>For negative quantity:</div><div>We have a check in the cart.html saying the minimum value<br>for quantity should be 0. That's why we get a validation saying cannot<br>be less than 0 when we try to update the cart with quantity<br>as negative value.<br><br></div><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/karthikkk999/IS601-006/pull/20">https://github.com/karthikkk999/IS601-006/pull/20</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Cart Item Removal </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a before and after screenshot of deleting a single item from the Cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/234091923-a5c05223-2c19-420a-a45e-eeec19af86da.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of cart before removing the soap<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/234091993-35593946-d60e-4bc1-9770-c9f5f37471cc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of cart after removing the soap<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after screenshot of clearing the cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/234087716-6cca83f5-a4c1-49f7-925f-2cef2f2b8734.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot before clearing the cart<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420633/234087854-0d974110-d5d5-4bf3-a655-99903bbcab8c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot after clearing the cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how each delete process works</td></tr>
<tr><td> <em>Response:</em> <p>For deleting single item:<br>When we delete a single item using the X button<br>in the actions column in the cart. For the product we set the<br>value of quantity to -1.<div>and then in the shop/cart route we delete the<br>product for the user when the quantity of the product in the cart<br>is less than 0 using a DELETE query along with the product_id and<br>the user_id in the WHERE clause.</div><div><br></div><div>For clearing cart:</div><div>When we select to clear the<br>cart we pass delete_all = 1 to the shop/cart route and if delete_all<br>is 1 we would delete the products in the cart for the specific<br>user by using a DELETE query with a user_id in the WHERE clause.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/karthikkk999/IS601-006/pull/20">https://github.com/karthikkk999/IS601-006/pull/20</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>Issues:&nbsp;<div>Initially I had faced an issue while selecting the categories as I had<br>hardcoded specific ones in the html. It was not allowing me to choose<br>the ones that I had creating form the Item Add page. To fix<br>this I used a query to fetch all the distinct categories form the<br>Items table and display it in the dropdown.<br></div><div><br></div><div>Also, I had mis typed DESC<br>as DES for the &#39;Hight to Low&#39; sort value so my items were<br>not getting sorted properly. Later noticed this and fixed it.</div><div><br></div><div>Learning:<br>I had learned how<br>to pass the record and additional parameters to the html from the routes<br>that I have created.</div><div>Also learned about overwriting the default properties of the bootstrap<br>css so we could customize it as required.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sk3374-prod.herokuapp.com/login">https://is601-sk3374-prod.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone-2-shop-project/grade/sk3374" target="_blank">Grading</a></td></tr></table>