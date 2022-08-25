# swagger-BookStore-api-testing
Sela repo Project for Api Testing 
BookStoreApi Project tests APIs on BookStore Swagger

At BookStoreApi folder  you will find:

1.BookStoreTests - contain the pytest script testing for the api

https://github.com/DayanShay/swagger-api-testing/tree/bookstore/Book_StoreApi/BookStoreTests

2.BookStore_Api - contain the python api for the swagger

https://github.com/DayanShay/swagger-api-testing/tree/bookstore/Book_StoreApi/BookStore_Api

3.Book_Models - contain the python moduls for the tests

https://github.com/DayanShay/swagger-api-testing/tree/bookstore/Book_StoreApi/Book_Models

Install requirements

"FullPath" < - insert full path to requirements.txt file.

```commandline
pip install -r .\Book_StoreApi\requirements.txt 
```

How to Run on cmd - by defalt url of the Swagger.
make sure to copy the full path to the tests file.

``` pytest "FullPath"\Book_StoreApi\BookStoreTests\tests_bookstore.py ```

How to Run on cmd - On your own Swaager.

"YourURL" = Your local Swager 

``` pytest --url "YourURL" .\"FullPath"\Book_StoreApi\BookStoreTests\tests_bookstore.py ```

Need to have
1. allure install
2. And JAVA_HOME

To run Allure Report 

1.``` pytest --alluredir=BookStoreReports\ .\"FullPath"\Book_StoreApi\BookStoreTests\tests_bookstore.py ```


2.``` allure serve .\"FullPath"\Book_StoreApi\BookStoreReports ```

exemple :

![image](https://user-images.githubusercontent.com/108628136/183494961-fb233df9-ded7-444e-acba-a064dc5df7ef.png)
