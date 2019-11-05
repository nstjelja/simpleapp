# Setup working environment with virtualenv

```
virtualenv -p $(which python3) venv/
source venv/bin/activate
```

# Setup python librarires

```
make setup
```

# Run application

```
make run
```

# Change health

```
curl -I http://localhost:5555/healthy 
```

```
curl -I http://localhost:5555/sethealthy?set=0
```

```
curl -I http://localhost:5555/sethealthy?set=1
```

# Run chaos experiment

```
docker run -d --name jaeger  -e COLLECTOR_ZIPKIN_HTTP_PORT=9411   -p 5775:5775/udp   -p 6831:6831/udp   -p 6832:6832/udp   -p 5778:5778   -p 16686:16686   -p 14268:14268   -p 9411:9411   jaegertracing/all-in-one:1.6
chaos run experiment.yaml
```