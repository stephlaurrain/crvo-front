FROM debian:bullseye-slim

ENV DEBIAN_FRONTEND noninteractive
ENV LSB_RELEASE=bullseye
WORKDIR "/root"
RUN apt-get update && apt-get install -y nano \
    apt-utils \    
    xz-utils \ 
    supervisor;



ENV NODE_VERSION=16
ENV NODE_SUBVERSION=18.0
ENV ARCH=x64
ENV NODEARCH=node-v$NODE_VERSION.$NODE_SUBVERSION-linux-$ARCH.tar.xz
COPY /conf/supervisord.conf /etc/supervisor/conf.d
COPY /install/$NODEARCH /root

RUN tar -xJf "$NODEARCH" -C /usr/local --strip-components=1 --no-same-owner; \
  rm "$NODEARCH"; \
  # mkdir /root/tmp; \
  apt-get clean; \
  npm install -g yarn; \
  npm install -g nodemon; \
  npm update -g; 

#WORKDIR "/root/frontend"
#RUN  npm install; 
EXPOSE 4200 3000
ENTRYPOINT ["/usr/bin/supervisord"]
