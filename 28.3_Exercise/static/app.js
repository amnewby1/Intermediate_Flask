//Markup for cupcakes
function makeCupcakeMarkup(cupcake) {
  return `<li data-cupcake-id=${cupcake.id} class='list-group-item'><img src='${cupcake.image}'> Flavor: ${cupcake.flavor}, Size: ${cupcake.size}, Rating: ${cupcake.rating} <button class = "btn btn-danger" id="delete-button">Delete</button></li>;`;
}

//Rendering all the cupcakes in the list
const getCupcakes = async () => {
  await axios.get("http://127.0.0.1:5000/api/cupcakes").then((res) => {
    for (let cupcake of res.data.cupcake) {
      let listOfCupcakes = $(makeCupcakeMarkup(cupcake));
      $("#list_of_cupcakes").append(listOfCupcakes);
    }
  });
};

//Handle form submission
const handleSubmit = async () => {
  console.log("got here!");

  let flavor = document.getElementById("flavor").value;
  let rating = document.getElementById("rating").value;
  let size = document.getElementById("size").value;
  let image = document.getElementById("image").value;

  const newCupcakeResponse = await axios.post(
    "http://127.0.0.1:5000/api/cupcakes",
    { flavor, rating, size, image }
  );

  let newCupcake = makeCupcakeMarkup(newCupcakeResponse.data.cupcake);
  $("#list_of_cupcakes").append(newCupcake);
  $("#addCupcake").trigger("reset");
};
//delete cupcake
$("#cupcakes-list").on("click", ".delete-button", async function (evt) {
  evt.preventDefault();
  let $cupcake = $(evt.target).closest("div");
  let cupcakeId = $cupcake.attr("data-cupcake-id");

  await axios.delete(`${BASE_URL}/cupcakes/${cupcakeId}`);
  $cupcake.remove();
});

getCupcakes();
