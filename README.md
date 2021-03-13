# rpc-assignment

## Setup & Testing

### Steps required for setting up the Docker container.

1. Install Docker to your system if not yet installed.
2. Clone this repository to your system.
3. CD into cloned directory and open terminal in the root of the folder.
4. In terminal run the following commands:
   * ```docker build -t rpc-assignment .``` _Creates the Docker container from the Dockerfile._
   * ```docker run -d -it --name rpc-assignment rpc-assignment``` _Starts up the container created above with the name 'rpc-assignment'._
   * ```docker exec -it rpc-assignment bash``` _Opens a bash terminal in the container to execute commands on it._
   * ```nameko shell``` _Opens a nameko shell for the created service, which can accept and reply to RPC's._
5. Now you can test all of the created functions inside the service.

### Format for calling a function
``` n.rpc.rpc_assignment_service.```_example_function(value="Example")_
### Example calls for each created function
   * ```n.rpc.rpc_assignment_service.sq_odd(nums=[1,2,3,4,5,6,7,8,9])```
   * ```n.rpc.rpc_assignment_service.gen_dictionary(strings=["Louis la Grange", "Good programming practices are important", "The quick brown fox jumps over the lazy dog"])```
   * ```n.rpc.rpc_assignment_service.decode_string(string="eJzzyS/NLFbISVRwL0rMS08FACs8BW4=")```
 
## My thoughts on the task

This task was a very good exercise of adaptability for me. I am familiar with Python as a programming language, however my knowledge of implementing, using frameworks, and creating microservices with it was limited. I had to spend a good amount of time reading docs and doing research in order to orchestrate all of the separate requirements into a unified solution. This task challenged me to: learn on the fly; overcome an array of hurdles; manage my time; expand my expertise.
 
## Pros and Cons of Technologies used

### Python
#### Pros
+ Allows algorithms and programming logic to be written in a timely manner.
+ Community support (such as documentation, libraries, frameworks, and tutorials) is extensive.
+ Quick to execute, well optimized, small in size.
#### Cons
- Formatting can be complex to keep track of for larger applications.
- No strongly typed variables (can result in more documentation or data type errors).

### Nameko
#### Pros
+ Allows microservices to be developed speedily.
+ Enables you to focus solely on application logic (instead of developing a microservices framework yourself).
#### Cons
- Requires rabbitmq as a dependency (can potentially cause confusion and annoyance of set up).
- Limited in use as a microservices framework for web apps (Not really relevant for current use case).

### Docker
#### Pros
+ Allows you to ship your developed software together with a suitable development environment.
+ Runs - essentially - the same on all systems.
+ Relatively quick to set up.
+ Simple syntax to learn.
+ Great community support (such as documentation and docker hub images).
#### Cons
- Amount of customization in container set up can be overwhelming for beginners.
- Containers/storage files can be large.

## Design decisions

### Interface for testing the service
One major decision I had to make was with regards to how the service should be run/tested. Since this is a backend engineering assignment, I spent no time on creating a user interface for calling the functions, instead choosing to showcase the created functions via command line, in a shell of the service.

### Docker container considerations
I chose Python as the base image, since it is the main language used in the service, as well as because it is smaller and simpler to set up than a base image like Ubuntu. 
I also made the decision to create a single Docker image (instead of running multiple with docker-compose) as all I needed was for rabbitmq-server/nameko to be installed and started before opening a nameko shell. To Facilitate the latter I chose to create a shell file (in the ```CMD []```) that executes two commands when the container is run - starting up the rabbitmq-server and nameko service automatically.

### Function implementations
#### ```sq_odd()```
The first function ```sq_odd()``` takes a list integers, squares the odd numbers in the list - as outlined - and returns a new list containing only the squared numbers in given order. This was done because no specificity was given with regards to expected output of the function, and allows a user to see the results in the terminal output.
#### ```gen_dictionary()```
The second function ```gen_dictionary()``` accepts a list of strings and generates a dictionary - as outlined. The design decision here was to use an existing Python library _zlib_ to compress the string to a byte-like object, and then _base64_ (another library) to represent this compressed object as a base64 string. This was done because no specificity with regards to the precise encoding method was outlined. This encoding method serves as a proof-of-concept.
#### ```decode_string()```
The third function ```decode_string()``` accepts a single string as input and uses the same method outlined in the second function, except in reverse, for decoding the input to a plain text string - which is then returned so that the user can see the outcome in the terminal.

## Time breakdown

### Coding the functions in Python

The creation of the service.py file - which contains all the outlined functions - was a relatively straightforward task, since the documentation of creating services in nameko was well documented, and because Python is a simple language to use and implement. 
_Total Time taken: ~3 hours_

### Testing the functions using nameko shell

Running the nameko shell on my system locally took more time than I anticipated. This was due to the fact that nameko requires certain dependencies to be configured separately, before the shell functions. This step required me to install rabbitmq-server (and its dependencies) and ensure that it was running before starting the nameko service. Only after this, I could open the nameko shell and call the created functions.
_Total Time taken: ~2 hours_

### Containerizing the service with Docker

I have no prior practical experience with Docker, so I had to learn on the fly using documentation and quick tutorials. After this I had to choose the ideal starting image for the container, ensure that the container had all the required dependencies mentioned above set up and installed, as well as trial and document the appropriate Docker CLI commands to replicate my results.
_Total Time taken: ~7 hours_

### Documentation

My documentation - such as commenting, pushing git commits, and annotating required commands - has been done in an ongoing manner and time taken is therefore included in the previous subsections. 
**This excludes the report (debrief) on my experience and thoughts of this assignment, which took about ~3 hours in total.

### Grand Total time taken
~ 15 Hours (50 - 65% research)
Note: This time does not include any breaks taken, communications to the company, and other miscellaneous activities (such as setting up my development environment, downloading large files, and waiting for large compilations/builds to complete)

![Thanks Gif](https://media3.giphy.com/media/e7QoUmjplkXzGUDWzF/giphy.gif)

♡ Louis la Grange © 2021
