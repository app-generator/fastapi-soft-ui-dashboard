# How manage products via API
- All of the products routes live in the same router. The url is prefixed with `/api/products`.


How to:
## Nonauthentication-Required Routes
- All of the routes in this category are open to the public. 

**Get ->**
The route used to get one product is named `get_product.` This route expects to recieve a product id (integer) in the url.

**Get All ->**
The route used to update a product is named `get_products.` This route will return all products, and an empty list if there are none. 


## Authenticaion-Required Routes
- All of the routes in this category require for the user to be authenticated. For more information on user authentication, see the `/docs/how-to-secure-api` documentation.

**Create ->** 
The route used to create a product is named `create_product`. This route expects to recieve raw json. The exact data required and corresponding types allowed can be seen in `/src/schemas.py`, under the class ProductBase.

**Update ->**
The route used to update a product is named `update_product.` This route expects to recieve a product id (integer) in the url, as raw as json, specifying which column needs to be changed. The exact data required and corresponding types allowed can be seen in `/src/schemas.py`, under the class ProductBase.

**Delete ->**
The route used to delete one product is named `delete_product.` This route expects to recieve a product id (integer) in the url. 
