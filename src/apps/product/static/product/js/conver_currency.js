

function convert(from, to, amount) {
    fetch(`https://api.exchangerate-api.com/v4/latest/${from}`)
    .then(response => {
        return response.json();
    })
    .then(data => {
    return data.rates[to] * amount;
    });
}


async function convert(from, to, amount) {
    resonse = await fetch(`https://api.exchangerate-api.com/v4/latest/${from}`)
    data = await response.json()
    return data.rates[to] * amount
}