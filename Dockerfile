FROM continuumio/miniconda:4.7.12
RUN cd /home && mkdir APISCHEMA_PLAY 
COPY * /home/APISCHEMA_PLAY/ 
#RUN conda env update -n base --file /home/APISCHEMA_PLAY/environment.yml
CMD bash