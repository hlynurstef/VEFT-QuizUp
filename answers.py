""" ANSWERS """

ANSWERS = {
    "Which of the following is generally considered to have defined the REST concept?":
        "Roy Fielding",
    "A full-blown REST service has the following characteristics, except for one. Which one is NOT considered one of the main characteristics of a REST service?":
        "JSON data format",
    "A web service with a single URL which only accepts a HTTP POST request, receives input on XML format and returns XML is probably a:":
        "SOAP service"
}

"""
    'A REST service for a Learning Management System has received a HTTP POST request, to create a new instance of a course. What is the most logical status code returned from the service, assuming the course instance can be properly created?': 
        '201',
    'What is the preferred method when requesting data in a given format from a web service?':
        'Specify the content-type in the "Accept" HTTP header: Accept: application/json',
    'Assume we want to support the given URL in our Web API:\n'+
    '/api/courses/123/assignments/234\n'+
    'Where 123 is the integer ID of the course in question, and 234 is the integer ID of a given assignment in that course.\n'+
    'What is the MOST correct way - using Attribute routing - to decorate a method in a Web API Controller such that it supports this URL?':
        'Route["/api/courses/{courseID:int}/assignments/{assignmentID:int}"]',
    'What is the proper status code for a endpoint that handles HTTP DELETE requests?':
        '204',
    'Which of the following is NOT among the methods used for versioning of Web APIs?':
        'Adding the version to a cookie. Example: "Version: v1"',
    'If an ASP.NET Core Web API application wants to ensure that the response to a given request will contain status code 200, which of the following methods will do that?':
        'All other options are correct',
    'What would be the correct status code returned from an API method, if the client issues a request for /api/courses/9999, but there is no course with ID = 9999?':
        '404',
    'Under what circumstances should an API method return HTTP status code 401?': 
        'When the client has not provided any authentication data, but the method requires it',
    'A DTO class (Data Transfer Object) is a class which:': 
        'is used to pass data from the web service to its clients',
    'Entity objects are classes which:': 
        'map to database tables',
    'Which of the following most correctly describes a service provider class?': 
        'contains the application business logic',
    'What support for different MIME types does ASP.NET Core Web API provide?':
        'It can return both JSON and XML, and allows adding support for other types (CSV, iCal, etc.) via custom formatters',
    'Which of the following LINQ methods will return a single item in a collection/table, null if no item is found, but will throw an exception if more than one is found?':
        'SingleOrDefault()',
    'Which of the following LINQ methods will NOT materialize a query?': 
        'OrderBy()',
    '_courses is a variable of type IRepository. What meaning does the "I" in the beginning of the type IRepository have?': 
        'It indicates that the type IRepository is an interface',
    'AutoMapper is created to solve a particular problem. Which one?': 
        'It simplifies mapping between entity classes and DTO classes',
    'What is the purpose of the attribute [TestInitialize] ?':
        'It means that the method that is decorated with this attribute will run before each unit test',
    'Which LINQ keyword can help us implementing a query which uses LEFT JOIN?':
        'into',
    'When implementing paging in ASP.NET Web API using the Entity Framework, two particular LINQ methods can help us to load a given page from a large list of items. Which two methods are those?':
        'Skip() / Take()',
    'When a HTTP request is issued to a web service, which method should be used to indicate what (human) language the response is preferred to be in (if applicable)?':
        'Add an "Accept-Language" HTTP header to the request',
    'The main purpose of a unit test is to:':
        'Test business logic',
    'For a unit test method to be recognized as such by MSTest, it must meet certain qualifications. Which one?':
        'The method must be marked with the [TestMethod] attribute',
    'What should happen in the "Arrange" section in a unit test?':
        'It should set up the necessary test data',
    'What should happen in the "Act" section in a unit test?':
        'It should call the method being tested',
    'What should happen in the "Assert" section in a unit test?':
        'It should check that the result of calling a given method in the system under test meets the expectations',
    'Why would we want to make us of caching in our web services?':
        'To make our webservice faster',
    'To ensure that a method is properly tested, we need to:':
        'a), b) and c)',
    'One of the following statements about Node.js is wrong. Which one?':
        'Node.js programs run in the browser',
    'Express provides various services to make it easier to write web applications. Below is a list of various services, Express implements one of those (without the use of any plugins). Which one?':
        'Routing',
    'In ES6, arrow functions differ from regular functions. Which one of the differences listed below is correct?':
        'The "this" keyword has different meaning in arrow functions than in regular functions',
    'What is the difference between the keywords "var" and "let" in ES6?':
        '"var" uses function scope, but "let" uses block scope',
    'We can tell Express to use middleware in our apps. Assuming that "app" is our Express app, and "m" is a reference to our middleware (either 3rd party or our own). How is that middleware registered?':
        'app.use(m)',
    'Assume we´ve got an Express app with a route that should return HTTP Status code 412 under a given circumstances. Which of the methods below will do that?':
        'res.status(412);',
    'What service does Mongoose provide us, which is not provided out of the box by MongoDB?':
        'Schema definitions and validation',
    'When using RabbitMQ, what do we call the code which receives messages from a message queue?':
        'Consumer'
}
"""
