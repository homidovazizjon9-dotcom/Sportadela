const playersByRole = {
  attack: [
    {
      name: "Эрлинг Холанд",
      team: "Манчестер Сити",
      badge: "xG 0.82",
      metrics: {
        "Голы/90": "1.02",
        "Удары": "4.7",
        "xG/удар": "0.21",
        "Вклад": "+0.34",
      },
    },
    {
      name: "Мохамед Салах",
      team: "Ливерпуль",
      badge: "xA 0.38",
      metrics: {
        "Голы/90": "0.78",
        "Ассисты": "0.31",
        "Ключ. пас": "2.1",
        "Вклад": "+0.28",
      },
    },
    {
      name: "Букайо Сака",
      team: "Арсенал",
      badge: "xG+xA 0.74",
      metrics: {
        "Голы/90": "0.62",
        "Ассисты": "0.29",
        "Дриблинг": "3.3",
        "Вклад": "+0.25",
      },
    },
  ],
  midfield: [
    {
      name: "Родри",
      team: "Манчестер Сити",
      badge: "Контроль 92%",
      metrics: {
        "Передачи": "89",
        "Прогресс": "11.4",
        "Отборы": "2.2",
        "Вклад": "+0.19",
      },
    },
    {
      name: "Деклан Райс",
      team: "Арсенал",
      badge: "Давление 28",
      metrics: {
        "Перехваты": "1.8",
        "Отборы": "2.4",
        "Пасы вразрез": "6.1",
        "Вклад": "+0.17",
      },
    },
    {
      name: "Бруно Гимарайнш",
      team: "Ньюкасл",
      badge: "Прессинг 31",
      metrics: {
        "Передачи": "78",
        "Прогресс": "10.2",
        "Фолы": "1.3",
        "Вклад": "+0.14",
      },
    },
  ],
  defense: [
    {
      name: "Вирджил ван Дейк",
      team: "Ливерпуль",
      badge: "xGA 0.68",
      metrics: {
        "Выносы": "5.6",
        "Пасы": "74",
        "Поб. борьбы": "73%",
        "Вклад": "+0.22",
      },
    },
    {
      name: "Уильям Салиба",
      team: "Арсенал",
      badge: "Дуэли 72%",
      metrics: {
        "Отборы": "1.7",
        "Перехваты": "1.9",
        "Пасы": "82",
        "Вклад": "+0.21",
      },
    },
    {
      name: "Кайр Уокер",
      team: "Манчестер Сити",
      badge: "Скорость 33.1",
      metrics: {
        "Отборы": "2.1",
        "Перехваты": "1.4",
        "Спринты": "21",
        "Вклад": "+0.18",
      },
    },
  ],
};

const playerGrid = document.querySelector("#playerGrid");
const tabs = document.querySelectorAll(".tab");

const renderPlayers = (role) => {
  playerGrid.innerHTML = "";
  playersByRole[role].forEach((player) => {
    const card = document.createElement("article");
    card.className = "player-card";

    card.innerHTML = `
      <span class="player-badge">${player.badge}</span>
      <h4>${player.name}</h4>
      <p>${player.team}</p>
      <div class="player-metrics">
        ${Object.entries(player.metrics)
          .map(
            ([label, value]) => `
              <div>
                <strong>${value}</strong>
                <div>${label}</div>
              </div>
            `
          )
          .join("")}
      </div>
    `;

    playerGrid.appendChild(card);
  });
};

tabs.forEach((tab) => {
  tab.addEventListener("click", () => {
    tabs.forEach((button) => button.classList.remove("active"));
    tab.classList.add("active");
    renderPlayers(tab.dataset.role);
  });
});

renderPlayers("attack");
