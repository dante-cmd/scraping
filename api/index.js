const tBodyId = document.getElementById("tbody-id");
const btn = document.getElementById("btn");

// function dynamicFunction() {
//   const nameInput = prompt("Name: ");
//   // const nameInput = "Dante"

//   if (! (nameInput == "Dante")) {

//     dynamicFunction()
//   } else {
//     console.log("Successful, your name is accepted")
//     // throw new Error("Wrong in the password");
//   }
// }
// dynamicFunction()


const getData = async () => {
  const request = new Request("http://127.0.0.1:8000")
  const resp = await fetch(request);
  const result = await resp.json();
  return result
}

btn.addEventListener("click", async () => {
  const data = await getData()
  const dataTo = data.number 
  const row = document.createElement('tr')
  dataTo.forEach(e => {
    const cell  = document.createElement('td')
    cell.textContent = e
    row.appendChild(cell)
  })
  tBodyId.innerHTML = row.innerHTML
  // const data = getdata()
  

});





// window.addEventListener('load', async () => {
//   const data = await getData()
//   const dataTo = data.number 
//   const row = document.createElement('tr')
//   dataTo.forEach(e => {
//     const cell  = document.createElement('td')
//     cell.textContent = e
//     row.appendChild(cell)
//   })
//   tBodyId.innerHTML = row.innerHTML
//   // const data = getdata()

// })

// setTimeout(function() {
//   window.location.reload(1)
// }, 4000)


