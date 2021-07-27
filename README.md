# Django_stock_app

Project contains two apps:

1. home
  That app have functionality login/logout. After login, user is directed to stock_app. For purposes of testing (there were no requirements to do creating of users) you can use kamil/kamil.
2. stock_app
  This app have query form with TextChoice company name of stock, start date, end date and submit button.
  As a result of submit button table with information about chosen company is presented (from start date to end date). Table contains columns - Date, Start Price, Max Price, Min Price, Close Price, Volume. If query returns no data (for eg. we have no data from period selected by user) special message is displayed. Messages are also displayed when query form is invalid (for eg. when start date is earlier than end date).

Data about stock company is in database 'stock_db', data was downloaded from https://stooq.pl/. I chose data for Allegro, Cd Project and PKN Orlen.
