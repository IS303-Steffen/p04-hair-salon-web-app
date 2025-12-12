#### Project
# Hair Salon Web App
#### Team Projects Overview
- This is a team project. Through GitHub Classroom you should have created a shared GitHub repository with your teammates. As long as you upload your finished code to that team repository, each team member will get credit. You will also need to fill out a peer review survey on Learning Suite to recieve credit (if you're in a team by yourself, you don't need to).
- I do not provide automated tests for projects. You will need to determine yourself whether the code meets the requirements provided in the rubric. It is important for you to be able to determine whether a program you write meets requirements (in the real world there won't be pre-written tests to tell you if you did your job right).
#### Overview
- [Click here](https://www.youtube.com/watch?v=4VG8CLuQtRU) for a video of me running through what the project will look like.
- The point of this project is to translate logic similar to your previous project to use a GUI web application using Streamlit, and then actually host your project on the internet so that anyone could use it. Most of the set up and a lot of the logic from your previous project is already present here in the `data_to_insert.py` file.
- This project is split up into 4 parts in 4 different files:
    - **Part 1: Set up your database on Supabase**
        - You'll need to create an account on [Supabase.com](https://www.supabase.com) and create the connection to your app. Or you can forgo this step for a loss of 5 points.
    - **Part 2: Set up your app to have 2 pages**
        - Use the `0_salon_app.py` file
    - **Part 3: Write the GUI for the customer check-in process**
        - Use the `1_check_in.py` file
    - **Part 4: Write the GUI for the manager tools**
        - Use the `2_manager_tools.py` file
    - **Part 5: Host your app on the Streamlit Community Cloud**
        - You'll need to create an account with [Streamlit](https://streamlit.io). You can forgo this step for a loss of 5 points.
- Important: Because you'll have multiple .py files open, make sure you save all your open files before running any single file.
    - You can go to File > Save All in VS Code to do this.
    - Or, the shortcut on Mac is `cmd + opt + s`
    - Or, the shortcut on Windows is `ctrl + k` then release the keys, then press `s`

## Libraries Required:
- `streamlit`
- `peewee`
- `pandas`
- `psycopg2`
    - only if you use Supabase. You don't need to import it, but it is needed for `peewee` to work with Supabase and a postgres database. Installation instructions will be given in part 1.
- If you are using a virtual environment, you can run `pip install -r requirements.txt` to install everything needed.

## Part 1: Set up your database on Supabase
### If you want to skip Part 1 at the cost of 5 points:
- If you're short on time or can't get Supabase to work, but still want everything else to work:
    1. Go into the `db_setup_and_helpers.py` module
    2. change the line near the top that says `USE_SUPABASE = True` to `USE_SUPABASE = False`
    3. Run the file. It will create an SQLite database with all the data loaded in for you.
- I recommend trying to get your program working with Supabase though. I explain why below.

### What is Supabase and why are we using it?
Supabase is an online service that hosts **PostgreSQL databases**, which are much more robust and capable than SQLite. We’re using Supabase in this project for three main reasons:

1. **Streamlit Community Cloud doesn’t persist local files.**  
   If you host your Streamlit app on the internet through Streamlit Community Cloud, it runs your app in a temporary virtual machine (VM). When the VM shuts down (because nobody is using your app or when it redeploys), any local files (like an SQLite database) are deleted.  
   By using Supabase, your data is stored externally and **persists across sessions**, which is how real web applications work.
2. **PostgreSQL is widely used in industry.**  
   Supabase gives you experience with a production-grade relational database. Even though your project uses fake salon data, the workflow mirrors how real companies build applications. Better to get some introductory experience to something you could use in real work.
3. **Supabase is simple to set up and works seamlessly with Peewee.**  
   Supabase provides an easy UI, clear connection credentials, and integrates smoothly with the Peewee ORM you’ve already learned. This lets you focus on learning web application development rather than database administration.

### Setting up your postgreSQL database with Supabase
#### 1. Install `psycopg2` 
- Before anything else, for `peewee` to work with postgresql databases, you need to have the `psycopg2` library installed. In your terminal, use one of the following:
    - `pip install psycopg2`
        - or if that doesn't work
    - `pip install psycopg2-binary`
        - or if you need to use pip3:
    - `pip3 install psycopg2` or `pip3 install psycopg2-binary`
- It just needs to be installed, no need to import it anywhere.

#### 2. Follow this tutorial to set up a Supabase account and postgresql database
- Head over to [supabase.com](https://supabase.com/) and then follow along with [this tutorial here (click)](https://www.youtube.com/watch?v=SCwN5uAjAjY)

#### 3. Set up your `secrets.toml` (shown in the tutorial video)
- The tutorial video will go over this, but below you can copy and paste this into your `secrets.toml` file that you create inside the `.streamlit` folder (remember the . in the folder name)
- Update the values for each line using the connection data from Supabase as shown in the video, as well as with the password you made. This isn't your Supabase account password, but the password you made when you made your project.
- Note that this (purposefully) won't sync to GitHub, so if you are working in a team at separate times, if you set this up, give your teammates this info and make sure they know to make their own `secrets.toml` on their computer.

```
SUPABASE_DB_HOST = ""
SUPABASE_DB_PORT = "5432"
SUPABASE_DB_NAME = ""
SUPABASE_DB_USER = ""
SUPABASE_DB_PASSWORD = ""
```

#### 4. Open the `db_setup_and_helpers.py` file and run it (also shown in the tutorial video).
- You already set up the peewee code and imported data in your last project, so I already wrote that part for you to save you time. Just run the `db_setup_and_helpers.py` file and it will automatically create your database and fill it with data, assuming you set up everything in `secrets.toml` and Supabase correctly. Rerun the file anytime you want to start the data from scratch.

## Part 2: Set up your app to have 2 pages
In `0_salon_app.py` you will write the setup for the 2 other pages of your web app. 
- It looks basically like what you did in file `10a` of the class practice if you want to reference the solution for that.
1. Import streamlit and create pages for `1_check_in.py` and `2_manager_tools.py` using `st.Page()`
2. Set up the navigation bar using `st.navigation()`. Give it the 2 pages you created, and set `position='top'`. Store the result in a variable
3. Call `.run()` using the variable you created in step 2.
From now on in the project, any time you want to run your app just use:
- `streamlit run 0_salon_app.py` or `python -m streamlit 0_salon_app.py`


## Part 3: Write the GUI for the customer check-in process
- You need to replicate similar check-in logic from the previous project, but using Streamlit. Put this in the `1_check_in.py` module. You just need to fulfill the listed requirements, but you are given lots of prewritten code to save you time if you follow the recommended logical flow.
### Requirements
1. *Get the user's phone number*
    - If the phone number isn't valid, display an error message and don't move to a different view.
2. *If the phone number is valid, but doesn't match an existing customer, go to a view to gather their info and create a new Customer in the database.*
3. *If the phone number is valid and matches an existing customer, go to a view that allows them to choose a hairstyle and stylist, but pre-select their previously chosen options.*
4. *Allow new customers to select their hairstyle and stylist, but don't preselect any options.*
5. *Bring the customers to a check out view to indicate if they were satisfied or not*
6. *Return to the original phone number view*

### Recommended Logical Flow for Part 3
**I highly recommend** you look at the solution for file `09_multiple_views_one_page` from the class practice. If you understand that file, this will be much easier.

You are given several functions to save you time so you don't have to rewrite a lot of what you did in your previous project. I recommend just using these imports:
```
import streamlit as st
from datetime import datetime
from db_setup_and_helpers import (
    clean_phone_number,
    get_customer_if_exists,
    get_all_stylists,
    get_index_of_most_recent_stylist,
    pretend_to_get_a_haircut,
    hairstyles_dict,
    Appointment,
    Customer,
)
```

#### 1. Add `current_view` to `st.session_state`
- Before anything, use an if statement to add `current_view` (or use any other name) to `st.session_state` and give it a starting value of something like `enter_phone_number`, but only if it is the first time your script is being run by streamlit.

#### 2. Create the enter phone number view
![enter_phone_number](./media/enter_phone_number.png)
- Only display this view if `enter_phone_number` is the value for `current_view` in `st.session_state`.
- Display:
    - `Check In`
    - `Welcome to Incredible Cuts! Please enter your phone number to check in`
- In a form, use `text_input()` to get a phone number with the message:
    - `Enter your phone number. It must be 10 digits long`
    - Include a form submit button.
- When the form submit button is pressed, take the inputted phone number, and pass it into the `clean_phone_number()` function that you are given.
    - If the phone number isn't valid, `clean_phone_number()` will return `None`. If it returns `None` display a message that says `That wasn't a 10 digit number, try again` and don't look up a customer.
        - You can display that error message just using `st.write()` but you could also use `st.warning()` instead. It displays text in a warning color to make the message pop out to users. 
- If the phone number is a valid 10 digit number, `clean_phone_number()` will return a 10 digit number. Pass that number into the provided `get_customer_if_exists()` function.
    - If `get_customer_if_exists()` can't find a matching customer with that phone number, it will return `None`. If it returns `None`:
        - Store the phone number in `session_state`
        - Set the `current_view` in `session_state` to `new_customer` (or a label that you make)
        - call `st.rerun()` so that it will jump to the `new_customer` view (described in step 2)
    - If `get_customer_if_exists()` finds a matching customer, it will return a customer object:
        - Store the customer object in `session_state`
        - Set the `current_view` in `session_state` to `select_options` (or a label that you make)
        - call `st.rerun()` so that it will jump to the `select_options` view (described in step 3)


#### 3. Create new customer view
![new_customer](./media/new_customer.png)
- Only display this view if `new_customer` is the value for `current_view` in `st.session_state`.
- Display:
    - `Welcome! Fill out your information so we can serve you better:` in large font
- In a form, gather first name, last name, gender (choose between M and F)
    - Include a form submit button.
- When the form submit button is pressed:
    - Take all the information you stored from the form and use it to create a new customer using peewee. Here's an exmaple. Note that I'm grabbing the phone number that they already entered in the `enter_phone_number` view (it is annoying to ask customers to enter the same info twice)
        - ```
            customer_obj = Customer.create(
                c_first_name = first_name,
                c_last_name = last_name,
                c_phone_number = st.session_state.get('customer_phone_number'),
                c_gender = gender
            )
          ```
    - Store the customer object you created in `st.session_state`
    - Set the `current_view` in `session_state` to `select_options` (or a label that you make)
    - call `st.rerun()` so that it will jump to the `select_options` view (described in step 4)

#### 4. Create select options view
![select_options](./media/select_options_new.png)
![select_option_2](./media/select_options_returning.png)
- Only display this view if `select_options` is the value for `current_view` in `st.session_state`.
- At this point, you should have stored a customer object in `st.session_state`, whether it is a brand new customer or a returning customer. Grab it from `st.session_state`.
- Using the customer object, call `customer_object.get_customer_message()` (already written for you) and display the ruturned string in a large font.
- Get a list of stylist objects and a list of the hairstyles. The `get_all_stylists` function and `hairstyles_dict` are already given to you. We'll use these in the selectbox widgets soon.
    - ```
      list_of_stylists = get_all_stylists()
      list_of_haircuts = list(hairstyles_dict.keys())
      ```
- Get the most recent appointment associated with you customer object. The `.get_most_recent_appointment()` method is already written for you. If the customer object is a new customer, it will return `None`, otherwise it will return an appointment object.
    - `appt_obj = customer_object.get_most_recent_appointment()`
- In a form, you'll need to display slighlty different things in this view depending on if they are a returning customer or new customer. You can tell them apart because returning customers will have an appointment object returned, but new customers will just have `None` returned.
    - *Returning customers (they have an appointment object):*
        - Display in semi-large text: `"### We've pre-selected the stylist and hairstyle you got last time, but feel free to choose any other if you'd like:"`
        - In selectboxes, display the same hairstylist and hairstyle that they got on their last appointment. You can find the indices of those like this:
            - ```
              stylist_index = get_index_of_most_recent_stylist(appt_obj)
              hairstyle_index = list_of_haircuts.index(appt_obj.a_haircut_type)
              ```
    - *New customers (they have no appointment object):*
        - Display in semi-large text: `"### Choose your preferred stylist and hairstyle:"`
        - In selectboxes, you'll allow them to choose a hairstylist and hairstyle that they got on their last appointment. You can just use `None` for their indices so the customer can just choose their first stylist and hairstyle manually.
            - ```
              stylist_index = None
              hairstyle_index = None
              ```
- When the form submit button is pressed:
    - Store the selected stylist object you created in `st.session_state`
        - if you are using the `list_of_stylists` code that I gave you above in your selectbox, the returned value of the selectbox choice will be a stylist object.
    - Store the selected hairstyle (a string) in `st.session_state`
    - Set the `current_view` in `session_state` to `getting_haircut` (or a label that you make)
    - call `st.rerun()` so that it will jump to the `getting_haircut` view (described in step 5)
    - Optional: If you want to (for no extra points) add some robustness, check if a stylist and hairstyle were selected before letting your code rerun, that way no new customer ever submits the form without choosing anything.

#### 5. Create the getting haircut view
- This is already made for you. I thought it would be fun to show you how you can have a progress bar. Feel free to look at the definition of the `pretend_to_get_a_haircut` function if you're curious how it works
```
elif st.session_state.get('current_view') == 'getting_haircut':
    pretend_to_get_a_haircut()
    st.session_state['current_view'] = 'check_out'
    st.rerun()
```

#### 6. Create check out view
![check_out](./media/check_out.png)
- Only display this view if `check_out` is the value for `current_view` in `st.session_state`.
- Get the customer object in `st.session_state`
- Using the name of the customer object, write out in large font:
    - `## Thank you for choosing Incredible Cuts, <customer first name>`
- Add a selectbox with the text `Were you satisfied with your haircut?` with the options being `Yes` or `No`.
    - If they choose `Yes` map that to a boolean `True`, `No` maps to boolean `False`
- When they hit the submit button, create an appointment row in your database. You can reference this code, but make yours match whatever you actually called your variables:
    - ```
      Appointment.create(
          a_haircut_type=st.session_state.get('chosen_hairstyle'),
          a_date_time = datetime.today(),
          a_payment = hairstyles_dict.get(st.session_state.get('chosen_hairstyle')),
          a_satisfied = satisfaction,
          c_id = customer_obj.c_id,
          s_id = st.session_state['chosen_stylist'].s_id
      )
      ```
- Set the `current_view` in `session_state` to `enter_phone_number` (or a label that you make)
- call `st.rerun()` so that it will jump to back to the `enter_phone_number` view, so a new customer could jump in.


## Part 4: Write the GUI for the manager tools
![manager_tools](./media/manager_tools.png)
- The point of this module is to simulate a few of the capabilities and reports that a manager of the hair salon might want access to. Put your code in the `2_manager_tools.py` file.
- Use these imports:
```
import streamlit as st
from db_setup_and_helpers import get_manager_tools_df, get_all_stylists
import time
```
- Write `Manager Tools` in the largest font, with `Choose an option:` in a smaller font.
- Use a selectbox to have 2 options (with the index being `None` so neither option is selected when the page first loads):

#### First Option: "View satisfaction rate by stylist"
![satisfaction_rate](./media/satisfaction_rate.png)
- The first option in the selectbox widget should be `View satisfaction rate by stylist`
- If it is selected, display the dataframe returned from the function `get_manager_tools_df()`

#### Second Option: "Terminate a stylist"
![delete_stylist](./media/delete_stylist.png)
- The second option in the selectbox widget should be `Terminate a stylist`
- If it is selected, create a form that displays another selectbox with the stylists all listed in a selectbox.
    - use the provided function `get_all_stylists()` to get a list of stylist objects to use in the selectbox widget.
- When the button is pressed:
    - write out `You have terminated <stylist first name> <stylist last name>`
    - delete that stylist by using `.delete_instance()` on the chosen stylist object
    - Then call `time.sleep(1.5)` to pause the program for a second and a half (so the user has time to read the message on who was deleted)
    - then run `st.rerun()` so that the page reruns and the deleted stylist isn't in the list anymore.

## Part 5: Host your app on the Streamlit Community Cloud
You just need to follow along with a tutorial posted below. Before that though, here's some background on hosting apps:
### What does it mean to "host" and "deploy" your app?

- **Hosting an app** means running your program on a computer (a server) that is always available on the internet (so not just on your own laptop).
- **Deploying an app** means uploading your code to that online server so other people can use it.
- When you deploy to **Streamlit Community Cloud**, your Python code runs on a remote server managed by Streamlit, not on your computer. They are nice and let people run small apps for free, but if you want more capability, you need to pay.
- Because it’s hosted online, **your app gets a public URL**, and anyone with that link can open and interact with your program from anywhere.
- Using **Supabase** for your database means your data also lives on the internet, so your app can access it whenever.

![hosted_app_image](./media/system_design.png)

### Deploy your app
To deploy your app, head over to [streamlit.io](https://streamlit.io) and follow along with [this tutorial](https://www.youtube.com/watch?v=-EK4hIF6-_g)
- If you can get your app's check in page to appear, but it breaks anytime you try to check in with a phone number, you probably have an issue with you secrets file. [Watch this video](https://www.youtube.com/watch?v=kaXKcnR9PmI) to see if that fixes your problem.
- If you run into any other issues, please reach out to your professor or TA. 

**IMPORTANT**:
- Make sure you made your app public. It shows how to do this at the end of the tutorial above, or you can [see here](https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app) for instructions.
- To get credit for hosting, you NEED to paste in the URL of your hosted web app in the `3_paste_your_url_here.txt` file.

## Grading Rubric
Remember there are no automated tests for projects. `See RUBRIC.md`. Remember to right click and select "Open Preview" to view the file in a nice format. The TAs will update this file with your grade and any comments they have when they are done grading your submission.

## Example Output
Nothing prints in the terminal in this project, but you can watch the overview video again to see what your GUI should look like [here](https://www.youtube.com/watch?v=4VG8CLuQtRU).
