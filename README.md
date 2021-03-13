# rpc-assignment

## Setup & Testing

### Steps required for setting up the Docker container.

1. Install Docker to your system if not yet installed.
2. Clone this repository to your system.
3. CD into cloned directory and open terminal in the root of the folder:
4. In terminal run the following commands:
   * ```docker build -t rpc-assignment .``` _Creates the Docker container from the Dockerfile_
   * ```docker run -d -it --name rpc-assignment rpc-assignment``` _Starts up the container created above with the name 'rpc-assignment'_
   * ```docker exec -it rpc-assignment bash``` _Opens a bash terminal in the container to execute commands on it_
   * ```nameko shell``` _Opens a nameko shell for the created service, which can accept and reply to RPC's_
5. Now you can test all of the created functions inside the service.

### Format for calling a function
``` n.rpc.rpc_assignment_service.```_example_function(value="Example")_
### Example calls for each created function
   * ```n.rpc.rpc_assignment_service.sq_odd(nums=[1,2,3,4,5,6,7,8,9])```
   * ```n.rpc.rpc_assignment_service.gen_dictionary(strings=["Louis la Grange", "Good programming practices are important", "The quick brown fox jumps over the lazy dog"])```
   * ```n.rpc.rpc_assignment_service.decode_string(string="eJzzyS/NLFbISVRwL0rMS08FACs8BW4=")```
 
