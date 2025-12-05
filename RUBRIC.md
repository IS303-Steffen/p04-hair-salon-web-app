### MAX SCORE: 100
### YOUR SCORE:  
## Grader's Notes:
- TAs: Put any notes on points lost here.
---
## Rubric

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>#</th>
      <th>Requirement</th>
      <th>Points</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>0_salon_app.py defines separate pages for 1_check_in.py and 2_manager_tools.py using st.Page (or equivalent) with correct labels / file references.</td>
      <td>6</td>
    </tr>
    <tr>
      <td>2</td>
      <td>0_salon_app.py sets up navigation with st.navigation(..., position="top") (or equivalent) and calls .run() so both pages are reachable.</td>
      <td>4</td>
    </tr>
    <tr>
      <td>3</td>
      <td>db_setup_and_helpers.py is correctly configured to use Supabase (USE_SUPABASE = True), connects to the Supabase PostgreSQL database, and creates/populates the tables.</td>
      <td>5</td>
    </tr>
    <tr>
      <td>4</td>
      <td>1_check_in.py correctly uses st.session_state (e.g., current_view) and st.rerun() to manage multi-view flow between the different screens.</td>
      <td>6</td>
    </tr>
    <tr>
      <td>5</td>
      <td>1_check_in.py implements the “enter phone number” view: shows instructions, collects phone number via a form, validates using clean_phone_number (or equivalent), and shows an error without changing views when invalid.</td>
      <td>8</td>
    </tr>
    <tr>
      <td>6</td>
      <td>1_check_in.py, on valid phone input, correctly branches: stores phone/customer in session_state, looks up existing customers (e.g., get_customer_if_exists), and sets current_view to either “new customer” or “select options”, then reruns.</td>
      <td>8</td>
    </tr>
    <tr>
      <td>7</td>
      <td>1_check_in.py implements the “new customer” view: collects first name, last name, and gender in a form, creates a new Customer row in the database using the stored phone number, stores the customer object in session_state, and moves to the “select options” view.</td>
      <td>8</td>
    </tr>
    <tr>
      <td>8</td>
      <td>1_check_in.py implements the “select options” view for both new and returning customers: shows customer message, loads stylists and hairstyles, pre-selects previous stylist/hairstyle for returning customers, leaves selections empty for new customers, and stores chosen stylist and hairstyle in session_state.</td>
      <td>12</td>
    </tr>
    <tr>
      <td>9</td>
      <td>1_check_in.py implements the “getting haircut” view: calls pretend_to_get_a_haircut (or equivalent progress bar behavior), then transitions to the “check out” view.</td>
      <td>3</td>
    </tr>
    <tr>
      <td>10</td>
      <td>1_check_in.py implements the “check out” view: thanks the customer by first name, collects satisfaction (Yes/No mapped to True/False), creates a new Appointment row with correct fields (including price from hairstyles_dict and correct c_id and s_id), and returns to the original phone number view.</td>
      <td>12</td>
    </tr>
    <tr>
      <td>11</td>
      <td>2_manager_tools.py displays “Manager Tools” heading, a “Choose an option:” subheading, and a selectbox with exactly the two options: “View satisfaction rate by stylist” and “Terminate a stylist” (with no default selection).</td>
      <td>4</td>
    </tr>
    <tr>
      <td>12</td>
      <td>2_manager_tools.py correctly implements “View satisfaction rate by stylist”: when selected, shows the dataframe returned by get_manager_tools_df().</td>
      <td>7</td>
    </tr>
    <tr>
      <td>13</td>
      <td>2_manager_tools.py correctly implements “Terminate a stylist”: shows stylists in a selectbox (via get_all_stylists), deletes the selected stylist with delete_instance(), shows the termination message, pauses briefly, and reruns so the stylist disappears from the list.</td>
      <td>10</td>
    </tr>
    <tr>
      <td>14</td>
      <td>App is hosted on Streamlit Community Cloud and the working URL is pasted into past_your_url_here.txt.</td>
      <td>7</td>
    </tr>
    <tr>
      <td colspan="2">Total</td>
      <td>100</td>
    </tr>
  </tbody>
</table>

## TA Guide:

1. #### 0_salon_app.py defines separate pages for 1_check_in.py and 2_manager_tools.py using st.Page (or equivalent) with correct labels / file references.
   - 6 points  
     - -2 if only one page is defined or the other file is unreachable.  
     - -1 if labels or file paths are incorrect but still basically work with minor fixes.  
     - -1 if they implement multi-page navigation in a different but valid way (no st.Page) and it is noticeably more brittle or confusing.

2. #### 0_salon_app.py sets up navigation with st.navigation(..., position="top") (or equivalent) and calls .run() so both pages are reachable.
   - 4 points  
     - -2 if navigation exists but does not use the Streamlit navigation API as intended (e.g., manual if/else, but both pages still reachable).  
     - -1 if position is not “top” but navigation is otherwise correct.  
     - -1 if .run() (or equivalent call) is missing and only one page executes without manual code changes.

3. #### db_setup_and_helpers.py is correctly configured to use Supabase (USE_SUPABASE = True), connects to the Supabase PostgreSQL database, and creates/populates the tables.
   - 5 points  
     - -5 if USE_SUPABASE is set to False (or Supabase is clearly not being used) — students can “skip this part” but they lose all 5 points.  
     - -3 if USE_SUPABASE is True but database setup fails due to incorrect credentials or connection string and nothing works with Supabase.  
     - -2 if tables exist but are not fully populated or have obvious structural issues coming from misconfigured Supabase settings.

4. #### 1_check_in.py correctly uses st.session_state (e.g., current_view) and st.rerun() to manage multi-view flow between the different screens.
   - 6 points  
     - -3 if current_view (or equivalent) is used but logic is fragile (e.g., views sometimes get stuck or flow is inconsistent).  
     - -2 if they manage multiple views without current_view, but with clearly working alternative session_state logic.  
     - -2 if they never call st.rerun() and rely on brittle workarounds that mostly work but cause odd behavior.  
     - -6 if there is effectively only a single view and the flow is not implemented as separate screens.

5. #### 1_check_in.py implements the “enter phone number” view: shows instructions, collects phone number via a form, validates using clean_phone_number (or equivalent), and shows an error without changing views when invalid.
   - 8 points  
     - -3 if phone number is collected but not validated (any input progresses).  
     - -3 if invalid phone numbers show an error, but the view still advances (i.e., they leave the enter-phone-number screen).  
     - -2 if they do not use clean_phone_number but implement clearly equivalent validation (must enforce 10 digits).  
     - -1 for minor UX issues (missing instructions text or missing “10 digits” requirement text).

6. #### 1_check_in.py, on valid phone input, correctly branches: stores phone/customer in session_state, looks up existing customers (e.g., get_customer_if_exists), and sets current_view to either “new customer” or “select options”, then reruns.
   - 8 points  
     - -4 if branch to new vs existing customer is incorrect or inconsistent (e.g., treating existing customer as new or vice versa).  
     - -2 if they do not store the phone/customer in session_state but still manage to get later steps working through more fragile logic.  
     - -2 if st.rerun() is missing and they rely on nested if/else within a single run to show multiple screens, but behavior still basically works.

7. #### 1_check_in.py implements the “new customer” view: collects first name, last name, and gender in a form, creates a new Customer row in the database using the stored phone number, stores the customer object in session_state, and moves to the “select options” view.
   - 8 points  
     - -4 if customer row is never actually created in the database (e.g., only stored in memory).  
     - -2 if phone number used in Customer.create is not the one from the original view (or they force users to enter it again).  
     - -2 if gender is not captured or stored.  
     - -2 if they do not store the new customer in session_state but manage to refetch it later in a reliable way.  
     - -3 if current_view is not updated correctly and the flow fails to move to “select options”.

8. #### 1_check_in.py implements the “select options” view for both new and returning customers: shows customer message, loads stylists and hairstyles, pre-selects previous stylist/hairstyle for returning customers, leaves selections empty for new customers, and stores chosen stylist and hairstyle in session_state.
   - 12 points  
     - -3 if customer message (get_customer_message or equivalent) is not displayed.  
     - -3 if hairstyles/stylists are not loaded from get_all_stylists / hairstyles_dict (or equivalent data source) and instead are hard-coded or incomplete.  
     - -4 if returning customers do not see their previous stylist/hairstyle preselected.  
     - -3 if new customers see preselected values instead of blank/None default.  
     - -3 if chosen stylist and/or hairstyle are not stored reliably in session_state for later use.  
     - -2 if they implement a different but functional selection component (e.g., radio buttons) instead of selectbox.

9. #### 1_check_in.py implements the “getting haircut” view: calls pretend_to_get_a_haircut (or equivalent progress bar behavior), then transitions to the “check out” view.
   - 3 points  
     - -2 if progress / “getting haircut” feedback is missing but they still jump straight to check-out correctly.  
     - -1 if they call pretend_to_get_a_haircut but do not update current_view afterward.  
     - -3 if this view is missing entirely and they go directly from selection to check-out.

10. #### 1_check_in.py implements the “check out” view: thanks the customer by first name, collects satisfaction (Yes/No mapped to True/False), creates a new Appointment row with correct fields (including price from hairstyles_dict and correct c_id and s_id), and returns to the original phone number view.
   - 12 points  
     - -3 if thank-you message does not use the customer’s first name.  
     - -4 if satisfaction is not mapped to a boolean or is not stored in the appointment (a_satisfied incorrect).  
     - -4 if Appointment.create is missing required information (e.g., wrong or missing c_id, s_id, haircut type, or payment).  
     - -2 if they do not use hairstyles_dict to determine price but instead hard-code or omit payment.  
     - -3 if the app does not reset back to the enter phone number view after creating the appointment.  
     - -2 if date/time is not set to “now” (datetime.today or equivalent) but is still a valid datetime.

11. #### 2_manager_tools.py displays “Manager Tools” heading, a “Choose an option:” subheading, and a selectbox with exactly the two options: “View satisfaction rate by stylist” and “Terminate a stylist” (with no default selection).
   - 4 points  
     - -2 if either the heading or “Choose an option” text is missing.  
     - -1 if the selectbox options are slightly mislabeled but clearly correspond to the two required features.  
     - -1 if there is a default selection instead of index=None behavior (or equivalent).  
     - -4 if there is no unified manager tools UI and the two features are separated into unrelated controls.

12. #### 2_manager_tools.py correctly implements “View satisfaction rate by stylist”: when selected, shows the dataframe returned by get_manager_tools_df().
   - 7 points  
     - -4 if it does not call get_manager_tools_df() and instead shows some unrelated or incorrect data.  
     - -3 if the dataframe is not displayed properly (e.g., it’s transformed into something incomplete or not readable).  
     - -2 if the correct dataframe is only shown after some unnecessary extra click or action beyond selecting the option.

13. #### 2_manager_tools.py correctly implements “Terminate a stylist”: shows stylists in a selectbox (via get_all_stylists), deletes the selected stylist with delete_instance(), shows the termination message, pauses briefly, and reruns so the stylist disappears from the list.
   - 10 points  
     - -3 if get_all_stylists() is not used but stylists are pulled via a custom query that still correctly lists all stylists.  
     - -3 if delete_instance() is not used but an equivalent correct deletion is performed.  
     - -2 if the termination message is missing or incomplete (e.g., missing first/last name).  
     - -2 if time.sleep(1.5) is missing but st.rerun() still correctly refreshes the page.  
     - -3 if stylist is “deleted” only visually (e.g., filtered out) but not actually removed from the database.

14. #### App is hosted on Streamlit Community Cloud and the working URL is pasted into past_your_url_here.txt.
   - 7 points  
     - -7 if the app is not hosted at all or the provided URL is clearly invalid/non-working.  
     - -4 if the app is hosted but the URL is missing from past_your_url_here.txt.  
     - -3 if the app generally works but has obvious deployment-related issues (e.g., missing requirements, secrets misconfigured) that would require non-trivial fixes before a normal user could use it.