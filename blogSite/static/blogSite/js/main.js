var button = document.getElementsByClassName('like-button')

for (let i = 0; i < button.length; i++){
    button[i].addEventListener('click',function(){
        let post_id = this.dataset.postid
        if (user != 'AnonymousUser')
            callAjax(post_id, button[i])
        else 
            console.log('not logged in!')
    })
}

function callAjax(post_id, button){
    var url = '/blogsite/like/'
    fetch(url,{
        method:'POST',
        headers:{
            'content_Type':'aplication/jason',
            'X-CSRFToken':csrftoken,
        },
        mode:'same-origin',
        body:JSON.stringify({'post_id':post_id})
    })
    .then(response=>{
        return response.json()
        //JSON.parser
    })
    .then(data=>{
        console.log(data)
        if (data.liked)
            button.value = String(data.total) + ' unlike'
        else
            button.value = String(data.total) + ' like'
    })
    .catch(function(){
        console.log('error')
    })
}