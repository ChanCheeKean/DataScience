# docker command line


# download latest image nginx from docker hub 
# started new container from the image, and open port 80
# if on window, need extra step to stop after ctrl-c, to stop it from running in the background
'''
docker container run --publish 80:80 nginx
docker stop <container id/name>
'''

# tell docker to run in background
'''
docker container run --publish 80:80 --detach --name webhost nginx
'''

# ls to see directory and running container
# stop it with container id
# -a to see all containers  (included not running)
'''
docker container ls
docker stop cebaabc
docker container ls -a
'''

# check log
'''
docker container logs webhost
'''

# remove container
'''
docker rm 4c8 ceba 5bad 
'''
