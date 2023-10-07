# SheFunds  - Backend

SheFunds was born as a class project for SheCodes cohort of Brisbane 2023.  

The goal of the project is to provide a one-stop-shop for students to browse and apply to programs.  

 For admins, to upkeep and maintain a dynamic view of available open programs, review applications and match students with the best scholarship for them.

 ## Contributors  
 Tracey Nguyen - Add github link?  
 Julie Powell - Add github link?   
 Cinzia Loi - Add github link?  

## Features: 
**USERS**  

Type | Access | Role type assignment
--- | --- | ---
*Admin* | All access    | **All SheCodes staff**  
-- | Can log in | --
-- | Can log out | --
-- | Create and manage Programs | --
-- | Create and manage Scholarships | --
-- | Create and manage other users | --
-- | View and manage applications | --
*Applicants* | Can browse open programs | **Public -anyone with link**
-- | Can apply for programs | --
-- | As explicitly requested by PO applications cannot be withdrawn | --


**SCHOLARSHIPS**  

Feature | Access | Note/Condition
--- | --- | ---
*Create, update, view* | Admin    | **User must be logged in**  
*Delete* | Admin | **Must be inactive** 


**APPLICATION**  

Feature | Access | Note/Condition
--- | --- | ---
*Create* | Anyone with a link    |   
*View* | Admin | **Must be logged in** 
*Update* | Admin | **Must be logged in** 
-- | -- | **Can only update specific fields (EG Is_accepted? And Scholarship)** 
*Delete* | Admin | **Must be logged in** 



**STRETCH GOALS**:  

- Dynamic form for new posting programs/questions  
- Profile accessible via login for applicants to update personal info and application.  
- Auto email applicants to let them know the outcome of their application  
- Auto email newly created users with their first-login credentials  
- Matrix to suggest best sponsor for an applicant based on predefined criteria  
- Search criteria for open programs for applicant
Editing own user profile


## Languages & Frameworks: 

Back-end:  

Django Rest Framework (DRF) API  
Python  

## Database schema  
To be added later

## Submission Documentation 
Deployed Project: [Deployed website]() 

## Instructions For Setting Up This Repo

1. Clone the repo down with `git clone https://github.com/SheCodesAus/heading_for_success_backend_bris_2023.git`
2. Create and activate a `venv`
3. Install dependencies with `pip install -r requirements.txt`

