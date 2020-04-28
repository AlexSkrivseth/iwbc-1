Idaho Wilderness Boys Camp Web App

February 11th, 2020

OVERVIEW
I would like to create a website to direct applicants to apply to the camp. All of the info would be then displayed in a variety of ways to make planning easier for the administrators.  

GOALS
  - Provide an informative about page (already done with the church page) https://kvmcs.org/idaho-wilderness-boys-camp
  - Provide an application page that boys could apply to camp
  - Have an admin dashboard where data can be viewed and actions can be done
  - Send out acceptance emails based on who is accepted
  - Have links to helpful packing tips
  - Have links to required gear


SPECIFICATIONS
    Built with Django for the backend.
    Bootstrap4 for the frontend.
    AWS s3 for static assets like pictures and files.
    Hosted on heroku using a hobby dyno.
    Postgres database will need to be implemented as well.
    API that can be used later for building out other features.






PAGES

WELCOME PAGE
  - APPLY FOR CAMP BUTTON
SIGN UP
  - EMAIL
  - PASSWORD
  - LOG IN
  - FORGOT PASSWORD?


APPLICATION PAGE

APPLICANT DASHBOARD
  - Gets created after the boys is accepted
  - Displays helpful packing tips and required gear
  - Provides a path to pay for tuition with card (displays paid once the boy has paid)
  - Gives them options to fill in Flight info or other travel arrangements
  - Prompts them to buy tickets within certain arrival times
  - Allow them to communicate the way that they will be arriving

ADMIN DASHBOARD
  - WHAT DOES THE ADMIN WANT TO HAVE DISPLAYED?
  - LIST OF ALL APPLICANTS FOR THE CURRENT YEAR?
  - LIST OF ACCEPTED AND CONFIRMED APPLICANTS?
  - THE ABILITY TO MESSAGE ALL OF THE CONFIRMED APPLICANTS
  - CHANGE INFO
  - MAKE GROUPS
  - SPLIT BOYS INTO GROUPS
  - VIEW THE STANDARD SCHEDULE FOR EACH GROUP
