var button = document.getElementsByClassName('like-button')
var commentForm = document.getElementsByClassName('comment-form')


// Ajax for like button
for (let i = 0; i < button.length; i++){
    button[i].addEventListener('click',function(){
        let post_id = this.dataset.postid
        if (user != 'AnonymousUser')
            AjaxLike(post_id, button[i])
        else 
            console.log('not logged in!')
    })
}
function AjaxLike(post_id, button){
    var url = '/interact/like/'
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
        if (data.liked)
            button.value = String(data.total) + ' unlike'
        else
            button.value = String(data.total) + ' like'
    })
    .catch(function(){
        console.log('error')
    })
}
//Ajax for comment.
for (let i = 0; i < commentForm.length; i++){
    commentForm[i].addEventListener('submit', function(e){
        e.preventDefault()
        let formData = new FormData(this)
        let data = {}
        formData.forEach(function(value, key){
            data[key] = value
        })
        let postId = this.dataset.postid
        data['postId'] = postId
        if (user == 'AnonymousUser')
            alert('not logged in')
        else if (data['body'])
            ajaxComment(data)
    })    
}

function ajaxComment(data){
    url = '/interact/comment/'
    fetch(url,{
        method:'POST',
        body:JSON.stringify(data),
        headers:{
            'content_Type':'aplication/jason',
            'X-CSRFToken':csrftoken,
        },
        mode:'same-origin',
    })
    .then(response=>{
        return response.json()
    })
    .then(data=>{
        let commentLists = document.getElementsByClassName('commentlist')
        for(let i = 0; i < commentLists.length; i++){
            let newComment = '<h3>' + String(data['username']) + '</h3>'
            newComment += '<p>'+ String(data['body']) +'</P>'
            commentLists[i].insertAdjacentHTML('beforebegin',newComment)
        }
    })
    .catch(function(){
        console.log('ajax comment error')
    })
}