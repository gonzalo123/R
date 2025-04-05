library(shiny)

source("api_client.R")

args <- commandArgs(trailingOnly = TRUE)
port <- if (length(args) >= 1) as.numeric(args[1]) else 3838
host <- if (length(args) >= 2) args[2] else "0.0.0.0"
launch_browser <- if (length(args) >= 3) as.logical(args[3]) else TRUE

runApp("app.R", port = port, host = host, launch.browser = launch_browser)