# Posh Portables - E-Commerce Site - Testing

![Mock-up]()

#### **By Lauren Pechey**
[Click here to view the live web application](https://posh-portables-6801c9648247.herokuapp.com/)

This is the testing documentation for my e-commerce web application: Posh Portables.

- - -
## Table of Contents

- [Introduction](#introduction)
- [Automated Testing](#automated-testing-using-test-driven-development)
- [Validation](#validation)
    - [HTML Validation](#html-validation)
    - [CSS Validation](#css-validation)
    - [JavaScript Linting](#javascript-linting)
    - [Python Linting](#python-linting)
    - [Accessibility Testing](#accessibility)
    - [Performance Testing](#performance)
- [Feature Testing](#feature-testing)
    - [Responsiveness/Device Testing](#responsiveness--devices)
    - [Browser Compatibility](#browser-compatibility)
    - [Feature Testing Results](#feature-testing-results)
- [User Stories Testing](#user-stories-testing)
- [Bugs and Fixes](#bugs--fixes)


---

## Introduction

In my testing I developed a comprehensive testing plan to make sure that the site was functioning correctly. I used a combination of automated testing using Django's built in test functionality and manual testing. The site was tested throughout the process, both in the development and deployed version of the sites. All the test results detailed below are based on the [deployed site](https://posh-portables-6801c9648247.herokuapp.com/).

---

## Automated Testing using Test Driven Development

During development I tried to maintain a test driven development approach. This was my first experience of using automated testing on a project so I kept things simple and wrote and ran tests appropriate to my experience level (backed up by rigorous manual testing both during the development process and at the end - see [feature testing](#feature-testing)). This allowed me to build my knowledge within the scope and time restraints of the project and course requirements. As part of the TDD (test driven development) approach; all automated tests were written after the stage of development to make sure that all features were checked for errors.

I found it to be a challenging but useful process, a number of times during development automated tests were able to flag up issues much earlier than I would have noticed them with manual testing alone. With large, complex project with inter-woven features and dependencies I can completely see the benefit of this approach and I look forward to expanding my knowledge and delving more in to the world of automated testing in the future.

### Automated testing coverage and results

**Automated Testing - Test Results**

<img src="">

## Validation


### HTML Validation

I ran the code for all the pages through the [W3C HTML Validator](https://validator.w3.org/nu/) using the textarea input by generating the source code from the deployed site (right click and select 'View Page Source' in Chrome) and pasting it in to allow me to check all pages whether requiring log in or not. All code passed the validation tests. Results below.


<details><summary>HTML Validation Results</summary>
<img src="">
</details>

#### Issues resolved during validation:

- Django forms renders its form inputs as a table and there were multiple errors about stray `<tr>` tags in the code, which I couldn't access as the form was added by using just `{{form}}`. I got around this based on a [post](https://code-institute-room.slack.com/archives/C7HS3U3AP/p1548669436265400) I found on the CI Slack Channel suggesting rendering them as `<p>` elements instead using `{{form.as_p}}` and amending the styling as necessary.

- Image selection in the custom_clearable_file_input on the product form was throwing an error as it had 2 ID attributes, one that I had set which was used in the JavaScript to display the filename and another that was added by the `{% include "django/forms/widgets/attrs.html" %}` tag. I solved this problem by changing the JavaScript to get an element using a class name rather than ID and removing the class.

### CSS Validation

I ran the CSS code through the [W3C CSS Validator](LINK). All code passed the validation tests. Results below.


<details><summary>CSS Validation Results</summary>

<img src="">

</details>

#### CSS Warnings

There were some warnings thrown up by the CSS Validator.

- Vendor extension warnings: refer to browser specific CSS classes such as `-webkit-transition`. These classes are best practice to make sure that certain CSS elements perform correctly in different browsers and so I have disregarded these warnings.
- Imported style sheets: This refers to Google's font import, again this is a standard way to import fonts directly in to the CSS.
- CSS Variables are not checked: This refers to the :root directory of colours and is just a warning that it cannot check these. They all performed as expected during testing and so I'm happy with this CSS code.

### JavaScript Linting

I ran the JavaScript code through [JSHint](https://jshint.com/). For full results see the dropdown below.

<details><summary>JavaScript Results</summary>
<img src="">
</details>

### Python Linting

I ran the app.py code through [https://pep8ci.herokuapp.com/](https://pep8ci.herokuapp.com/) to check the Syntax. GitPod also has a built in Python Linter which was used throughout the development process (see below). All code passed the validation tests. For full results see the dropdowns below.

<details><summary>Python Results Table</summary></details>

#### Additional Linting Using Flake8 in GitPod

I used the inbuilt linting in GitPod (Flake8) to check my code and keep it as clean as possible. All code was cleaned up, errors dealt with and any suggested changes made apart from the following issues which I was unable to solve:

- **checkout/apps.py - checkout.signals is imported but unused** - signals is being passed in and used elsewhere so can be disregarded
- **checkout/webhooks.py - local variable e is assigned to but never used** - have investigated this and it appears to be an industry standard way of assigning this particular error checking. I also passed this same code through the [CI Python Linter](https://pep8ci.herokuapp.com/) and it didn't raise an issue so I am disregarding this.
- remaining linting errors are in files that are automatically created by Django such as migration files & vscode/arctictern.py

- - -
[Go to Top](#posh-portables---e-commerce-site---testing)
- - -

### Performance

I ran the site through Google Chrome Dev Tools' Lighthouse to check on its performance scores. All pages passed the validation tests. For full results see the dropdowns below.

<details><summary>Performance Results Table</summary>


| **Feature**                             | **Expected Outcome**                          | **Test Performed**                | **Change / Final Result**               | **Pass / Fail** |
|-----------------------------------------|-----------------------------------------------|-----------------------------------|-----------------------------------------|-----------------|
| **HOME**                                | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | Tinified Hero image • All scores 90+    | PASS            |
| **PRODUCTS**                            | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | All scores 90+                          | PASS            |
| **PRODUCT DETAILS**                     | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | All scores 90+                          | PASS            |
| **CREATE PRODUCT**                      | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | All scores 90+                          | PASS            |
| **UPDATE PRODUCT**                      | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | All scores 90+                          | PASS            |
| **CREATE REVIEW**                       | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | All scores 90+                          | PASS            |
| **UPDATE REVIEW**                       | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | All scores 90+                          | PASS            |
| **SHOPPING CART**                       | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | All scores 90+                          | PASS            |
| **CHECKOUT**                            | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | All scores 90+                          | PASS            |
| **CHECKOUT SUCCESS**                    | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | All scores 90+                          | PASS            |
| **PROFILE**                             | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | All scores 90+                          | PASS            |
| **FAQS**                                | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | All scores 90+                          | PASS            |
| **CREATE FAQ**                          | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | All scores 90+                          | PASS            |
| **UPDATE FAQ**                          | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | All scores 90+                          | PASS            |
| **SIGN IN (login)**                     | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | Added meta description • All scores 90+ | PASS            |
| **REGISTER (signup)**                   | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | Added meta description • All scores 90+ | PASS            |
| **MANAGE EMAIL (email)**                | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | Added meta description • All scores 90+ | PASS            |
| **CHANGE PASSWORD (password/change)**   | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | Added meta description • All scores 90+ | PASS            |
| **FORGOT PASSWORD (password/reset)**    | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | Added meta description • All scores 90+ | PASS            |
| **SIGN OUT (logout)**                   | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | Added meta description • All scores 90+ | PASS            |
| **VERFICATION SENT (confirm-email)**    | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | Added meta description • All scores 90+ | PASS            |
| **CONFIRM EMAIL (confirm-email/(key))** | All scores 90+ with no errors or major issues | Chrome Lighthouse Report for page | Added meta description • All scores 90+ | PASS            |


</details>

<details><summary>Performance Results Images</summary>

<details><summary>HOME</summary>
<img src="m">
</details>

<details><summary>PRODUCTS</summary>
<img src="g">
</details>

<details><summary>PRODUCT DETAILS</summary>
<img src="">
</details>

<details><summary>CREATE PRODUCT</summary>
<img src="">
</details>

<details><summary>UPDATE PRODUCT</summary>
<img src="">
</details>

<details><summary>CREATE REVIEW</summary>
<img src="">
</details>

<details><summary>UPDATE REVIEW</summary>
<img src="">
</details>

<details><summary>SHOPPING CART</summary>
<img src="">
</details>

<details><summary>CHECKOUT</summary>
<img src="media/docs/docs_val_perf_9.jpg">
</details>

<details><summary>CHECKOUT SUCCESS</summary>
<img src="">
</details>

<details><summary>PROFILE</summary>
<img src="">
</details>

<details><summary>FAQS</summary>
<img src="">
</details>

<details><summary>CREATE FAQ</summary>
<img src="media/docs/docs_val_perf_13.jpg">
</details>

<details><summary>UPDATE FAQ</summary>
<img src="media/docs/docs_val_perf_14.jpg">
</details>

<details><summary>SIGN IN (AllAuth Name - login)</summary>
<img src="media/docs/docs_val_perf_17.jpg">
</details>

<details><summary>REGISTER (AllAuth Name - signup)</summary>
<img src="media/docs/docs_val_perf_18.jpg">
</details>

<details><summary>MANAGE EMAIL (AllAuth name - email)</summary>
<img src="media/docs/docs_val_perf_19.jpg">
</details>

<details><summary>CHANGE PASSWORD (AllAuth name - password/change)</summary>
<img src="media/docs/docs_val_perf_20.jpg">
</details>

<details><summary>FORGOT PASSWORD (AllAuth name - password/reset)</summary>
<img src="media/docs/docs_val_perf_21.jpg">
</details>

<details><summary>SIGN OUT (AllAuth name - logout)</summary>
<img src="media/docs/docs_val_perf_22.jpg">
</details>

<details><summary>VERFICATION SENT (AllAuth name - confirm-email)</summary>
<img src="media/docs/docs_val_perf_23.jpg">
</details>

<details><summary>CONFIRM EMAIL (AllAuth name - confirm-email/(key))</summary>
<img src="media/docs/docs_val_perf_2.jpg">
</details>

</details>

#### Issues resolved during performance validation:

- Console Error about one of the Favicon icons being missing returning a 404, the site appeared to be looking in the wrong location for the file. I fixed this by explicitly naming all the icons in the `<head>` element and removing the web manifest.

- - -
[Go to Top](#posh-portables---e-commerce-site---testing)
- - -

## Feature Testing

The whole site and all its features were tested manually thoroughly throughout the development process and at the end of development. This testing covered content, style, interactive feature functionality as well as making sure all backend processes worked as expected including testing of all CRUD functionality and routing. This was in addition to the automated testing described [above](#automated-testing-using-test-driven-development). The results of the final full manual test are below.

### **Responsiveness / Devices**

The manual testing was done on the following devices
* Apple Macbook Pro 16inch
* Samsung Galaxy S10
* Apple Mac Pro 13-Inch 
* OnePlus Nord 2023
* Apple iPhone SE 2020
* Apple iPhone SE 2022
* Google Chrome Developer Tools - simulator for all different device options as well as using the adjustable sizing options

### **Browser Compatibility**

The manual testing was done on the following browsers
* Google Chrome
* Mozilla Firefox
* Apple Safari

### **Feature Testing Results**


<details><summary>All Pages</summary>

| **Testing**                           | **Expected Outcome**                                                                                                         | **Test Performed**                                                                                                              | **Pass / Fail** |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|-----------------|
| **Site width**                        | Max width 1400px with grey background                                                                                        | Expand window & use dev tools to check size                                                                                                               | PASS            |
| **Favicon**                           | Appears in browser tab                                                                                                       | Check favicon appears in multiple browsers                                                                                                        | PASS            |
| **Navbar - contents**                 | Contains logo and nav links. All links lead to correct pages.                                                                | Check nav contents. Click on all links.                                                                                                                   | PASS            |
| **Navbar - accounts dropdown**        | Account dropdown is clickable and displays nav links                                                                         | Click on dropdown menu & dropdown links                                                                                                           | PASS            |
| **Navbar - products dropdown**        | Products dropdown displays correct working links                                                                             | Click on products dropdown menu & dropdown links - check products are filtered correctly                                                            | PASS            |
| **Navbar - sticky**                   | Stays at the top of the browser page                                                                                         | Scroll to bottom of page                                                                                                                     | PASS            |
| **Navbar - logo**                     | Clickable and links to homepage                                                                                              | Click on logo                                                                                                                     | PASS            |
| **Navbar - hover**                    | Hover effect with transition                                                                                                 | Hover over nav links                                                                                                                    | PASS            |
| **Navbar - responsive**               | On smaller devices nav links change to a burger menu which displays all links and submenus. Logo changes on smaller screens. | Use dev tools to simulate smaller screen & check on mobile devices. Click on burger menu & all links                                               | PASS            |
| **Navbar - logged out**               | "Visible links on Accounts Dropdown: Register, Sign In"                                                                      | Sign out of site & check nav bar                                                                                                                      | PASS            |
| **Navbar - logged in (non-admin)**    | "Visible links on Accounts Dropdown: My Profile, Sign Out"                                                                   | Sign in to site as non-admin & check nav bar                                                                                                            | PASS            |
| **Navbar - logged in (admin)**        | "Visible links on Accounts Dropdown: Site Management, My Profile, Sign Out"                                                  | Sign in to site as admin & check nav bar                                                                                                                  | PASS            |
| **Navbar - cart (empty)**             | Bag icon is yellow with £0 showing if bag is empty                                                                           | Check nav bar with empty bag                                                                                                                      | PASS            |
| **Navbar - bag (contents)**           | Bag icon is white with correct total showing                                                                                 | Add products to bag and check nav bar                                                                                                                  | PASS            |
| **Navbar - search box (no contents)** | Search term submits and links to products page. Message appears (no search term)                                             | Click on search icon with no contents in search box                                                                                                   | PASS            |
| **Navbar - search box (contents)**    | Search term submits and links to products page with correct results. Search term appears on page.                            | Add search term to search box and click on search icon. Check results and page contents.                                                               | PASS            |
| **Navbar - search box dropdown**      | On Medium & smaller screens clicking the search icon triggers the dropdown search bar.                                       | "Using dev tools simulate a medium or small screen, click on search icon. Add contents to search bar and click search."                              | PASS            |
| **Delivery Banner**                   | Delivery banner shows correct text and amount                                                                                | Check banner contents                                                                                                                 | PASS            |
| **Footer - contents**                 | "Contains Social links, more info links, about us text, disclaimer & personal links"                                         | Check footer                                                                                                                   | PASS            |
| **Footer - responsive**               | Contents stack on smaller devices & margins adjust                                                                           | Use dev tools to simulate different screen sizes & check on smaller devices                                                                        | PASS            |
| **Footer - Hover on links**           | Hover effect with transition                                                                                                 | Hover over links                                                                                                                    | PASS            |
| **Footer - social**                   | Open correct pages in separate tab                                                                                           | Click on links                                                                                                                    | PASS            |
| **Footer - More Info links**          | Link to correct pages                                                                                                        | Click on links                                                                                                                    | PASS            |

</details>

<details><summary>Home</summary>

| **Testing**                       | **Expected Outcome**                                                   | **Test Performed**                                                                                      | **Pass / Fail** |
|-----------------------------------|------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|-----------------|
| **Page Contents**                 | All page contents appear and are fully responsive                      | Check page contents on different devices and in Chrome Dev Tools                                        | PASS            |
| **Page Links**                    | All page links lead to correct location                                | Click on all links & check page contents                                                                | PASS            |
| **Product Category Filter Links** | All category links lead to products page with correct products visible | Click on category links & categories in product cards & check products page contents.                   | PASS            |
| **Hover effects**                 | Buttons and links have hover effect with smooth transition             | Hover over buttons & links                                                                              | PASS            |
| **Authentication Tests**          | Page is visible to all users                                           | "Navigate to page as an unauthenticated, authenticatied & superuser"                                    | PASS            |
| **Featured Products**             | Only featured products appear                                          | "Go to admin panel, change ‘is_featured’ boolean value on a product, check if product appears on page." | PASS            |

</details>

<details><summary>Products</summary>

| **Testing**                                | **Expected Outcome**                                                   | **Test Performed**                                                            | **Pass / Fail** |
|--------------------------------------------|------------------------------------------------------------------------|-------------------------------------------------------------------------------|-----------------|
| **Page Contents**                          | All page contents appear and are fully responsive                      | Check page contents on different devices and in Chrome Dev Tools              | PASS            |
| **Page Links**                             | All page links lead to correct location                                | Click on all links & check page contents                                      | PASS            |
| **Authentication Tests**                   | Page is visible to all users                                           | "Navigate to page as an unauthenticated, authenticatied & superuser"          | PASS            |
| **Product Count**                          | Product Count matches number of products                               | Check product count with filtered & unfiltered product selection              | PASS            |
| **Product Category Filters**               | All category links lead to products page with correct products visible | Click on categories in product cards & check product cards and category name. | PASS            |
| **Filtered Products - All Products Reset** | All Products button removes all filters and shows all products         | Filter products by category. Click on ‘All Products’                          | PASS            |
| **Sorting**                                | Sort box sets the correct sort and direction of the product cards      | Select all sorting options and check product cards                            | PASS            |
| **Product Cards**                          | Clicking on card image links to correct product page                   | Click on product card                                                         | PASS            |
| **Product Cards**                          | Product cards contain correct information for products                 | Check card contents against products in database                              | PASS            |

</details>

<details><summary>Product Details</summary>

| **Testing**                                    | **Expected Outcome**                                                                                | **Test Performed**                                                                                                             | **Pass / Fail** |
|------------------------------------------------|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|-----------------|
| **Page Contents**                              | All page contents appear and are fully responsive                                                   | Check page contents on different devices and in Chrome Dev Tools                                                               | PASS            |
| **Page Links**                                 | All page links lead to correct location                                                             | Click on all links & check page contents                                                                                       | PASS            |
| **Hover effects**                              | Buttons and links have hover effect with smooth transition                                          | Hover over buttons & links                                                                                                     | PASS            |
| **Product Category Filter Links**              | Category link lead to products page with correct products visible                                   | Click on category link & check products page contents.                                                                         | PASS            |
| **Authentication Tests**                       | Page is visible to all users                                                                        | "Navigate to page as an unauthenticated, authenticatied & superuser"                                                           | PASS            |
| **Authentication Tests - Edit/Delete Product** | Edit / Delete buttons only visible to superusers                                                    | "Navigate to page as an unauthenticated, authenticatied & superuser"                                                           | PASS            |
| **Authentication Tests - Edit Review**         | Edit buttons only visible to creator                                                                | "Navigate to page as an unauthenticated, authenticatied & superuser"                                                           | PASS            |
| **Authentication Tests - Delete Review**       | Delete buttons only visible to creator & superusers                                                 | "Navigate to page as an unauthenticated, authenticatied & superuser"                                                           | PASS            |
| **Non-existent product**                       | 404 page displays if product doesn’t exist                                                          | Navigate to product details for a product id that doesn’t exist on database.                                                   | PASS            |
| **Discontinued product**                       | Error message shows if product is discontinued and user redirected to ‘products’ page               | "Set a product to ‘discontinued’, attempt to navigate to that product using direct URL input."                                 | PASS            |
| **Quantity Input**                             | Quantity Buttons increment/decrement quantity. Quantity can be typed in.                            | Click on quantity buttons. Type in to quantity box.                                                                            | PASS            |
| **Quantity Input**                             | Buttons are disabled when lower/upper limit is reached                                              | Input 1 as quantity & check decrement button. Input 99 as quantity & check increment button                                    | PASS            |
| **Add to Bag Button**                          | Adds the correct item and quantity to the bag. Shows a message & bag summary with correct contents. | Input quantity and click on ‘add to bag’. Add another of the same item. Add a different item. Check bag matches at each stage. | PASS            |
| **Bag Summary**                                | View Bag link leads to bag page & contents match summary.                                           | Click on view bag and compare contents                                                                                         | PASS            |
| **Product Contents**                           | "Product name, description, image & price are correct."                                             | Navigate to page and check product details.                                                                                    | PASS            |
| **Product Image**                              | Clicking on image opens full size image in a new tab.                                               | Navigate to page and click on product image.                                                                                   | PASS            |
| **Product Rating**                             | Product rating is the average of the review ratings.                                                | Compare product rating to ratings on reviews                                                                                   | PASS            |
| **Product Reviews**                            | Reviews are for correct product and sorted by rating (high-low) then date                           | Check random selection of reviews against database entries and check rating/date                                               | PASS            |

</details>

<details><summary>Add / Edit / Delete Products</summary>

| **Testing**                                               | **Expected Outcome**                                                                                               | **Test Performed**                                                                                                                                                                            | **Pass / Fail** |
|-----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| **Page Contents**                                         | All page contents appear and are fully responsive                                                                  | Check page contents on different devices and in Chrome Dev Tools                                                                                                                              | PASS            |
| **Page Links**                                            | All page links lead to correct location                                                                            | Click on all links & check page contents                                                                                                                                                      | PASS            |
| **Authentication Tests - Add Product - Logged Out**       | Redirects to login for unauthenticated user with error message & redirects back after sign in.                     | Log out of site. Navigate to add product direct via URL                                                                                                                                       | PASS            |
| **Authentication Tests - Add Product - Non-superuser**    | Redirects to home with error message if user is not superuser                                                      | "Log in as non-superuser, navigate to add product direct via URL"                                                                                                                             | PASS            |
| **Authentication Tests - Add Product - Superuser**        | Opens Add Product Form                                                                                             | "Log in as superuser, navigate to add product page"                                                                                                                                           | PASS            |
| **Add product form**                                      | Has correct fields & all are required (apart from image)                                                           | Navigate to add product form. Attempt to submit form with empty inputs.                                                                                                                       | PASS            |
| **Add product form**                                      | Form can be submitted without an image                                                                             | Submit form without selecting an image                                                                                                                                                        | PASS            |
| **Add product form - submission**                         | "On submission success message displays, product is created in database with correct information"                  | "Submit form, check message and check database (and site if product is not discontinued)"                                                                                                     | PASS            |
| **Authentication Tests - Edit Product - Logged Out**      | Redirects to login for unauthenticated user with error message & redirects back after sign in.                     | Log out of site. Navigate to edit product direct via URL                                                                                                                                      | PASS            |
| **Authentication Tests - Edit Product - Non-superuser**   | Redirects to home with error message if user is not superuser                                                      | "Log in as non-superuser, navigate to edit product direct via URL"                                                                                                                            | PASS            |
| **Authentication Tests - Edit Product - Superuser**       | Opens Edit Product Form                                                                                            | "Log in as superuser, navigate to edit product page"                                                                                                                                          | PASS            |
| **Edit Product Message**                                  | Message displays on page load with product name                                                                    | Click on ‘edit’ on a product and check message contents.                                                                                                                                      | PASS            |
| **Edit Product - Non existent Product**                   | 404 page displays if product doesn’t exist                                                                         | Navigate to edit product for a product id that doesn’t exist on database.                                                                                                                     | PASS            |
| **Edit product form**                                     | Form contains correct information for product                                                                      | Click on edit product and check form contents                                                                                                                                                 | PASS            |
| **Edit product form**                                     | Has correct fields & all are required (apart from image)                                                           | Navigate to add product form. Attempt to submit form with empty inputs.                                                                                                                       | PASS            |
| **Edit product form**                                     | Form can be submitted without an image                                                                             | Remove image if required. Submit form without selecting an image                                                                                                                              | PASS            |
| **Edit product form - submission**                        | "On submission success message displays, product is updated in database with correct information"                  | "Submit form, check message and check database (and site if product is not discontinued)"                                                                                                     | PASS            |
| **Authentication Tests - Delete Product - Logged Out**    | Redirects to login for unauthenticated user with error message & redirects back after sign in.                     | Log out of site. Navigate to delete product direct via URL                                                                                                                                    | PASS            |
| **Authentication Tests - Delete Product - Non-superuser** | Redirects to home page if user is not superuser with error message                                                 | "Log in as non-superuser, navigate to delete product direct via URL."                                                                                                                         | PASS            |
| **Authentication Tests - Delete Product - superuser**     | Superuser is able to delete or discontinue product                                                                 | Sign in to site. Navigate to delete product.                                                                                                                                                  | PASS            |
| **Delete Product - Non existent Product**                 | 404 page displays if product doesn’t exist                                                                         | Navigate to delete product for a product id that doesn’t exist on database.                                                                                                                   | PASS            |
| **Delete Product Modal**                                  | Modal appears when deleting a product to confirm deletion                                                          | Click on delete product                                                                                                                                                                       | PASS            |
| **Delete Product Modal**                                  | Clicking on ‘close’  or cross icon closes the modal and doesn’t delete product                                     | "Click on delete product, click on close button, check product details page still exists, repeat with cross icon."                                                                            | PASS            |
| **Delete Product Modal - non-protected product**          | Clicking on ‘delete’ deletes product from site & displays success message                                          | "Click on delete product, then ‘delete’ in modal. Check message. Check product has gone from site and database."                                                                              | PASS            |
| **Delete Product Modal - protected product**              | Clicking on delete for a product that appears on an previous order brings up modal with option to ‘remove’ product | Attempt to delete a product which appears as a line item on an order. Check modal contents                                                                                                    | PASS            |
| **Delete Product Modal - protected product**              | Clicking ‘remove’ sets the ‘discontinued’ field to True & removes product from site                                | Attempt to delete a product which appears as a line item on an order. Click on remove & check product has gone from site. Check product exists on database with correct ‘discontinued’ value. | PASS            |
| **Products General - Missing Image**                      | Product without an image displays no-image alternative                                                             | Log in as a superused. Add a new product without an image. Check product on all relevant pages.                                                                                               | PASS            |

</details>

<details><summary>Bag</summary>

| **Testing**                    | **Expected Outcome**                                                                                              | **Test Performed**                                                                          | **Pass / Fail** |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|-----------------|
| **Page Contents**              | All page contents appear and are fully responsive                                                                 | Check page contents on different devices and in Chrome Dev Tools                            | PASS            |
| **Page Links**                 | All page links lead to correct location                                                                           | Click on all links & check page contents                                                    | PASS            |
| **Hover effects**              | Buttons and links have hover effect with smooth transition                                                        | Hover over buttons & links                                                                  | PASS            |
| **Authentication Tests (bag)** | Page is visible to all users                                                                                      | "Navigate to page as an unauthenticated, authenticatied & superuser"                        | PASS            |
| **Bag summary message**        | "Appears when adding, removing or updating a product in the bag. Totals match bag contents and exclude delivery." | "Add, remove & update an item in the bag, check message contents."                          | PASS            |
| **Bag summary message**        | “Spend £— more” message appears when total is under free delivery threshold in summary.                           | "Add items under £100, check message contents."                                             | PASS            |
| **Bag Contents**               | Match items added to bag                                                                                          | "Add items to bag, navigate to bag page & check contents"                                   | PASS            |
| **Product Image Link**         | Clicking on product image leads to the product detail page.                                                       | "Add product to bag, navigate to bag page, click on image."                                 | PASS            |
| **Quantity Input**             | Quantity Buttons increment/decrement quantity for correct product. Quantity can be typed in.                      | Click on quantity buttons. Type in to quantity box. Click on ‘update’.                      | PASS            |
| **Quantity Input**             | Buttons are disabled when lower/upper limit is reached                                                            | Input 1 as quantity & check decrement button. Input 99 as quantity & check increment button | PASS            |
| **Remove Item**                | Removes item from bag & updates bag totals.                                                                       | Click on ‘remove’ for a product. Check bag contents & totals.                               | PASS            |
| **Bag totals**                 | Bag total matches bag contents. Grand total = bag total + Delivery Charge.                                        | Add contents to bag & check totals add up.                                                  | PASS            |
| **Delivery Charge**            | Is 10% of total for qualifying products                                                                           | Add items to bag which qualify for delivery charge. Check totals.                           | PASS            |
| **Delivery Charge**            | Items which are subject to delivery charge aren’t included in delivery calculations                               | "Add item to bag with no delivery charge, check delivery total."                            | PASS            |
| **Free delivery threshold**    | “Spend £— more” message appears when total is under free delivery threshold on bag page.                          | "Add items under £100 and navigate to the bag page, check message & contents."              | PASS            |
| **Checkout Link**              | Checkout button links to checkout page and order summary matches bag contents.                                    | "Add items to bag, navigate to bag page, click on ‘checkout’"                               | PASS            |

</details>