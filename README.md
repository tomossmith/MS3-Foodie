<style>

@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@200;300;400;500;600;700&display=swap');

body{
    background-color: black;
    font-family: Oswald;
    font-weight: 300;
    letter-spacing: 1px;
}
</style>

<center><img src="static/images/logo.png" alt="Foodie Logo" width="50%"></center>

----

This is the README file for my Code Institute MS3 project site, Foodie - The Recipe Sharing Site

This project is the 3rd project as part of the Code Institute Full Stack Development course. The projects are set in order to demonstrate my understanding of what we have learnt during the previous units.
The task set for this project is to demonstrate the ability to create a fully responsive web application that allows users to interact and manipulate with data stored in a database.

############### PHOTOS OF THE LIVE SITE ################

[Click Here to visit the live site](https://ts-foodie.herokuapp.com/)

----

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

    <center><img src="readme-images/color.jpeg" alt="Color Palette" width="50%"></center>

    After finding the colors I felt were most suitable I implemented them into the site, in later stages of development I began testing the site's compatibility using [Adobe Color](https://developers.google.com/web/tools/lighthouse) and it was brought to my attention that the way I was using the colors was not meeting lightroom's accessibility criterias due to contrasting colors. I have explained further in my testing section on the steps I had to take to overcome this issue.


* ### <span id="ux-design-typography"><b>Typography</b></span>

* ### <span id="ux-design-images"><b>Images</b></span>



* ### <span id="ux-design-structure"><b>Structure & Mockup Designs</b></span>

* ### <span id="ux-design-amendments"><b>Amendments To Mockup Designs During Development</b></span>

## <span id="features"><b>Features</b></span>

* ### <span id="features-current"><b>Current Features</b></span>

* ### <span id="features-future"><b>Possible Future Features</b></span>

## <span id="database"><b>Database</b></span>

## <span id="key-components"><b>Key Components</b></span>

* ### <span id="key-components-languages"><b>Languages</b></span>

* ### <span id="key-components-frameworks"><b>Frameworks & Libraries</b></span>

* ### <span id="key-components-others"><b>Others</b></span>

## <span id="testing"><b>Testing</b></span>
* ### <span id="testing-problems-during-development"><b>Problems During Development</b></span>
* ### <span id="testing-bugs"><b>Known Bugs</b></span>
* ### <span id="testing-html"><b>HTML</b></span>
* ### <span id="testing-css"><b>CSS</b></span>
* ### <span id="testing-javascript"><b>Javascript</b></span>
* ### <span id="testing-lighthouse"><b>Overall Website Performance & Compatibility</b></span>
<< MENTION COLOR CONTRASTS >>
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