
const numberInput = document.getElementById("number");
const generateBtn = document.getElementById("generateBtn");
const tableOutput = document.getElementById("tableOutput");
const resultSubtitle = document.getElementById("resultSubtitle");
const error = document.getElementById("error");

function generateTable() {
    const rawValue = numberInput.value.trim();
    const number = Number(rawValue);

    error.textContent = "";

    if (
        rawValue === "" ||
        !Number.isFinite(number) ||
        Math.abs(number) > 1000000
    ) {
        error.textContent =
            "Please enter a valid number between -1,000,000 and 1,000,000.";
        numberInput.focus();
        return;
    }

    tableOutput.innerHTML = "";

    resultSubtitle.textContent =
        `Multiplication table of ${number} · 1 to 10`;

    for (let i = 1; i <= 10; i++) {
        const result = number * i;

        const card = document.createElement("div");
        card.className = "table-card";
        card.style.animationDelay = `${i * 0.04}s`;

        const equation = document.createElement("span");
        equation.className = "equation";
        equation.textContent = `${number} × ${i} =`;

        const answer = document.createElement("span");
        answer.className = "answer";
        answer.textContent = result;

        card.append(equation, answer);
        tableOutput.appendChild(card);
    }
}

generateBtn.addEventListener("click", generateTable);

numberInput.addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
        generateTable();
    }
});
