document.getElementById('checkBtn').addEventListener('click', () => {
  const emailText = document.getElementById('emailText').value;
  const resultEl = document.getElementById('result');
  resultEl.innerText = "Checking...";  

  fetch("http://127.0.0.1:5001/predict", { 
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ email_text: emailText }) 
  })
  .then(res => res.json())
  .then(data => {
    console.log("Response data:", data);

    if (data.prediction === "Phishing") {
      resultEl.innerText = "This email is PHISHING!";
      resultEl.style.color = "red";
    } else if (data.prediction === "Legitimate") {
      resultEl.innerText = "This email is LEGITIMATE.";
      resultEl.style.color = "green";
    } else {
      resultEl.innerText = data.error || "Unknown response from server";
      resultEl.style.color = "gray";
    }
  })
  .catch(err => {
    resultEl.innerText = "Error contacting server";
    resultEl.style.color = "gray";
    console.error("Server error:", err);
  });
});