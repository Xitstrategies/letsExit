# Welcome!

## Projects we are working on

A. Shipment creation
  * Making sure all the fields are defined
  * Making sure all the field types are what we want and have the right attributes (max_length, null=True, etc.)
  * Building the Views for creating, searching, editing shipments

B. Determine which db type we should use
  * MySQL
  * PostgreSQL

B. User registration
  * Models
  * Views for registering, logging in, editing the user information
  * Views for changing passwords, etc.
  * Create tests

C. Subscription structures
  * Models
  * Views for Super users to create subscriptions, products, etc.
  * Hook up billing code for products
  * Views for clients to register for subscriptions per user/whole client
  * Create tests
  * 2.0 Submit billing info to Xero/Quickbooks

D. Create Logging for everything
  * creation
  * editing
  * reports

E. Create EDI file creation for transmittal
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

F. Expose certain parts of the API for customers to submit information straight to the DB for shipments and run the checks/submission

G. Create EDI file Inbound to create shipments
