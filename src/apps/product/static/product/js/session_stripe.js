

const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
const st_pk = document.getElementById('stripe_pk').innerText
const stripe = Stripe(st_pk);

const checkoutButton = document.getElementById("buy-button");
checkoutButton.addEventListener("click", getSessionToRedirect)

let p = document.getElementById("to_current")
p.addEventListener("change", convert)

async function getSessionToRedirect() {
    let current = document.getElementById('currency').innerText.split(':')[1].replace(/\s/g, '')
    let price = document.getElementById('price').innerHTML.split(':')[1].replace(/\s/g, '')
    let name = document.getElementById('item_name_').innerText

    const response = await fetch(`http://127.0.0.1:8000/api/v1/session/get_session/`, {
      method: "POST",
      headers: {
          'X-CSRFToken': csrftoken,
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        amount: Math.floor(price),
        currency: current,
        name_product: name,
        quantity: 1

      })
    })
    const session = await response.json()
    const result =  await stripe.redirectToCheckout({ sessionId: session.id });

    if (result.error) {
      alert(result.error.message)
    }
}


  async function convert() {
      let now_current = document.getElementById('currency')
      let n_current = now_current.innerText.split(':')[1].replace(/\s/g, '')

      let to_current_element = document.getElementById('to_current')
      let to_current = to_current_element.options[to_current_element.selectedIndex].text;
      let price = document.getElementById('price')
      let n_price = price.innerHTML.split(':')[1].replace(/\s/g, '')


      let resonse = await fetch(`https://api.exchangerate-api.com/v4/latest/${n_current}`)
      data = await resonse.json()
      let new_price  = data.rates[to_current] * Number(n_price)

      now_current.innerHTML = `Оплата в валюте: ${to_current}`
      price.innerHTML = `Цена: ${new_price}`

  }