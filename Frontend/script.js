document.addEventListener("DOMContentLoaded", function() {
    fetch("http://127.0.0.1:5000/transactions")
        .then(response => response.json())
        .then(data => {
            let tableBody = document.getElementById("transactionTable");
            let categories = {};
            
            data.forEach(transaction => {
                let row = `<tr>
                    <td>${transaction.category}</td>
                    <td>${transaction.amount}</td>
                    <td>${transaction.timestamp}</td>
                </tr>`;
                tableBody.innerHTML += row;

                if (categories[transaction.category]) {
                    categories[transaction.category] += transaction.amount;
                } else {
                    categories[transaction.category] = transaction.amount;
                }
            });

            let ctx = document.getElementById("transactionChart").getContext("2d");
            new Chart(ctx, {
                type: "pie",
                data: {
                    labels: Object.keys(categories),
                    datasets: [{
                        data: Object.values(categories),
                        backgroundColor: ["red", "blue", "green", "yellow", "purple"]
                    }]
                }
            });
        });
});
