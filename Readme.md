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