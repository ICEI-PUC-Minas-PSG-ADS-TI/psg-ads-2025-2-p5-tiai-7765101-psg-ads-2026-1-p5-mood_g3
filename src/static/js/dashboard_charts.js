document.addEventListener("DOMContentLoaded", function () {

  // =========================
  // PEGAR DADOS DO HTML
  // =========================

  const dailyElement = document.getElementById("daily-data");
  const emotionElement = document.getElementById("emotion-data");
  const hourlyElement = document.getElementById("hourly-data");
  const weeklyElement = document.getElementById("weekly-data");

  if (!dailyElement || !emotionElement) {
    console.error("Dados principais não encontrados.");
    return;
  }

  const daily = JSON.parse(dailyElement.textContent);
  const emotions = JSON.parse(emotionElement.textContent);

  const hourly = hourlyElement
    ? JSON.parse(hourlyElement.textContent)
    : [];

  const weekly = weeklyElement
    ? JSON.parse(weeklyElement.textContent)
    : [];

  // =========================
  // CONFIGURAÇÃO GLOBAL
  // =========================

  Chart.defaults.font.family = "'Segoe UI', sans-serif";

  // =========================
  // GRÁFICO 1 - EVOLUÇÃO
  // =========================

  const moodCtx = document.getElementById("moodChart");

  if (moodCtx) {
    new Chart(moodCtx, {
      type: "line",
      data: {
        labels: daily.map(item => item.date),
        datasets: [{
          label: "Humor Médio",
          data: daily.map(item => item.avg),
          borderColor: "#4f46e5",
          backgroundColor: "rgba(79,70,229,0.15)",
          borderWidth: 3,
          tension: 0.4,
          fill: true,
          pointRadius: 5
        }]
      },
      options: {
        responsive: true,
        plugins: {
          legend: {
            display: true
          }
        }
      }
    });
  }

  // =========================
  // GRÁFICO 2 - EMOÇÕES
  // =========================

  const emotionCtx = document.getElementById("emotionChart");

  if (emotionCtx) {
    new Chart(emotionCtx, {
      type: "doughnut",
      data: {
        labels: emotions.map(item => item.emotion),
        datasets: [{
          label: "Frequência",
          data: emotions.map(item => item.count),
          backgroundColor: [
            "#6366f1",
            "#14b8a6",
            "#f59e0b",
            "#ef4444",
            "#8b5cf6",
            "#06b6d4"
          ]
        }]
      },
      options: {
        responsive: true,
        plugins: {
          legend: {
            position: "bottom"
          }
        }
      }
    });
  }

  // =========================
  // GRÁFICO 3 - HORÁRIOS
  // =========================

  const hourCtx = document.getElementById("hourChart");

  if (hourCtx && hourly.length > 0) {

    new Chart(hourCtx, {
      type: "bar",
      data: {
        labels: hourly.map(item => `${item.hour}h`),
        datasets: [{
          label: "Registros",
          data: hourly.map(item => item.count),
          backgroundColor: "#0ea5e9",
          borderRadius: 10
        }]
      },
      options: {
        responsive: true,
        plugins: {
          legend: {
            display: true
          }
        }
      }
    });
  }

  // =========================
  // GRÁFICO 4 - SEMANAL
  // =========================

  const weekCtx = document.getElementById("weekChart");

  if (weekCtx && weekly.length > 0) {

    new Chart(weekCtx, {
      type: "line",
      data: {
        labels: weekly.map(item =>
        item.week
        ),
        datasets: [{
          label: "Média Semanal",
          data: weekly.map(item => item.avg),
          borderColor: "#10b981",
          backgroundColor: "rgba(16,185,129,0.15)",
          borderWidth: 3,
          tension: 0.4,
          fill: true,
          pointRadius: 5
        }]
      },
      options: {
        responsive: true,
        plugins: {
          legend: {
            display: true
          }
        }
      }
    });
  }

});