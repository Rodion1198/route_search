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
    qs = Train.objects.all().select_related('from_city', 'to_city')
    graph = get_graph(qs)
    data = form.cleaned_data
    from_city = data['from_city']
    to_city = data['to_city']
    cities = data['cities']
    travelling_time = data['travelling_time']   # noqa: F841
    all_routes = list(dfs_paths(graph, from_city.id, to_city.id))
    if not len(all_routes):   # There is no route for this search
        raise ValueError('There is no route satisfying the condition!')
    if cities:
        _cities = [city.id for city in cities]   # noqa: F841  # Get a list of cities through which you need to drive
        _ways = []
        for route in all_routes:   # loop through all id cities
            # Checking the entry of the city into the route,
            # if all the cities that are indicated there are in the route, then all() return True

            if all(city in route for city in _cities):
                _ways.append(route)
        if not _ways:   # When list of routes is empty
            raise ValueError('Route through these cities is not possible!')
    else:
        _ways = all_routes
    routes = []
    all_trains = {}
    for q in qs:
        all_trains.setdefault((q.from_city_id, q.to_city_id), [])
        all_trains[(q.from_city_id, q.to_city_id)].append(q)
    for route in _ways:
        tmp = {}
        tmp['trains'] = []
        total_time = 0
        for i in range(len(route) - 1):
            qs = all_trains[(route[i], route[i + 1])]
            q = qs[0]
            total_time += q.travel_time
            tmp['trains'].append(q)
        tmp['total_time'] = total_time
        if total_time <= travelling_time:
            routes.append(tmp)
    if not routes:
        raise ValueError('Travel time is longer than specified!')
    sorted_routes = []
    if len(routes) == 1:
        sorted_routes = routes
    else:
        times = list(set(r['total_time'] for r in routes))
        times = sorted(times)
        for time in times:
            for route in routes:
                if time == route['total_time']:
                    sorted_routes.append(route)
    context['routes'] = sorted_routes
    context['cities'] = {'from_city': from_city.name, 'to_city': to_city.name}
    return context
