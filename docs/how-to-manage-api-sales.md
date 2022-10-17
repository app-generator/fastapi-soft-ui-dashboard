# How manage sales via API
- All of the sales routes live in the same router. The url is prefixed with `/api/sales`.


How to:
## Nonauthentication-Required Routes
- All of the routes in this category are open to the public. 

**Get ->**
The route used to get one sale is named `get_sale.` This route expects to recieve a sale id (integer) in the url.

**Get All ->**
The route used to update a sale is named `get_sales.` This route will return all sales, and an empty list if there are none. 


## Authenticaion-Required Routes
- All of the routes in this category require for the user to be authenticated. For more information on user authentication, see the `/docs/how-to-secure-api` documentation.

**Create ->** 
The route used to create a sale is named `create_sale`. This route expects to recieve raw json. The exact data required and corresponding types allowed can be seen in `/src/schemas.py`, under the class SaleBase.

**Update ->**
The route used to update a sale is named `update_sale.` This route expects to recieve a sale id (integer) in the url, as raw as json, specifying which column needs to be changed. The exact data required and corresponding types allowed can be seen in `/src/schemas.py`, under the class SaleBase.

**Delete ->**
The route used to delete one sale is named `delete_sale.` This route expects to recieve a sale id (integer) in the url. 
