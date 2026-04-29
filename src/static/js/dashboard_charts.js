document.addEventListener("DOMContentLoaded", function () {

  // 🔥 Pega dados do HTML (Django json_script)
  const dailyElement = document.getElementById("daily-data");
  const emotionElement = document.getElementById("emotion-data");

  if (!dailyElement || !emotionElement) {
    console.error("Dados do dashboard não encontrados no HTML.");
    return;
  }

  const daily = JSON.parse(dailyElement.textContent);
  const emotions = JSON.parse(emotionElement.textContent);

  // 🧠 DEBUG (pode remover depois)
  console.log("Daily:", daily);
  console.log("Emotions:", emotions);

  // 📈 GRÁFICO 1: Evolução do humor
  const moodCtx = document.getElementById("moodChart");

  if (moodCtx) {
    new Chart(moodCtx, {
      type: "line",
      data: {
        labels: daily.map(item => item.date),
        datasets: [{
          label: "Humor médio",
          data: daily.map(item => item.avg),
          borderWidth: 2,
          tension: 0.3
        }]
      },
      options: {
        responsive: true,
        plugins: {
          legend: { display: true }
        }
      }
    });
  }

  // 📊 GRÁFICO 2: Frequência de emoções
  const emotionCtx = document.getElementById("emotionChart");

  if (emotionCtx) {
    new Chart(emotionCtx, {
      type: "bar",
      data: {
        labels: emotions.map(item => item.emotion),
        datasets: [{
          label: "Frequência",
          data: emotions.map(item => item.count),
          borderWidth: 1
        }]
      },
      options: {
        responsive: true,
        plugins: {
          legend: { display: true }
        }
      }
    });
  }

});