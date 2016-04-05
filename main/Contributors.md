# Welcome!
## Project Setup
### Prerequisites
-Python 2+
-Django ..+
-Node 5+

### To Install
1. `git clone the project to a directory of your choosing`
2. virtual / docker
3. `pip install -r requirements.txt`
4. `cp xitstrategies/xitstrategies/local_settings_example.py local_settings.py`
adjust any db/port settings to run the dev server locally
5. set up the database locally
```
python manage.py syncdb
python manage.py migrate
```
6. `npm install`
7. `python manage.py runserver`

## Editors
I would love to not have to say anything about this, but the editor you use determines your code quality more than you know.
Please use either
Atom.io some configuration required
Webstorm less configuration required
JetBrains Python editor some configuration required

If you must, use another editor of your choosing, but please update this section and include ALL of the configuration adjusts to ensure the editor is enforcing/reminding you of the code standards set in this project.

#### Configuring editor
set up editor to look at eslint file
.. python enforcement
.. sql enforcement
.. html enforcement
..


## Projects we are working on
A. Basic creation
  * Making sure all basic resources are available (city, country, hazmat, hts, etc.)
  * Make sure we can edit the basic resources clearly from the django admin pages

B. Shipment creation
  * Making sure all the fields are defined
  * Making sure all the field types are what we want and have the right attributes (max_length, null=True, etc.)
  * Building the Views for creating, searching, editing shipments

C. Determine which db type we should use and set up in Docker
  * MySQL
  * PostgreSQL

D. Wrap applications in Docker
  * Authentication
  * Shipment

D. User registration
  * Models
  * Views for registering, logging in, editing the user information
  * Views for changing passwords, etc.
  * Create tests

E. Subscription structures
  * Models
  * Views for Super users to create subscriptions, products, etc.
  * Hook up billing code for products
  * Views for clients to register for subscriptions per user/whole client
  * Create tests
  * 2.0 Submit billing info to Xero/Quickbooks

F. Create Logging for everything
  * creation
  * editing
  * reports

. Create EDI file creation for transmittal
  * US AMS/ACE Import (Ocean NVO)
  * US AMS/ACE Import (Ocean MVO)
  * Japan AFR (Ocean NVO)
  * Japan AFR (Ocean MVO)
  * US AMS/ACE Import (Air MVO/NVO)
  * US AMS/ACE Export (Air MVO/NVO)
  * US AMS/ACE Export (Ocean MVO/NVO)
  * US AMS/ACE Export (Rail)?
  * EU UK (Ocean MVO)
  * EU UK (Air MVO)
  * EU additional countries
  * logging of transmissions sent and received back from customs
  * create reports and ways to easily view the transmissions and status'

. Expose certain parts of the API for customers to submit information straight to the DB for shipments and run the checks/submission

. Create EDI file Inbound to create shipments
