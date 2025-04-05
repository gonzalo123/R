library(shiny)

library(ggplot2)
library(dplyr)
library(shinyWidgets)
library(dotenv)
library(DT)

df <- data.frame()
load_dot_env()

config <- list(
  api_url = Sys.getenv("API_URL"),
  api_token = Sys.getenv("API_KEY")
)

ui <- fluidPage(
  titlePanel("R api call example"),

  fluidRow(
    column(12,
           actionButton("refrescar", "Refresh data", icon = icon("refresh"), class = "btn-primary")
    )
  ),

  mainPanel(
    DTOutput("table")
  )
)

server <- function(input, output, session) {
  data <- reactiveVal(df)

  refreshData(data, config$api_url, config$api_token)

  observeEvent(input$refrescar, {
    refreshData(data, config$api_url, config$api_token)
  })

  output$table <- renderDT({
    data()
  })
}

shinyApp(ui = ui, server = server)