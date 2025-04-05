get_data <- function(uri, token = NULL) {
  library(httr)
  library(jsonlite)

  showNotification("Updating data...", type = "message")

  headers <- c(`Content-Type` = "application/json", `Accept` = "application/json")
  if (!is.null(token)) {
    headers <- c(headers, Authorization = paste("Bearer", token))
  }

  response <- GET(url = uri, add_headers(.headers = headers))

  if (http_error(response)) {
    stop(sprintf("Error en la petición: %s", status_code(response)))
  }

  content_text <- content(response, "text", encoding = "UTF-8")
  df <- fromJSON(content_text, flatten = TRUE)

  if (is.list(df) && "data" %in% names(df)) {
    df <- df$data
  }

  if (!is.data.frame(df)) {
    df <- as.data.frame(df)
  }

  return(df)
}

refreshData <- function(data, uri, token = NULL) {
  showNotification("Updating data...", type = "message")

  tryCatch({
    new_data <- get_data(uri, token)
    data(new_data)
    showNotification("Data updated!", type = "message")
  }, error = function(e) {
    showNotification(paste("Error updating data:", e$message), type = "error")
  })
}