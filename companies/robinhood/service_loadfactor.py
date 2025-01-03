# You are building an application that consists of many different services that can depend on each other. One of these services is the entrypoint which receives user requests and then makes requests to each of its dependencies, which will in turn call each of their dependencies and so on before returning.

# Given a directed acyclic graph that contains these dependencies, you are tasked with determining the "load factor" for each of these services to handle this load. The load factor of a service is defined as the number of units of load it will receive if the entrypoint receives a 1 unit of load. Note that we are interested in the worst case capacity. For a given downstream service, its load factor is the number of units of load it is required to handle if all upstream services made simultaneous requests. For example, in the following dependency graph where A is the entrypoint: { A:[B, C], B:[C], C:[D] }

# Each query to A will generate one query to B which will pass it on to C and from there to D. A will also generate a query to C which will pass it on to D, so the worst case (maximum) load factors for each service is A:1, B:1, C:2, D:2.

# (Important: make sure you've fully understood the above example before proceeding!)

# Problem Details

    # service_list: An array of strings of format service_name=dependency1,dependency2. Dependencies can be blank (e.g. dashboard=) and non-existent dependency references should be ignored (e.g. prices=users,foobar and foobar is not a service defined in the graph). Each service is defined only once in the graph.

    # entrypoint: An arbitrary service that is guaranteed to exist within the graph

    # Output: A list of all services depended by (and including) entrypoint as an array of strings with the format service_name*load_factor sorted by service name.

# Example

    # # Input:
    # service_list = ["logging=", 
    #  "user=logging", 
    #  "orders=user,foobar", 
    #  "recommendations=user,orders", 
    #  "dashboard=user,orders,recommendations"]
    # entrypoint = "dashboard"

# # Output (note sorted by service name)
    # ["dashboard*1", 
    #  "logging*4", 
    #  "orders*2", 
    #  "recommendations*1", 
    #  "user*4"]


def load_Factors(service_list, entrypoint):
    
    graph = defaultdict(list)
    indegree = defaultdict(int)
    services = set()

    for service in service_list:
        srv, deps = service.split("=")
        deps = deps.spilt(",") if deps else []
        services.add(srv)
        
        for dep in deps:
            graph[srv].add(dep)
            indegree[dep] += 1
            services.add(dep)

    for srv in services:
        if srv not in indegree:
            indegree[srv] = 0

    # toposort
    topo_order = []
    queue = deque()

    for srv in services:
        if indegree[srv] == 0:
            queue.append(src)

    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for neigh in graph[node]:
            indegree[neigh] -= 1
            if indegree[neigh] == 0:
                queue.append(neigh)
    
    load_factors = defaultdict(int)
    load_factors[entrypoint] = 1

    for node in reversed(topo_order):
        if node in load_factors:
            for neigh in graph[node]:
                looad_factors[neigh] += load_factors[node]

    result = [f"{service}*{load_factor[service]}" for service in services if service in load_factors]

    result.sort()
    return result

# Example input
service_list = [
    "logging=", 
    "user=logging", 
    "orders=user,foobar", 
    "recommendations=user,orders", 
    "dashboard=user,orders,recommendations"
]
entrypoint = "dashboard"

# Calculate and print the load factors
result = calculate_load_factors(service_list, entrypoint)
print(result)