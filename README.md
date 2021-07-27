# Django_stock_app

Project contain two apps.

1. home
  That app have functionality login/logout. After login, user direction to stock_app.
2. stock_app
  Have form with TextChoice company name of stock, start date, end date and submit button.
  This form generate table with information about choose company from start date to end date. Table columnes containe( Date, Sart Pirice, Max, Price, Min Price,      Close Price, Volume) 

Data about stock company are in datebase 'stock_db', there was downlowde from https://stooq.pl/. Stock choose to app are Allegre, Cd Priject and PKN Orlen.
