# serach_products_api

Cirst create virualenv
then please install requirered modules with
"pip install requirements.txt"
then create a super user account to access admin console.
run 
"python manage.py makemigrations"
 and  
"python manage.py migrate" commands to create database tables.

then loin to admin and goto  "http://127.0.0.1:8000/admin/food_sales/order_detail/" 
click on "import"  to upload xls data provided in the GitHub as "FoodSales_Sample.xlsx".
to export data goto http://127.0.0.1:8000/admin/food_sales/order_detail/export/? and select format as "xlsx" and click on submit to download xlsx file.

now to search product with GET request use this api to search prodct name with "chocolate"
http://127.0.0.1:8000/api/orders/?search=Chocolate
