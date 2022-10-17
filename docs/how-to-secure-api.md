# How the API is Secured

The application is secured using jwt, or `json web tokens`. Communicating to the api that you are authorized occurs in two ways, differing on whether you're manually making requests or trying to access pages that require authentication.

**Getting Authorized**
Getting authorized is the basic process of recieving a jwt token and storing it in your browser. This is done when you successfully send the correct credentials to login route, `/api/auth/login`. This route is looking to recieve form data with two key/value pairs, "username", which holds the users email, and "password" which holds the user's password. 

**Making Authorized Requests**
The majority of the routes in this category are going to be prefixed with `/api`. You can tell specifically by looking at the route, it will have this argument ` current_user: int = Depends(oauth2.get_current_user)`, meaning that the route depends on an authorized user and won't function without one. Oauth2 is doing most of the heavy lifting in this case. It checks the request's Header for a particualr key/value pair. The key it is searching for is `Authorization`, and the value is the token type (bearer) and the actual token, `Bearer {my.jwt.token}`. This form of authorization applies to all create, update, and delete nodes. 

**Navigating to Authorized Webpages**
All of the routes in this category will have no prefix `/`, as they are user interface routes. All of the routes that require authorization will have the decorator function `@oauth2.auth_required`. This function take a look at the request's cookies, particularly with the key `Authorization`, which stores the users looking for jwt token. If a jwt token is not found or has expired, the user is forwarded to signin page. A cookie is used in this case because it persists across all requests.

