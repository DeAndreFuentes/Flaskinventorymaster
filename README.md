
##To run the project

1- create env in project main directory 

`python3 -m venv env`

2-activate it

`source env/bin/activate`

3. Install requirements

`pip install -r requiremnets.txt`

4.Run the project server

`cd inventory_management/`
`python run.py`

OR set the script in script
configuration
 point your browser at http://0.0.0.0:5000/
 


## Inventory manager

### Acceptance criteria:

- [x] 1. Users must be able to CRUD+S the product table data.

- [x] 2. Deletion is soft-delete only and there must be a way to re-activate soft-deleted items.

- [x] 3. The main product view must be an HTML table that allows you to see all products.

    - [x] 3.1. Products with a value of 100 or lower in the "quantity" column must be highlighted in red.

    - [x] 3.2. Products with a value of 101 to 500 in the "quantity" column must be highlighted in yellow.

    - [x] 3.3. Products with a value of 501 or more in the "quantity" column must either be highlighted in green or the table's default color.

- [x] 4. There must be a separate product view for (soft) deleted items that allows users to re-activate products.

- [x] 5. Your entire app must use bootstrap 4 for its graphical user interface.

- [x] 6. You must submit a link to your GitHub repository that hosts the code.

- [x] 7. Users can submit product reviews that other users may read.

![](/inventory_manager/app/static/img/app1.png)
![](/inventory_manager/app/static/img/app2.png)



You are a full-stack developer working at an e-commerce company. Your company, Duckommerce.com focuses on importing and selling goods that are manufactured abroad which helps keep costs low and profits high. The main issue however is how long things take to reach your warehouse because of the long shipping times, so the procurement department is constantly monitoring items that are low in stock to order them before you run out.

Sales have ramped up this quarter and the procurement department is having trouble tracking all of the different products you sell, so you've been asked to build an in-home software tool that allows them to manage all this data in a database, which will later be synced with other databases your operation relies on.

You must build a product inventory management solution that allows the procurement department to create, read, update, (soft) delete and scan all of the contents of the "product" table which will, through a background process that one of your teammates has already built, constantly synchronize with the main database your online store relies on.

The product table must have at least 8 columns: id (primary key, auto-incremental), name, price, description, category, quantity, unique_tag and active.

Important note: The IT department has made it clear that they will limit access to this application to the procurement department via firewall settings, so it is not necessary to add a login screen for the time being.