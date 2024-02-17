
change <- function(now, prev) {
  ch <- now - prev
  pc_ch <- (ch / prev) * 100
  
  cat("% change: ", round(pc_ch, 1), "%", "\n")
  cat("Delta: ", round(ch, 3))
  
}

ht_loss <- function(bad, normal) {
  loss_pc <- ( (normal - bad) / normal ) * 100
  degree <- if(loss_pc >= 40){
    "severe"
  } else if (loss_pc >= 25) {
    "moderate"
  } else if (loss_pc >= 20) {
    "mild"
  } else {
    "less than mild"
  }
  
  cat("Height loss: ", round(loss_pc, 1), " %", " (", degree, ") ", sep = "")
}


bmi <- function(ht_cm, wt_kg) {
  wt_kg / (ht_cm/100)^2
}