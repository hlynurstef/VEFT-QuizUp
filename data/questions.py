""" QUESTIONS """

QUESTIONS = {
    "Which of the following is generally considered to have defined the REST concept?": [
        "Douglas Crockford",
        "Misko Hevery",
        "Roy Fielding",
        "Leonard Richardsson"
    ],
    "A full-blown REST service has the following characteristics, except for one. Which one is NOT considered one of the main characteristics of a REST service?": [
        "Hypertext driven",
        "Cacheable",
        "JSON data format",
        "Client/Server architecture",
        "Stateless"
    ],
    "A web service with a single URL which only accepts a HTTP POST request, receives input on XML format and returns XML is probably a:": [
        "Ruby on Rails project",
        "SOAP service",
        "Classic ASP project",
        "REST service"
    ],
    'A REST service for a Learning Management System has received a HTTP POST request, to create a new instance of a course. What is the most logical status code returned from the service, assuming the course instance can be properly created?': [
        '200',
        '204',
        '201',
        '404'
    ],
    'What is the preferred method when requesting data in a given format from a web service?': [
        'To put it in the HTTP footer',
        'Specify the content-type in the "Accept" HTTP header: Accept: application/json',
        'To put it in the query string: http://server/api/courses?format=json',
        'To put it in the URL: http://server/api/courses/json',
        'To put it in the body of the HTTP request'
    ],
    'Assume we want to support the given URL in our Web API:\n'+
    '/api/courses/123/assignments/234\n'+
    'Where 123 is the integer ID of the course in question, and 234 is the integer ID of a given assignment in that course.\n'+
    'What is the MOST correct way - using Attribute routing - to decorate a method in a Web API Controller such that it supports this URL?': [
        'Route["/api/courses/{courseID}/assignments/{assignmentID:string}"]',
        'RoutePrefix["/api/courses/123/assignments/234"]',
        'RoutePrefix["/api/courses/{courseID:int}/assignments/{assignmentID:int}"]',
        'Route["/api/courses/{courseID:int}/assignments/{assignmentID:int}"]',
        'RoutePrefix["/api/courses/{courseID:int}/assignments/{assignmentID:string}"]'
    ],
    'What is the proper status code for a endpoint that handles HTTP DELETE requests?': [
        '418',
        '400',
        '204',
        '201'
    ],
    'Which of the following is NOT among the methods used for versioning of Web APIs?': [
        'Adding the version to the MIME type being reqested via the "Accept" header.',
        'Adding a custom header to the request. Example: "api-version: 1"',
        'Adding the version to a cookie. Example: "Version: v1"',
        'Adding the version to the URL. Example: /api/v1/courses'
    ],
    'If an ASP.NET Core Web API application wants to ensure that the response to a given request will contain status code 200, which of the following methods will do that?': [
        'Declare the method as returning an object (or a list of objects), and then return such object(s).',
        'All other options are correct',
        'Use IActionResult, and then return StatusCode(200, obj);',
        'Use IActionResult, and then return new ObjectResult(obj);'
    ],
    'What would be the correct status code returned from an API method, if the client issues a request for /api/courses/9999, but there is no course with ID = 9999?': [
        '204',
        '404',
        '500',
        '400',
        '303'
    ],
    'Under what circumstances should an API method return HTTP status code 401?': [
        'When the client HAS provided authentication data, but the given user doesn´t have permission to perform the given action'
        'When the client has issued a request for a method which doesn´t return any content, such as a DELETE method'
        'When the client has made some unspecified mistake in the request, i.e. could be a missing property value when creating a resource'
        'When the server is a teapot'
        'When the client has not provided any authentication data, but the method requires it'
    ],
    'A DTO class (Data Transfer Object) is a class which:': [
        'is used to pass data from the web service to its clients',
        'is used for validation of input from clients',
        'contains the application business logic',
        'maps to a database table',
        'are used to pass data from clients to the web service'
    ],
    'Entity objects are classes which:': [
        'contain the application business logic',
        'map to database tables',
        'are used to pass data from the web service to its clients',
        'are used for validation of input from clients'
    ],
    'Which of the following most correctly describes a service provider class?': [
        'contains validation attributes on its properties',
        'contains the application business logic',
        'maps to a database table',
        'handles all exceptions in the application and takes care of returning the correct status code'
    ],
    'What support for different MIME types does ASP.NET Core Web API provide?': [
        'It can return both JSON and XML, and allows adding support for other types (CSV, iCal, etc.) via custom formatters',
        'It can return both JSON and XML, but nothing else',
        'It can return only JSON',
        'It can return only XML',
        'It has built in support for all known MIME types in the universe'
    ],
    'Which of the following LINQ methods will return a single item in a collection/table, null if no item is found, but will throw an exception if more than one is found?': [
        'FirstOrDefault()',
        'First()',
        'SingleOrDefault()',
        'Take(1)',
        'Single()'
    ],
    'Which of the following LINQ methods will NOT materialize a query?': [
        'SingleOrDefault()',
        'Count()',
        'ToList()',
        'Min()',
        'OrderBy()'
    ],
    '_courses is a variable of type IRepository. What meaning does the "I" in the beginning of the type IRepository have?': [
        'It means that the type IRepository is a regular poco class',
        'It has no meaning whatsoever',
        'It means that it will be mapped using IAutoMapper',
        'It indicates that the type IRepository is an interface'
    ],
    'AutoMapper is created to solve a particular problem. Which one?': [
        'It allows us to inject dependencies into our application',
        'It simplifies mapping between entity classes and database tables',
        'It simplifies mapping between entity classes and DTO classes',
        'It makes it easier to declare test instances of data in unit tests',
        'It simplifies mapping between the business layer and the Web API layer'
    ],
    'What is the purpose of the attribute [TestInitialize] ?': [
        'It means that a new instance of the class that is decorated with this attribute will be created before each unit test is run',
        'It means that the method that is decorated with this attribute is a unit test',
        'There is no attribute called [TestInitialize]',
        'It means that the method that is decorated with this attribute will run before each unit test'
    ],
    'Which LINQ keyword can help us implementing a query which uses LEFT JOIN?': [
        'into',
        'where',
        'select',
        'equals',
        'orderby'
    ],
    'When implementing paging in ASP.NET Web API using the Entity Framework, two particular LINQ methods can help us to load a given page from a large list of items. Which two methods are those?': [
        'Skip() / Take()',
        'First() / Top()',
        'Skip() / Top()',
        'First() / Next()',
        'First() / Take()'
    ],
    'When a HTTP request is issued to a web service, which method should be used to indicate what (human) language the response is preferred to be in (if applicable)?': [
        'The client has no way to indicate what language is preferred',
        'Add a "lang" parameter to the query string: path/to/web/service?lang=is',
        'Add a JSON object to the request body: { "lang" : "is" }',
        'Add an "Accept-Language" HTTP header to the request',
        'Put the language into the URL: /path/to/web/service/lang/is'
    ],
    'The main purpose of a unit test is to:': [
        'Test business logic',
        'Test that the mapping between entity classes and database tables is correct',
        'Test the integration between all parts of the system, i.e. Web API layer, business logic layer, and database layer',
        'Test routing in the Web API layer',
        'Test DTO and ViewModel classes'
    ],
    'For a unit test method to be recognized as such by MSTest, it must meet certain qualifications. Which one?': [
        'The method must have three sections: Arrange, Act and Assert',
        'The method must be marked with the [Fact] attribute, and there must be a constructor in the class which contains common setup code',
        'The method must be marked with the [TestMethod] attribute',
        'The method must either be marked using the [Fact] attribute, or the [TestMethod] attribute'
    ],
    'What should happen in the "Arrange" section in a unit test?': [
        'It should call the method being tested',
        'Nothing, it should all happen in the method marked as [TestInitialize]',
        'It should throw an exception if the unit test expects one',
        'It should set up the necessary test data',
        'It should check that the result of calling a given method in the system under test meets the expectations'
    ],
    'What should happen in the "Act" section in a unit test?': [
        'It should call the method being tested',
        'It should set up the necessary test data',
        'It should check that the result of calling a given method in the system under test meets the expectations',
        'It should catch an exception if the system under test is expected to throw such an exception'
    ],
    'What should happen in the "Assert" section in a unit test?': [
        'It should set up the necessary test data',
        'Nothing, it should all happen in the method marked as [TestInitialize]',
        'It should call the method being tested',
        'It should throw an exception if the unit test expects one',
        'It should check that the result of calling a given method in the system under test meets the expectations'
    ],
    'Why would we want to make us of caching in our web services?': [
        'because it is faster than a database and we won´t need a database if we have caching',
        'We would want to use caching because it is a depency injection framework and depency injection is crusial when writing loosely coupled code',
        'To make our webservice faster',
        'We wouldn´t want to use caching. It has no benefits at all'
    ],
    'To ensure that a method is properly tested, we need to:': [
        'a) Test that the return value of the method is what is expected given its input',
        'b) Test that any side effects (such as updating a record in a table) did in fact happen',
        'c) Test that if the method has side effects (such as updating a record in a table), only the intended records were affected, and not others (i.e. only those records which were supposed to be updated should have changed, and not any others)',
        'a), b) and c)',
        'Both a) and c)'
    ],
    'One of the following statements about Node.js is wrong. Which one?': [
        'Node.js was created by Ryan Dahl',
        'A Node.js application is single-threaded',
        'Node.js uses Google V8 behind the scenes',
        'Node.js programs run in the browser'
    ],
    'Express provides various services to make it easier to write web applications. Below is a list of various services, Express implements one of those (without the use of any plugins). Which one?': [
        'Routing',
        'XML serialization of objects',
        'Connection to ElasticSearch servers',
        'Unit testing'
    ],
    'In ES6, arrow functions differ from regular functions. Which one of the differences listed below is correct?': [
        'Arrow functions are always asynchronous, while regular functions are always synchronous',
        'We can use the "const" keyword inside arrow functions, but not inside regular functions',
        'The "this" keyword has different meaning in arrow functions than in regular functions',
        'There is no closure created for arrow functions',
        'Arrow functions can take optional parameters, but regular functions cannot'
    ],
    'What is the difference between the keywords "var" and "let" in ES6?': [
        '"var" is non-typesafe, but "let" is typesafe',
        '"var" creates a new scope, but "let" doesn´t',
        '"var" uses function scope, but "let" uses block scope',
        '"var" creates a closure object, but "let" doesn´t',
        '"var" is considered harmful, but "let" is not'
    ],
    'We can tell Express to use middleware in our apps. Assuming that "app" is our Express app, and "m" is a reference to our middleware (either 3rd party or our own). How is that middleware registered?': [
        'app.express(m)',
        'app(use(m))',
        'app.middleware(m);',
        'app.use(m => { res, req });',
        'app.use(m)'
    ],
    'Assume we´ve got an Express app with a route that should return HTTP Status code 412 under a given circumstances. Which of the methods below will do that?': [
        'res.error(412);',
        'res.send(412);',
        'res.throw(412);',
        'res.status(412);',
        'res.fail(412);'
    ],
    'What service does Mongoose provide us, which is not provided out of the box by MongoDB?': [
        'It allows us to export the table definitions, such that they can be declared in one file, but used in another',
        'Indexing on certain columns',
        'Automatic cleanup of unused tables',
        'It adds a number of datatypes not supported directly by Mongo',
        'Schema definitions and validation'
    ],
    'When using RabbitMQ, what do we call the code which receives messages from a message queue?': [
        'Listener',
        'Producer',
        'Performer',
        'Consumer',
        'Receiver'
    ]
}
