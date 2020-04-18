# Facebook-API-Integration-Webhook
This will help to integrate bot for a page into facebook page messenger and facebook page wall.

Facebook API Integration using Webhook

### •   Step 1: Create a page.

1.  Create a page on Facebook.
2.  And note down that page id. Now this page id will act as BOT_ID.
3.  Find this Facebook page id in page information section which is unique to every page.

### •   Step 2: Create an app.

1.  Login to https://developers.facebook.com and login.
2.  Create an app in developer account. Enter app name.

### •   Step 3: Setup webhook app.

1.  Run facebook.py file in one command prompt.
2.  Now your code is running on http://127.0.0.1:65000 URL because I fixed 65000 port in code itself.
3.  Now task is to convert http to https request, and this is because your code always should be reachable to Facebook for handshake.
4.  Facebook will perform handshake (to hit that URL to check whether code is reachable or not) with your code every 20 seconds, until a 200 OK response received.
5.  Click on setup webhooks. (See Documentation).
6. - Choose “Page” and “Permissions” in tab and subscribe those objects (Highlighted in Red in below Image).
   - After Clicking on “Subscribe to this object” paste our https URL appending “/facebook/webhook” in “Callback URL” section and put “check1234” as “Verify Token”.
   - Click on “Verify and Save”. (See Documentation).
7.  - In “Page” subscribe to “feed”.
    - In “Permissions” subscribe to “pages_messaging” and “read_page_mailboxes”.

### •   Step 4: Setup messenger app.

1.  Setup Messenger. (See Documentation).
2.  Select “Add or Remove Pages”. And select page which will act as BOT. (See Documentation).
3.  Once you selected page then allow with your account. And then generate token which is a Page Access Token which we want in config.py.
4.  Paste this token in config.py file.
5.  Now you have PAGE_ACCESS_TOKEN, BOT_ID paste this info into the config.py.

### •   Step 5: Make app public.

1.  Click on “in development”. And complete all necessary information. (See Documentation).
2.  Bingo now your messenger chatbot is ready.
