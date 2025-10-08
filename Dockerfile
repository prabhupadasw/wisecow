FROM ubuntu:22.04


RUN apt-get update && \
    apt-get install -y fortune-mod cowsay netcat


WORKDIR /app


COPY wisecow.sh /app/wisecow.sh


RUN chmod +x /app/wisecow.sh


EXPOSE 4499


CMD ["/app/wisecow.sh"]
