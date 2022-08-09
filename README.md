# swagger-BookStore-api-testing
Sela repo Project for Api Testing 
BookStoreApi Project tests APIs on BookStore Swagger

At BookStoreApi folder  you will find:

1.BookStoreTests - contain the pytest sqript testing for the api

https://github.com/DayanShay/swagger-api-testing/tree/bookstore/BookStoreApi/BookStoreTests

2.BookStore_Api - contain the python api for the swagger

https://github.com/DayanShay/swagger-api-testing/tree/bookstore/BookStoreApi/BookStore_Api

3.Book_Models - contain the python moduls for the tests

https://github.com/DayanShay/swagger-api-testing/tree/bookstore/BookStoreApi/Book_Models


How to Run on cmd - by defalt url of the Swagger.
make sure to copy the full path to the tests file.

``` pytest "FullPath"\BookStoreApi\BookStoreTests\tests_bookstore.py ```

How to Run on cmd - On your One Swaager.

"YourURL" = Your local Swager 

``` pytest --url "YourURL" .\"FullPath"\BookStoreApi\BookStoreTests\tests_bookstore.py ```

Need to have
1. allure install
2. And JAVA_HOME

To run Allure Report 

1.``` pytest --alluredir=BookStoreReports\ .\"FullPath"\BookStoreApi\BookStoreTests\tests_bookstore.py ```


2.``` allure serve .\"FullPath"\BookStoreApi\BookStoreReports ```

exemple :

![image](https://user-images.githubusercontent.com/108628136/183494961-fb233df9-ded7-444e-acba-a064dc5df7ef.png)
=======
# Swagger
Sela project API testing - PetStore and BookStore
>>>>>>> 9a15cb8 (Initial commit)
