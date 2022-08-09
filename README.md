# swagger-PetStore-api-testing
Sela repo Project for Api Testing

PetShopApi Project tests APIs on PetStore Swagger

At PetShopApi folder you will find:

1.PetStoreApi -  contain the python api for the swagger

https://github.com/DayanShay/swagger-api-testing/tree/petshop/PetShopApi/PetStoreApi

2.PetStoreTests - contain the pytest sqript testing for the api

https://github.com/DayanShay/swagger-api-testing/tree/petshop/PetShopApi/PetStoreTests

3.Pet_Models - contain the python moduls for the tests

https://github.com/DayanShay/swagger-api-testing/tree/petshop/PetShopApi/Pet_Models

How to Run on cmd - by defalt url of the Swagger. make sure to copy the full path to the tests file.

``` pytest "FullPath"\PetShopApi\PetStoreTests\test_petstpreApi.py ```

How to Run on cmd - On your One Swaager. 

"YourURL" = Your local Swager 

``` pytest --url "YourURL" ."FullPath"\PetShopApi\PetStoreTests\test_petstpreApi.py ```

Need to have

allure install
And JAVA_HOME
To run Allure Report

1.``` pytest --alluredir=PetStoreReports\ ."FullPath"\PetShopApi\PetStoreTests\test_petstpreApi.py ```

2.``` allure serve ."FullPath"\PetShopApi\PetStoreReports ```

exemple :

![image](https://user-images.githubusercontent.com/108628136/183497574-c04a6022-2e73-4a88-ae0b-6f0201dd23e9.png)

