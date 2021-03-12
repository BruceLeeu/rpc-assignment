# rpc-assignment

Running/testing the service.

1. Ensure docker is installed.
2. Clone repo to your device.
3. CD into cloned directory and open terminal:
4. In terminal run the following commands:
  docker build -t rpc-assignment .
  docker run -d -it --name rpc-assignment rpc-assignment
  docker exec -it rpc-assignment bash
  (a new shell will open)
  nameko shell
  (new shell will open)
  -- Now you can test all of the created services. An example of each:
  
  --> n.rpc.rpc_assignment_service.sq_odd(nums=[1,2,3,4,5,6,7,8,9])
  --> n.rpc.rpc_assignment_service.gen_dictionary(strings=["Louis la Grange", "Good programming practices are important", "The quick brown fox jumps over the lazy dog"])
  --> n.rpc.rpc_assignment_service.decode_string(string="eJzzyS/NLFbISVRwL0rMS08FACs8BW4=")
