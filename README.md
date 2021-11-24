<style>

@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@200;300;400;500;600;700&display=swap');

body{
    background-color: black;
    font-family: Oswald;
    font-weight: 400;
    letter-spacing: 1px;
    line-spacing: 
}

p {
  line-height: 32px;
  margin-bottom: 20px;
  }

</style>

<center><img src="static/images/logo.png" alt="Foodie Logo" width="50%"></center>

----

    This is the README file for my Code Institute MS3 project site, Foodie - The Recipe Sharing Site

    This project is the 3rd project as part of the Code Institute Full Stack Development course. The projects are set in order to demonstrate my understanding of what we have learnt during the previous units.
    The task set for this project is to demonstrate the ability to create a fully responsive web application that allows users to interact and manipulate with data stored in a database.

<br>

<center><img src="readme-images/website-mockup.png" alt="Website Mockup" width="100%">

[CLICK HERE TO VISIT THE LIVE SITE](https://ts-foodie.herokuapp.com/) </center>

----
<br>

# Table Of Content:

- <a href="#project_goals">Project Goals</a>
- <a href="#ux">User Experience (UX)</a>
    - <a href="#ux-user_stories">User Stories</a>
    - <a href="#ux-design">Design</a>
        - <a href="#ux-design-color">Color</a>
        - <a href="#ux-design-color">Typography</a>
        - <a href="#ux-design-color">Images</a>
        - <a href="#ux-design-structure">Structure & Mockup Designs</a></a>
        - <a href="#ux-design-amendments">Amendments To Mockup Designs During Development</a></a>
- <a href="#features">Features</a>
    - <a href="#features-current">Current Features</a>
    - <a href="#features-future">Possible Future Features</a>
- <a href="#database">Database</a>
- <a href="#key-components">Key Components</a>
    - <a href="#key-components-languages">Languages</a>
    - <a href="#key-components-frameworks">Frameworks & Libraries</a>
    - <a href="#key-components-others">Others</a>
- <a href="#testing">Testing</a>
    - <a href="#testing-problems-during-development">Problems During Development</a>
    - <a href="#testing-bugs">Known Bugs</a>
- <a href="#deployment">Deployment</a>
    - <a href="#deployment-github">Deployment Through GitHub Pages</a>
    - <a href="#deployment-forking">Forking</a>
    - <a href="#deployment-cloning">Cloning Project</a>
    - <a href="deployment-admin">Administrator Access Credentials</a>
- <a href="#credits">Credits</a>
    - <a href="#credits-content">Content</a>
    - <a href="#credits-media">Media</a>
    - <a href="#credits-code">Code</a>
    - <a href="#credits-acknowledgments">Acknowledgements</a>


----

# <span id="#project_goals">Project Goals</span>

*   Design, develop and implement a full stack web application using HTML, CSS, JavaScript, Python, Flask and MongoDB
*   Identify and apply necessary security features


# <span id="#ux">User Experience (UX)</span>

    This section is designed to generate possible scenarios of the typical end user that would use this website. 
    This will help ensure end user requirements are designed into the website.

    To create a web application that offered a good experience to the user, I found that a minimal and simplistic style would be the best approach. 
    Not only does this keep the site easy to use, it also makes sure that the users aren't over powered with all the information the database may store/display.   

    A key priority was to try to make the journey from entering the site to displaying a recipe as quickly and clean as possible.


## <span id="#ux-user_stories"><b>User Stories</b></span>

* ### <b>User Experience</b>

    - When I visit the site, I want to know that I have landed on the correct site that I intended to visit.

    - I need to be able to navigate to the key elements of the site quickly.

    - The website should load correctly on any device.

    - The website should load quickly and only load the necessary files required to display the key elements of the site first to improve load times.

    - Site visitors should be able to find social links to engage and share recipes to friends through their social media connections.


* ### <b>First Time Visitor Goals</b>

    - First Time Visitors, should be able to understand the purpose and reason for the site.

    - First Time Visitors, should be able to easily find the navigation links.

    - First Time Visitors, should be able to interact with the site upon landing on the site.

    - First time users should be able to view the recipes on the site without having to log in or register for an account.

    - First time users are likely to be un-registered users and must have restricted access to certain areas of the site.

    - First time users are able to navigate the site without registering. However in order to submit a recipe to the site, users must register and therefore the user must be able to locate the Register link on the hompeage easily and quickly.

* ### <b>Returning Visitor Goals</b>

    - A returning visitor would typically be a user that has already registered with the website, therefore the user should be able to locate the log in link easily and quickly on the homepage.

    - A returning visitor should be able to make changes to any recipes they have uploaded onto the site, but must not be able to edit or remove entries entered by the site admin or other users.

* ### <b>Website Administrator Goals</b>

    - The website administrator must be able to find the administrator tools when logged into the site.

    - The website administrator must be able to add and remove administrator to the administrator access database.

    - The website administrator must not be able to delete the main administrator account from the database.

    - The website administrator must be able to create, remove, update and delete recipe categories.

    - The website administrators must be the only users to have access to the restricted websites and non-administrators must not be able to access restricted sites by direct URL inputs.

## <span id="#ux-design"><b>Design</b></span>

* ### <span id="#ux-design-color"><b>Color</b></span>

    When choosing the most suitable color scheme for the site, I decided to list the main points of what I wanted to try to create from the design.

    Here are the key points to consider when choosing the colors:

    * Eye Catching
    * Comfertable
    * Color Compatibility

    I chose to develop both the logo and the main site theme at the same time to ensure that they could work well together. 
    The colors were going to be an important part of the design in order to create a brand that could be applied throughout the company should it be required in the future.

    To choose a compatible color scheme, I decided to use [Adobe Color](https://color.adobe.com/) to find colors that would work well together. 
    I began by choosing a base color that I thought would work well for the brand, then entered the color codes into the site and it came up with other colors that would work well in combination with the colors I had already entered. When [Adobe Color](https://color.adobe.com/) displayed the result, it stated 'No conflicts found. Swatches are color blind safe.'

    <img src="readme-images/color.jpeg" alt="Color Palette" width="50%">

    After finding the colors I felt were most suitable I implemented them into the site, in later stages of development I began testing the site's compatibility using [Adobe Color](https://developers.google.com/web/tools/lighthouse) and it was brought to my attention that the way I was using the colors was not meeting lightroom's accessibility criterias due to contrasting colors. I have explained further in my testing section on the steps I had to take to overcome this issue.

* ### <span id="ux-design-typography"><b>Typography</b></span>


    When choosing which font to use as part of my design, I felt it was important for it to be easy to read but have similar feel as a font you would choose for a restraunt menu. I wanted the font to be appropriate so that I could use it for the logo text and also the main site text. This would then help maintain a nice continuity within the design and also help create the 'Foodie' brand I was aiming for.

    I have used Google to source the fonts and these are loaded within the head of the page.

    The main font is [Lobster](https://fonts.google.com/specimen/Lobster?query=lobster)

    This is the font I used for fancy headings and labelling.

    The secondary font is [Oswald](https://fonts.google.com/specimen/Oswald?query=oswald)

    This font is used as a uniform font for all key information, keeping it easy to read.

* ### <span id="ux-design-images"><b>Images</b></span>

    There is very little base images on the site, but does display a large amount of images based on the content uploads of the end user.
    The images for each of the recipes posted to the site are outsourced and the user must provided a url to the image of their recipe when uploading it to the site.
    These uploads then form the design of all the pages.

* ### <span id="ux-design-structure"><b>Structure & Mockup Designs</b></span>

    <h3> Homepage </h3>
    <img src="readme-images/wireframe-recipe-book.png" alt="Wireframe image for the Homepage" width="100%">

    <h3> Registration Page </h3>
    <img src="readme-images/wireframe-register.png" alt="Wireframe image for the Registration page" width="100%">

    <h3> Login Page </h3>
    <img src="readme-images/wireframe-login.png" alt="Wireframe image for the Login page" width="100%">

    <h3> Add Recipe Page</h3>
    <img src="readme-images/wireframe-add-recipe.png" alt="Wireframe image for the add recipe page" width="100%">

    <h3> Edit Recipe Page</h3>
    <img src="readme-images/wireframe-edit-recipe.png" alt="Wireframe image for the edit recipe page" width="100%">

    <h3> Manage Categories Page (Administrators Only) </h3>
    <img src="readme-images/wireframe-manage-categories.png" alt="Wireframe image for the manage categories page." width="100%">

* ### <span id="ux-design-amendments"><b>Amendments To Mockup Designs During Development</b></span>

    During the development there were very minor changes to the original design I created. I had originally planned to have a landing page to welcome users to the site with a button that they could click to open the recipe book. However when I built this, it felt that having this feature increased the time it took for the end user to reach the purpose of the site. I made the decision to remove the opening page and direct users straight into the recipe book.

    I also felt that the site needed an additional feature for Administrators to be able to assign other administrators. As the number of users using the site increases, it would be useful for the Administrator to be able to share any administrative tasks with other users. I therefore chose to implement a page for anyone with administrative access to add/remove other administrators.

    <img src="readme-images/wireframe-manage-administrators.png" alt="Wireframe image for the manage administrators page." width="100%">

## <span id="features"><b>Features</b></span>

* ### <span id="features-current"><b>Current Features</b></span>

    * #### <b>User Access Structure</b>

        In order to manage the recipe uploads, the site needed to be able to restrict certain users from being able to carry out certain tasks on the site.
        Tasks such as:
            - A user <b>MUST</b> be registered and logged in to the site to upload a recipe.
            - A user <b>MUST</b> be logged in and the owner of the uploaded recipe to edit or remove the recipe.
            - The necessary user access requirements <b>MUST</b> be checked upon landing on every restricted site, even if the user enters the direct URL.

        In order to achieve this, all the restricted access sites have functions at the top of the site that will check if the user meets the necessary requirements. If they do, the content will load. If not, an error message will be displayed.

    * #### <b>Navigation Menu Based On User Level</b>

        <img src="readme-images/wireframe-user-access.png" alt="Wireframe image for the navigation bars based on user access." width="100%">

        There are additional items placed within the navigation menu that are only displayed depending on the user's log in state.
        I felt it was important that a user that is not logged in, shouldn't need to see the 'new recipe' button. The same would also apply for a user that is logged in that shouldn't see all of the navigation options that an administrator would see.

        To overcome these issues, there are if statements within the navigation menu code that checks the state of the user and displays the relevant options based on the result.

    * #### <b>Dynamically Created Navigation Menu Dropdown</b>

        Administrators of the site are able to edit the different recipe categories.
        These categories are then listed as options within a dropdown in the navigation menu so that the site user can see a all the recipes that are uploaded to the site based on the category they choose.

        When an administrator adds/removes a category from the site, the navigation item 'categories' will automatically update to show the changes made by the administrator.

    * #### <b>Read Only Access To Recipes For Unregistered Users</b>

        It was important that first time visitors to the site were able to see what the site was all about. The site will display all of the uploaded content to the un-registered user, however the un-registered user will not have access to add, edit, remove recipes but does have access to login or register for an account at anytime.

    * #### <b>User Account</b>

        In order to manage how the recipe's were managed, the site has a user account system. Users can create an account with the website that will allow them to log in and extend the functionality of the site.

    * #### <b>User's Recipe Collection & Management Page</b>

        I felt it was important for a user to be able to manage their uploads in a quick and easy way and to do this, I created a user recipe page.
        When a user succesfully logs in, they will be re-directed to a page that displays all of the recipe's they have uploaded.
        From here they have the option to open, edit or delete any of the displayed recipes.
        They can also visit this page by clicking the {{username}}'s Recipes link within the navigation bar. This link will automatically update to display the session user's username for a more personal interaction with the site.

    * #### <b>Administrator Account</b>

        To manage the site, I created an administrator account. This account provides the user with all priviledges to manage the website.

        The administrator is able to:
            - create or remove additional recipe categories
            - create or remove additional administrators to the site

* ### <span id="features-future"><b>Possible Future Features</b></span>

    * #### Video Demonstrations / Live Cooking Sessions
        Now that more and more users are using the internet to learn, it would be great to offer the site users some live and pre-recorded cooking events. Users will be able to watch a live or recorded video of top chefs preparing some of the recipes from the site. This could be a feature that coulc become part of a paid subscription, this then earing revenue to the site.

    * #### Cookery Equipment Store
        The internet is quickly becoming a tool to promote and advertise products to their customers. By offering a cookery equipment store as part of the site, it is likely that the audience of the site already has a large interest in cooking and therefore the target audience for selling cooking products is already at the site.

        Recipe's could include links to equipment best used to cook the recipe, offering the user the opportunity to buy the equipment directly from the site. This also helps create an 'all in one' portal for all things cooking!

    * #### Order Recipe Ingredients
        Very similar to the cook shop, offering the customers a quick and easy solution to buy all the necessary ingredients for the recipe would be a great feature for those who want a quick an easy solution to producing these foods themselves at home, and would also offer another revenue generating opportunity to the site.

        The recipes could have a button at the bottom that users could click to buy the exact ingredients listed within the recipe.

## <span id="database"><b>Database</b></span>

As part of my planning process, I felt it was important to work out what fields I would need to use and share as part of the site.

<img src="readme-images/wireframe-databases.png" alt="Wireframe image for the database plans." width="100%">

## <span id="key-components"><b>Key Components</b></span>

* ### <span id="key-components-languages"><b>Languages</b></span>

    * #### [HTML5](https://en.wikipedia.org/wiki/HTML5)
    * #### [CSS3](https://en.wikipedia.org/wiki/CSS)
    * #### [JavaScript](https://www.javascript.com/)
    * #### [Python](https://www.python.org/)

* ### <span id="key-components-frameworks"><b>Frameworks & Libraries</b></span>

    * #### [Flask](https://palletsprojects.com/p/flask/)
    * #### [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/)
    * #### [jQuery](https://jqueryui.com/)
    * #### [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)
    * #### [Werkzeug](https://pypi.org/project/Werkzeug/)
    * #### [FontAwesome](https://fontawesome.com/)
    * #### [Google Fonts](https://fonts.google.com/)
    * #### [Materialize](https://materializecss.com/)

* ### <span id="key-components-others"><b>Others</b></span>

    * #### [GitHub](https://github.com/) - Repository Hosting
    * #### [GitPod](https://www.gitpod.io/) - Development Enviroment
    * #### [Adobe Illustrator](https://www.adobe.com/uk/products/illustrator.html) - Used to create the logo and favicon
    * #### [Website Mockup Generator](https://websitemockupgenerator.com/) - To create the opening image for the README.
    * #### [TinyPNG](https://tinypng.com/) - Used to reduce image file sizes
    * #### [Lighthouse](https://developers.google.com/web/tools/lighthouse) - Performance and Accessibility Reporting
    * #### [Balsamiq](https://balsamiq.com/) - Used to build the wireframes
    * #### [MongoDB](https://www.mongodb.com/) - Database hosting
    * #### [Heroku](https://www.heroku.com/) - Live site deployment
    * #### [Am I Responsive](http://ami.responsivedesign.is/) - To check responsive design
    * #### [W3 Validator](https://validator.w3.org/) - To check my HTML code


## <span id="testing"><b>Testing</b></span>
* ### <span id="testing-problems-during-development"><b>Problems During Development</b></span>

A blank search would return an error, therefore I had to include an IF statement that would display the main page with all recipes if the user was to search a blank field.

<br>

* ### <span id="testing-bugs"><b>Known Bugs</b></span>

<br>

* ### <span id="testing-html"><b>HTML</b></span>

    To test my HTML code, I used the [W3 Validator](https://validator.w3.org/)

    A common problem that kept appearing in the validation was the error relating to the multiple uses of the same id's. 
    When writing some of the for loops, it never occured to me that by using the ID within the loop, it would be repeating itself multiple times on the published page. I quickly resolved these issues by changing the ID's to class rules. Once I made these changes, the all of the pages passed the validation check.

    Here is the pass report for the homepage:

    <img src="readme-images/html_validation_report.png" alt="HTML Validation Report" width="80%">

<br>

* ### <span id="testing-css"><b>CSS</b></span>

    To test my CSS code, I used the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

    When I first ran the validator, it returned the following errors:

    <img src="readme-images/css_errors.png" alt="CSS Validator Error Report" width="80%">

    The first error was simply a typing error and once the ',' was removed the error was cleared.

    The next two errors were due to the sizes I had entered as the parameters for the media queries. I had entered the dimensions incorrectly, setting a parameter of 319px instead of 320px for example. I had also generated 2 media queries to cover 2 screen dimensions, I then realised I could achieve the desired results with a much simpler query, setting the page logo to a smaller size for screen widths of less than 768px.

    Once I made the changes above, the errors were then cleared. However there are 3 remaining warnings within the CSS validation, these errors related to external style sheets as part of the Materialize style sheets and extensions.

    Here is the pass report:

    <img src="readme-images/css_pass.png" alt="CSS Validator Report" width="80%">

<br>

* ### <span id="testing-javascript"><b>Javascript</b></span>

    To test my Javascript code, I used the [JSHint Validator](https://jshint.com/)

    The initial report showed that I had an instance that was no longer being used, to correct this error I removed this instance.

    Further errors were listed (as shown below) that related to the validator reporting that each '$' was an undefined variable.
    I believe this is an issue within the validator itself. It is trying to determine that the '$' is a variable in itself.
    I therefore ignored these errors as the functions would not work correctly without the '$'.

    <img src="readme-images/js_error_report.png" alt="JSHint Validator Report" width="80%">

<br>

* ### <span id="testing-lighthouse"><b>Overall Website Performance & Compatibility</b></span>

    To test my websites performance and compatibility, I used [Lighthouse](https://developers.google.com/web/tools/lighthouse)

    The initial lighthouse report showed that there was a significant issue with the accessibility score that related to the choice of colors that were used for the site.

    There were areas of the site that did not meet the color contrast requirement of the site. A poor contrast between colors can often be difficult and uncomfertable for users to see. To help improve this score and to ensure the site is easy to read, I altered some of the poorly contrasting colors and made sure that any background colors work well with the foreground colors.

    Once I rectified this issue, I ran the tests again and the results showed a poor rating for the performance. 

    <img src="readme-images/lighthouse_error_report.png" alt="Lighthouse Error Report" width="80%">

    These errors were due to load times for the images being used for the recipes on the site, as these are external URL's to images then I have no control of the size or format of image that the user has uploaded. I researched what options were available to deal with images being loaded from URL's and the only solution I found was to include '?tr=q-10' at the end of the image URL's. This reduces the quality of the image to 20% when loading.  This increased my performance score from 70 to 72.

    <img src="readme-images/lighthouse_report.png" alt="Lighthouse Report" width="80%">

    In the future I would like to include the possibility for users to upload and store the images onto the websites server, this will help manage file sizes, and types in order to improve load times.

<br>

* ### <span id="testing-responsive-design"><b>Responsive Design</b></span>
* ### <span id="testing-browser-compatibility"><b>Browser Compatibility</b></span>
* ### <span id="testing-links"><b>Link Testing</b></span>

## <span id="deployment"><b>Deployment</b></span>

* ### <span id="deployment-github"><b>Deployment Through GitHub Pages</b></span>
* ### <span id="deployment-forking"><b>Forking</b></span>
* ### <span id="deployment-cloning"><b>Cloning Project</b></span>
* ### <span id="deployment-admin"><b>Administrator Access Credentials</b></span>

## <span id="credits"><b>Credits</b></span>

* ### <span id="credits-content"><b>Content</b></span>

* ### <span id="credits-media"><b>Media</b></span>

* ### <span id="credits-code"><b>Code</b></span>

Function to add additional fields to form: https://www.codexworld.com/add-remove-input-fields-dynamically-using-jquery/

* ### <span id="credits-acknowledgments"><b>Acknowledgements</b></span>