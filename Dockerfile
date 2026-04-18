FROM nginx:alpine

# 복사할 Nginx 설정 파일
COPY ./nginx.conf /etc/nginx/conf.d/default.conf

# HTML Mockup 파일을 Nginx 서빙 위치로 복사
COPY ./docs/SafeK_Mockup.html /usr/share/nginx/html/index.html

EXPOSE 80
EXPOSE 8080

CMD ["nginx", "-g", "daemon off;"]
