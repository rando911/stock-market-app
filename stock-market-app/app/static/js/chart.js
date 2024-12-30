document.addEventListener('DOMContentLoaded', () => {
    const symbol = "AAPL"; // You can change this or make it dynamic
    fetch(`/api/stock/${symbol}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                console.error(data.error);
                return;
            }

            const dates = data.prices.map(p => p.date);
            const prices = data.prices.map(p => p.close);

            const trace = {
                x: dates,
                y: prices,
                type: 'scatter',
                mode: 'lines+markers',
                name: symbol
            };

            const layout = {
                title: `Stock Prices for ${symbol}`,
                xaxis: { title: 'Date' },
                yaxis: { title: 'Price (USD)' }
            };

            Plotly.newPlot('chart', [trace], layout);
        });
});
