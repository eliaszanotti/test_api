FROM	node:22-alpine

WORKDIR	/usr/src/front

COPY	. /usr/src/front
RUN		npm install
EXPOSE	5173

RUN		chmod +x ./entrypoint.sh
CMD		./entrypoint.sh