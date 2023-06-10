function greet()
{
    alert("hello there");
}



document.querySelector('form').addEventListener('submit',function(e){
    let rating = document.querySelector('#rating').value;
    alert("theodore's seductive rating: "+rating);
    e.preventDefault()
});
