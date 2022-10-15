# Docker in docker
```
docker network create some-network 
docker volume create some-docker-certs-ca
docker volume create some-docker-certs-client
docker run --privileged --name some-docker -d \
	--network some-network --network-alias docker \
	-e DOCKER_TLS_CERTDIR=/certs \
	-v some-docker-certs-ca:/certs/ca \
	-v some-docker-certs-client:/certs/client \
	docker:20.10.17-dind
docker run -it --network some-network \
	-e DOCKER_TLS_CERTDIR=/certs \
	-v some-docker-certs-client:/certs/client:ro \
	docker:20.10.17-git
```