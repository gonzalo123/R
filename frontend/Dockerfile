FROM rocker/shiny:4.3.3 AS base

ENV APP_USER=appuser
ENV APP_HOME=/src
ENV TZ='Europe/Madrid'

RUN groupadd -r $APP_USER && \
    useradd -r -g $APP_USER -d $APP_HOME -s /sbin/nologin -c "Docker image user" $APP_USER

RUN echo $TZ > /etc/timezone && \
    apt-get update && apt-get install -y --no-install-recommends \
    libcurl4-openssl-dev \
    libssl-dev \
    libxml2-dev \
    libcairo2-dev \
    libsqlite3-dev \
    libmariadbd-dev \
    libpq-dev \
    libssh2-1-dev \
    libgit2-dev \
    zlib1g-dev \
    unixodbc-dev \
    libfontconfig1-dev \
    libfreetype6-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


RUN mkdir -p $APP_HOME && chown $APP_USER:$APP_USER $APP_HOME

FROM base

WORKDIR $APP_HOME


COPY --chown=$APP_USER:$APP_USER src/renv.lock ./renv.lock
COPY --chown=$APP_USER:$APP_USER src/.Rprofile ./.Rprofile
RUN Rscript -e 'install.packages("renv")'
RUN Rscript -e 'renv::restore(confirm = FALSE)'

COPY --chown=$APP_USER:$APP_USER src/. .

USER $APP_USER
