# To build image:
```
docker build -t shamimice03/demo-app:2.0.0 .
```

# Test image locally:
```
docker run -p 8080:5050 -d shamimice03/demo-app:2.0.0 
```

# Add tag:
```
docker tag shamimice03/demo-app:2.0.0 shamimice03/demo-app:latest
```

# Push to dockerhub:
```
docker push shamimice03/demo-app:2.0.0
docker push shamimice03/demo-app:latest
```

# Pull image:
```
docker pull shamimice03/demo-app
```

