from trains.models import Train


def dfs_paths(graph, start, goal):
    """ Search func for all possible routes from one city to another.
     The option of visiting the same city more than once is not considered """
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        if vertex in graph.keys():
            for next_ in graph[vertex] - set(path):
                if next_ == goal:
                    yield path + [next_]
                else:
                    stack.append((next_, path + [next_]))


def get_graph(qs):
    """ The func creates a graph so that this graph can be passed to the func
     for finding all routes using the depth-first-search algorithm """
    graph = {}
    for q in qs:
        graph.setdefault(q.from_city_id, set())
        graph[q.from_city_id].add(q.to_city_id)
    return graph


def get_routes(request, form) -> dict:
    context = {'form': form}
    qs = Train.objects.all()
    graph = get_graph(qs)
    data = form.cleaned_data
    from_city = data['from_city']
    to_city = data['to_city']
    cities = data['cities']
    travelling_time = data['travelling_time']   # noqa: F841
    all_routes = dfs_paths(graph, from_city.id, to_city.id)
    if not len(list(all_routes)):
        raise ValueError('There is no route satisfying the condition!')
    if cities:
        _cities = [city.id for city in cities]   # noqa: F841  # Get a list of cities through which you need to drive
        _ways = []
        for route in all_routes:   # loop through all id cities
            """ Checking the entry of the city into the route,
            if all the cities that are indicated there are in the route, then all() return True """
            if all(city in route for city in cities):
                _ways.append(route)
        if not _ways:
            raise ValueError('Route through these cities is not possible!')
    return context
