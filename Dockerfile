FROM continuumio/miniconda:4.7.12
COPY * /home/APISCHEMA_PLAY
RUN conda create -f environment.yml
RUN CD /home && mkdir APISCHEMA_PLAY
CMD conda activate base