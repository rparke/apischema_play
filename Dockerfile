FROM continuumio/miniconda:4.7.12
RUN cd /home && git clone https://github.com/rparke/apischema_play 
#RUN conda env update -n base --file /home/APISCHEMA_PLAY/environment.yml
CMD bash