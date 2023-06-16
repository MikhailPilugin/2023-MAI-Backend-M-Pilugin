FROM nginx:1.22.1

RUN cd /etc/nginx/conf.d/ && mv default.conf default.conf~
RUN rm -rf /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/nginx.conf
RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr /var/log/nginx/error.log
EXPOSE 81
