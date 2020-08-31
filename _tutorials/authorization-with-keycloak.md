---
title: "How to use Keycloak to provide authorization services to your application"
description: "This tutorial describes how to leverage Keycloak to offload the authorization tasks in our applications"
last_update: "2020-07-18"
published: false
---
# How to use Keycloak to perform authorization services for your application
###### Last Updated: {{ page.last_update | date: "%A, %B %d, %Y" }}


==========================================
How to use Keycloak to provide authorization services to your application
==========================================

.. |f| replace:: *FastAPI*
.. _f: https://fastapi.tiangolo.com/

.. |g| replace:: *Grafana*
.. _g: https://grafana.com/

.. |k| replace:: *Keycloack*
.. _k: https://www.keycloak.org/

.. |n| replace:: *Nginx*
.. _n: https://www.nginx.com/

.. |o| replace:: *Oauth2-Proxy*
.. _o: https://oauth2-proxy.github.io/oauth2-proxy/

.. |p| replace:: *Prometheus*
.. _p: https://prometheus.io/

.. |r| replace:: *Requests*
.. _r: https://requests.readthedocs.io/en/master/

.. |t| replace:: *Typer*
.. _t: https://typer.tiangolo.com/

*Author*: Antonello Izzi (antonello.izzi@konikaminolta.cz)

*Last Modified*: 06/08/2020

------------
Introduction
------------

When it comes to access management, there are two main concepts to consider:

**Authentication**
    Refers to the process of confirming identity. It it used to verify that the user is who she claims to be.

**Authorization**
    Refers to the process of verifying that the user has access to a resource, or can perform an specific action. Usually, authorization occurs after identity is successfully validated through *authentication*.

In the tutorial :ref:`authentication-tutorial` we have explored how to use |k|_ to perform *authentication*. In this tutorial we are going to explore how to use it to perform *authorization*.

|k|_ supports several access control mechanism, as detailed on the `Authorization Services Guide <https://www.keycloak.org/docs/latest/authorization_services/#_overview_architecture>`_ page. In this tutorial we will focus on the **Role-based access control (RBAC)** one.

In this tutorial we will leverage part of the infrastructure we built for :ref:`authentication-tutorial`:

* ``keycloak.vas.cz`` VM hosts the |k|_ application
* ``oauth.vas.cz`` VM hosts the authentication proxy
* ``nginx.vas.cz`` VM hosts the reverse proxy

In addition, we will develop a simple client-server backend in Python to test the authentication, with the help of |f|_ and |t|_:

* ``fastapi.vas.cz`` VM hosts our *test application* backend

--------
Concepts
-------- 

Before to proceed, let's clarify some concepts.

The authorization process in |k|_ is based on three steps:

* Resource Management 
* Permission and Policy Management 
* Policy Enforcement 

Resource Management 
===================
In this phase you'll specify in |k|_ *what are you looking to protect*, using the Keycloak Administration Console. There you can enable any registered client application as a resource server and start managing the resources and scopes you want to protect. Scopes usually represent the actions that can be performed on a resource, but they are not limited to that. You can also use scopes to represent one or more attributes.

Permission and Policy Management 
================================
Once you have defined your resource servers and all the resources you want to protect, you must set up permissions and policies.

Policies define the conditions that must be satisfied to access or perform operations on something, but they are not tied to what they are protecting.

Permissions are coupled with the resource they are protecting. Here you specify what you want to protect (resource or scope) and the policies that must be satisfied to grant or deny permission.

Policy Enforcement
==================
Policy Enforcement involves the necessary steps to actually enforce authorization decisions to a resource server. This is achieved by enabling a **Policy Enforcement Point (PEP)** at the resource server that is capable of communicating with the authorization server, ask for authorization data and control access to protected resources based on the decisions and permissions returned by the server.

For more details, read the *Overview* section of the |k|_ `Authorization Services Guide <https://www.keycloak.org/docs/latest/authorization_services/#_overview_architecture>`_.

---------------------
Create the API Server
---------------------

Create a new VM and assign it to the following hostname/ip address::

    192.168.56.9	fastapi fastapi.vas.cz

Verify that ``Python`` is installed::

    $ python3
    Python 3.6.9 (default, Jul 17 2020, 12:50:27)
    [GCC 8.4.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> quit    

Install pip3::

    $ sudo apt install python3-pip

    $ alias pip=pip3

Install Fastapi::

    $ pip3 install fastapi[all]

    $ pip3 install uvicorn

    $ mkdir tutorial03

    $ cd tutorial03

---------------------------
Define the tutorial's scope
---------------------------

My purpose in this tutorial is to test and validate authorization options using Keycloak. This is how I plan to do it:

1. Create an API server with two endpoints:
    - */read*, accessible to all users, will provide the value of a variable
    - */write*, accessible only to administrators, will modify the value of the same variable

2. Create two users in Keycloack:
    - *Alice* with the *updater* role 
    - *Bob* with the *operator* role

3. Place the API server behind |n|_ and use |o|_ to provide for Authentication of *Alice* and *Bob*

4. Leverage the Authorization capabilities of Keycloak to verify that *Alice* can access both endpoints, while *Bob* is denied access to */write*

---------------------
Create the API server 
---------------------

On ``fastapi`` host create the following ``main.py`` file

.. code-block:: python

    from fastapi import FastAPI

    app = FastAPI()

    class message():
        text = "This is the default message"

        def set_message(self, new_message: str = ""):
            self.text = new_message

        def get_message(self):
            return self.text

    app_message = message()

    @app.get("/")
    async def root():
        return {"message": "Welcome to VAS API server"}

    @app.get("/read")
    async def read_message():
        return {"message": app_message.get_message()}

    @app.get("/write/{new_message}")
    async def write_message(new_message: str = ""):
        app_message.set_message(new_message)
        return {"message updated"}

.. Note::
    The above code has no pretense of being *good code*: I just need something quick and dirty to test authorization, hence the usage of a *get* method to update the message.

Start the uvicorn server with the following command::

    $ uvicorn main:app --host 192.168.56.9 --reload

Now check you can reach the endpoints and get the appropriate answers::

    >curl -X GET "http://192.168.56.9:8000/read" -H  "accept: application/json"
    {"message":"This is the default message"}

    >curl -X GET "http://192.168.56.9:8000/write/this%20is%20the%20new%20message" -H  "accept: application/json"
    ["message updated"]

    >curl -X GET "http://192.168.56.9:8000/read" -H  "accept: application/json"
    {"message":"this is the new message"}

---------------------
Create Keycloak users
---------------------

Now create *Alice* and *Bob* in Keycloak in the ``Tutorial01`` realm we created in the previous tutorial :ref:`authentication-tutorial`. This way we can use the same authentication infrastructure to protect our API server. Remember that we will need to use user's email as userid. The email for the two users will be "alice@example.org" and "bob@example.org".

For them I'll use the passwords "alicepwd" and "bobpwd".

In order to login, both users must be part of the ``admin`` group we defined in the previous tutorial, because that is the group |o|_ will validate against for access.

.. figure:: ../images/tutorial03-01.png
   :name: alice_and_bob

   User's Creation

----------------------------------------
Enable Authentication for the API Server
----------------------------------------

On ``nginx`` server edit the ``/etc/nginx/sites-available/default`` file and add a location for your API server::

    location /fastapi/ {
            auth_request /oauth2/auth;
            error_page 401 = /oauth2/sign_in;

            # pass information about the user to the backend
            # requires oauth2-proxy to run with --set-xauthrequest flag
            auth_request_set $user $upstream_http_x_auth_request_preferred_username;
            auth_request_set $email $upstream_http_x_auth_request_email;
            auth_request_set $name $upstream_http_x_auth_request_user;

            proxy_set_header X-Username $email;

            proxy_pass http://fastapi.vas.cz:8000/;
    }

Now on ``oauth`` server start the |o|_ proxy::

    $ ./oauth2/oauth2-proxy --provider=keycloak --client-id=oauth2 --client-secret=0e7fc0a2-0ed5-4147-8ce5-dd479b90c445 --login-url="http://keycloak.vas.cz:8080/auth/realms/tutorial01/protocol/openid-connect/auth" --redeem-url="http://keycloak.vas.cz:8080/auth/realms/tutorial01/protocol/openid-connect/token" --validate-url="http://keycloak.vas.cz:8080/auth/realms/tutorial01/protocol/openid-connect/userinfo" --keycloak-group=/admin --email-domain=* --cookie-secret=1234567890123456 --http-address="http://192.168.56.8:4180" --scope=openid --set-xauthrequest=true

Now open a browser window and navigate to ``https://nginx/fastapi/``: you should be redirected to the |k|_ login page. Verify you can login with both *Alice* and *Bob* credentials. You should be able to read and change the user message with both users.

.. note::
    I suggest to use a private browsing window, so that you will not retain any cookies betwee tests.

-----------------------------
Enable Authorization Services
-----------------------------

On the |k|_ ``Administration Console`` edit the ``Oauth2`` client and activate the ``Authorization Enabled`` switch.

.. figure:: ../images/tutorial03-02.png
   :name: authorization_enabled

   Authorization Enabled

This will activate a new ``Authorization`` tab for the client, where we can define our fine grained authorization policies.

.. figure:: ../images/tutorial03-04.png
   :name: authorization_settings

   Authorization Settings


Start by creating the scope ``message:update``.

.. figure:: ../images/tutorial03-03.png
   :name: authorization_scope

   Authorization Scope

Create a resource to protect the ``/fastapi/write/`` endpoint.

.. figure:: ../images/tutorial03-05.png
   :name: authorization_resource

   Resource Creation

Now create the *updater* role for the user *Alice*

.. figure:: ../images/tutorial03-06.png
   :name: updater_role

   Updater Role

.. figure:: ../images/tutorial03-07.png
   :name: updater_role_assignment

   Updater Role Assignment

.. figure:: ../images/tutorial03-08.png
   :name: updater_role_assignment_verification

   Updater Role Assigned

Now create the policy to enforce for updating a message

.. figure:: ../images/tutorial03-09.png
   :name: create_policy

   Message Updating Policy

Finally, create a resource permission to protect the resource

.. figure:: ../images/tutorial03-10.png
   :name: create_permission

   Message Update Permission

You can use the ``Evaluate`` tab to verify that *Bob* gets denied access to the ``fastapi-writ-message`` resource.

---------------------------
Validate User Authorization
---------------------------

Now we need to validate user's authorization. |k|_ handles for us the authentication part, providing the user with the session cookie ``_oauth2_proxy`` and an ``access token``: we can use this token to validate user's authorization.

First of all, we must pass the access token provided by |k|_ upstream from |o|_. In order to do this, we need to enable the following parameters in |o|_ configuration:

* pass-access-token = true

::

    $ ./oauth2/oauth2-proxy --provider=keycloak --client-id=oauth2 --client-secret=0e7fc0a2-0ed5-4147-8ce5-dd479b90c445 --login-url="http://keycloak.vas.cz:8080/auth/realms/tutorial01/protocol/openid-connect/auth" --redeem-url="http://keycloak.vas.cz:8080/auth/realms/tutorial01/protocol/openid-connect/token" --validate-url="http://keycloak.vas.cz:8080/auth/realms/tutorial01/protocol/openid-connect/userinfo" --keycloak-group=/admin --email-domain=* --cookie-secret=1234567890123456 --http-address="http://192.168.56.8:4180" --scope=openid --set-xauthrequest=true --pass-access-token=true

Next, modify |n|_ configuration to pass it upstream::

    location /fastapi/ {
            auth_request /oauth2/auth;
            error_page 401 = /oauth2/sign_in;

            # pass information about the user to the backend
            # requires oauth2-proxy to run with --set-xauthrequest flag
            auth_request_set $user $upstream_http_x_auth_request_preferred_username;
            auth_request_set $email $upstream_http_x_auth_request_email;
            auth_request_set $name $upstream_http_x_auth_request_user;

            # pass OAuth access_token to the backend
            # requires oauth2-proxy to run with --pass-access-token --set-authorization-header --pass-authorization-header flag
            auth_request_set $access_token $upstream_http_x_auth_request_access_token;

            proxy_set_header X-Username $email;
            proxy_set_header X-Access-Token $access_token;

            proxy_pass http://fastapi.vas.cz:8000/;
    }

Now, we can access the access token and use it to validate our user.

In order to interact with the Keycloak APIs, let's install the |r|_ module::

    $ pip3 install requests

and modify `main.py` in the following way::

    from fastapi import FastAPI, Cookie, Header
    from typing import Optional
    import functools
    import requests
    import base64
    import json

    app = FastAPI()

    class message():
        text = "This is the default message"

        def set_message(self, new_message: str = ""):
            self.text = new_message

        def get_message(self):
            return self.text

    app_message = message()

    # Decorator function to provide authorization capabilities to endpoints
    def check_authorization(resource="", scope=""):
        def authorize(func):
            """ The code outlined here is directly derived from the Keycloak Authorization Services Guide web page:
                https://www.keycloak.org/docs/latest/authorization_services/ """

            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                # Retrieve session cookie and access token from parameters
                cookie = kwargs["_oauth2_proxy"]
                access_token = kwargs["x_access_token"]

                # Define Keycloak related variables
                server_url = "http://keycloak.vas.cz:8080"
                realm = "tutorial01"
                client_id="oauth2"
                client_secret_key="0e7fc0a2-0ed5-4147-8ce5-dd479b90c445"

                # Discovering authorization services endpoints and metadata
                url = f"{server_url}/auth/realms/{realm}/.well-known/uma2-configuration"
                endpoints = requests.get(url).json()
                token_endpoint = endpoints["token_endpoint"]
                issuer_endpoint = endpoints["issuer"]
                token_introspection_endpoint = endpoints["token_introspection_endpoint"]

                ## Retrieving the Keyclock public key (not needed for tutorial's scope)
                ## It was used during the tests and I decided to left it here for documentation
                #issuer_info = requests.get(issuer_endpoint).json()
                #public_key = issuer_info["public_key"]
                #public_key = f"-----BEGIN PUBLIC KEY-----\n{public_key}\n-----END PUBLIC KEY-----"

                # Retrieve access token's details
                parameters = {"client_id": client_id
                            ,"token": access_token
                            ,"client_secret": client_secret_key}
                introspection = requests.post(token_introspection_endpoint, data=parameters)

                # Verify if the user is authorized to the specific action
                parameters = {"grant_type" : "urn:ietf:params:oauth:grant-type:uma-ticket"
                            ,"permission": f"{resource}#{scope}"
                            ,"audience": "oauth2"
                            #,"response_mode": "permissions" # Provide permission's details
                            ,"response_mode": "decision"     # Provide permission's summary
                            }
                headers = {"Authorization": f"Bearer {access_token}"}
                permission = requests.post(token_endpoint, data=parameters, headers=headers)

                # Check the permission and execute accordingly
                if (permission.status_code == 200): # user is authorized to resource and scope
                    status = func(*args, **kwargs)
                else:
                    result = permission.json()
                    error = result["error"]
                    error_description = result["error_description"]
                    status = f"{error}: {error_description}"
                return {"status": status
                        #,"cookie": cookie
                        #,"access_token": access_token
                        #,"access_token_details": introspection.json()
                        #,"permission request status code": permission.status_code
                        #,"permission result": permission.json()
                        #,"endpoints": endpoints
                    }
            return wrapper
        return authorize


    @app.get("/")
    def root():
        return {"message": "Welcome to VAS API server"}

    @app.get("/read")
    def read_message(_oauth2_proxy: Optional[str] = Cookie(None),
                    x_access_token: Optional[str] = Header(None)
                    ):
        return {"message": app_message.get_message()}

    @app.get("/write/{new_message}")
    @check_authorization(resource="fastapi-write-message", scope="message:update")
    def write_message(new_message: str = "",
                    _oauth2_proxy: Optional[str] = Cookie(None),
                    x_access_token: Optional[str] = Header(None)
                    ):
        app_message.set_message(new_message)
        return {"message updated"}

    @app.get("/cookie/")
    def get_auth_cookie(_oauth2_proxy: Optional[str] = Cookie(None)):
        return {"auth_token": _oauth2_proxy}

The code should be quite straightforward, but let's analyze the main parts.

First of all, we wrap the ``write_message`` with the ``check_authorization`` decorator, passing the ``resource`` and ``scope`` that we want to check among with the ``access token`` provided by |k|_ during the login::

    @app.get("/write/{new_message}")
    @check_authorization(resource="fastapi-write-message", scope="message:update")
    def write_message(new_message: str = "",
                    _oauth2_proxy: Optional[str] = Cookie(None),
                    x_access_token: Optional[str] = Header(None)
                    ):
        app_message.set_message(new_message)
        return {"message updated"}

Next, we check the permission inside the decorator::

    # Verify if the user is authorized to the specific action
    parameters = {"grant_type" : "urn:ietf:params:oauth:grant-type:uma-ticket"
                ,"permission": f"{resource}#{scope}"
                ,"audience": "oauth2"
                #,"response_mode": "permissions" # Provide permission's details
                ,"response_mode": "decision"     # Provide permission's summary
                }
    headers = {"Authorization": f"Bearer {access_token}"}
    permission = requests.post(token_endpoint, data=parameters, headers=headers)

The ``permission`` returns a status of ``200`` if the user is authorized and ``403`` if the user is not authorized. We then use this value to proceed with the update request or deny the access::

    # Check the permission and execute accordingly
    if (permission.status_code == 200): # user is authorized to resource and scope
        status = func(*args, **kwargs)
    else:
        result = permission.json()
        error = result["error"]
        error_description = result["error_description"]
        status = f"{error}: {error_description}"
    return {"status": status
            #,"cookie": cookie
            #,"access_token": access_token
            ,"access_token_details": introspection.json()
            #,"permission request status code": permission.status_code
            #,"permission result": permission.json()
            #,"endpoints": endpoints
            }

-----------------
Test the scenario
-----------------
1) Login as ``alice`` and check the value of the message

.. figure:: ../images/tutorial03-11.png
   :name: alice_read

   The default message is there

2) Have ``alice`` modify the message

.. figure:: ../images/tutorial03-12.png
   :name: alice_modify

   Alice successfully change the message

3) Close the browser window and login as Bob. You should get the message modified by Alice.

.. figure:: ../images/tutorial03-13.png
   :name: modified_message

   Bob see the message modified by Alice

4) Now try to change the message as Bob

.. figure:: ../images/tutorial03-14.png
   :name: access_denied

   Bob is denied access to the resource

----------
Conclusion
----------
Although this is just a basic example, missing every real complexity that must be implemented in a real case scenario, we have now a way to offload authentication and authorization duties to |k|_, maintaining very little intelligence in our application and being able to modify access without the need to change the code.