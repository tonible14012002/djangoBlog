var button = document.getElementsByClassName('like-button')
var commentForm = document.getElementsByClassName('comment-form')

function isEmptyOrSpaces(str){
    return str === null || str.match(/^ *$/) !== null;
}

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
        let form = new FormData(this)
        let formData = {}
        form.forEach(function(value, key){
            formData[key] = value
        })
        let postId = this.dataset.postid
        formData['postId'] = postId
        if (user == 'AnonymousUser')
            alert('not logged in')
        else if (!isEmptyOrSpaces(formData['body']))
            ajaxComment(formData)
    })    
}

function ajaxComment(formData){
    url = '/interact/comment/'
    fetch(url,{
        method:'POST',
        body:JSON.stringify(formData),
        headers:{
            'content_Type':'aplication/jason',
            'X-CSRFToken':csrftoken,
        },
        mode:'same-origin',
    })
    .then(response=>{
        return response.json()
    })
    .then((data)=>{
        let commentLists = document.getElementsByClassName('commentlist')
        for(let i = 0; i < commentLists.length; i++){
            
            //render new Comment
            let username = document.createElement('h3')
                username.innerText = data['username']
            let newComment = document.createElement('p')
                newComment.innerText = formData['body']
        
            commentLists[i].insertAdjacentElement('afterbegin',newComment)
            commentLists[i].insertAdjacentElement('afterbegin',username)
            
            //clear input field
            let input = document.querySelector('.comment-form > input[name="body"]')
            input.value =''
            
            commentCountId = 'cmt-count-' + formData['postId']
            commentCount = document.getElementById(commentCountId)
            num = String(data['commentCount'])
            commentCount.innerText = num + ' comments'
        }
    })
    .catch(function(){
        console.log('ajax comment error')
    })
}