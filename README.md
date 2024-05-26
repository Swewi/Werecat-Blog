![Werecat Industries Logo](static/images/readme/cat-eyes1.jpg)

# Werecat Industries Blog
## Portfolio Project 4 - Fullstack Dev course taught by Code Institute

## [Link to live site](https://werecat-blog-46217e65417f.herokuapp.com/)

![Screenshot of Responsive site created by TechSini](static/images/readme/Django-werecat.png)

### This is Portfolio Project 4 for Full Stack Developer Diploma taught through Code Insititute.

## Purpose

The idea behind this website was to design a blog for a couple of crafty people that want to take things to the next level.

## Design

The client wanted a 'blog' so they could keep their community upto date with their project, any courses they may want to expand into, interesting events and information.  The second ask was for a 'contact form' so that people could contact them.  The third thing they wanted was an 'about me' page to introduce themselves to the world.  And finally they wanted a 'gallery' to show off.

They requested a vibrant cyberpunk colour scheme, when questioned about a preference for background image versus a solid colour, they said they had been playing with AI image generation and would love to have a background image using the colour scheme discused, and AI image generation.  We had a play with several generators while we were discussing things, and had a play with prompts.  After several tries we settled on this image:

![Background image for blog](static/images/readme/Background.jpeg)

The client loved it, and we were asked to proceed.

## UX - layout

### Home Page

This is the first page you see when opening the site, it has a responsive design so that it displays differently for different sized screens, the version shown here is for an ipad.

![Home page for an ipad sized screen](static/images/readme/home%20ipad.png)

#### Navbar

It has a fully functional navbar:

Large screen version

![Large screen navbar including Admin button](static/images/readme/navbar%20inc%20admin.png)

Small screen version

![Small screen navbar](static/images/readme/menu%20small%20screen.png)

You can see that there is an admin button on the right hand side, this allows a user logged in as Admin can access the admin panel directly from the home page.  There is a 'sign out' link, that will be display as follows:

![Sign out screen](static/images/readme/sign%20out%20screen%20-%20large%20laptop.png)

You will recieve a message once you succesfully log out:

![Sign out message](static/images/readme/logout%20alert.png)

After succesfully signing out the sign out button is replaced with a 'register' and 'sign in' link.  If either of these options is clicked you it will re-direct you to the appropiate screen.

The register link opens to show this page, shown here for ipads:

![Sign up/register screen](static/images/readme/signup%20ipad.png)

The sign-in link opens to show the following page:

![Sign in larger screen](static/images/readme/signin%20screen%20laptop.png)

The same page for a smaller mobile screen:

![Sign in small screen](static/images/readme/signin%20galaxy%20fold.png)

After succesfully registering or signing in there will be a message shown to notify you, I have only shown a single version here:

![Sign in alert](static/images/readme/signin%20alert.png)

#### Body of the page

Under the navbar we find the section with the blog posts, these are displayed in a card form that will open the post completely when the title of the post is clicked.  Each card shows a header image, that is by default, the same one shown at the top of the ReadMe, however there is an option to add images to the post to override this.

Blog post opened up for reading in a mobile phone sized screen:

![Mobile screen blog post](static/images/readme/)

Same post but for an ipad sized screen:

![ipad screen sized blog post](static/images/readme/)