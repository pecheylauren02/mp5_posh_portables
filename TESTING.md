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

<details><summary>Python Results Table</summary>

#### Additional Linting Using Flake8 in GitPod

I used the inbuilt linting in GitPod (Flake8) to check my code and keep it as clean as possible. All code was cleaned up, errors dealt with and any suggested changes made apart from the following issues which I was unable to solve:

- **checkout/apps.py - checkout.signals is imported but unused** - signals is being passed in and used elsewhere so can be disregarded
- **checkout/webhooks.py - local variable e is assigned to but never used** - have investigated this and it appears to be an industry standard way of assigning this particular error checking. I also passed this same code through the [CI Python Linter](https://pep8ci.herokuapp.com/) and it didn't raise an issue so I am disregarding this.
- remaining linting errors are in files that are automatically created by Django such as migration files & vscode/arctictern.py

---

