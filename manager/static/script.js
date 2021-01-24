function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


$('document').ready(function () {
    $('.like-comment').on('click', function like_com () {
        let id=$(this).attr('id');
        let comment_id = id.split('-')[2];
        $.ajax({
            url:`/shop/add_like2comment_ajax/${comment_id}`,
            headers: {'X-CSRFToken': csrftoken},
            method: "PUT",
            success: function (data) {
                $(`#${id}`).html(`Likes: ${data['likes']}`);
            }
        })
    });

    $('.delete-comment').on('click', function () {
        let id=$(this).attr('id'), id2=`block-comment-${id.split("-")[2]}`;
        let comment_id = id.split("-")[2];
        $.ajax({
            url: `/shop/delete_comment_ajax/${comment_id}`,
            method: "DELETE",
            headers: {'X-CSRFToken': csrftoken},
            success: function (data) {
                $(`#${id2}`).remove()
            }
        })
    });

    $('.delete-book').on('click', function () {
        let id=$(this).attr('id'), id2=`${id.split("-")[2]}`;
        $.ajax({
            url: "/shop/delete_book_ajax",
            data: {"slug": id.split("-")[2]},
            method: "GET",
            success: function (data) {
                $(`#${id2}`).remove()
            }
        })
    });

    $('.rate').on('click', function () {
        let id=$(this).attr('id'),
            id6=`total_rate-${id.split("-")[1]}`,
            id7=`voice-${id.split("-")[1]}`;
//            id8='check-star',
//            id9='dark-star';
        console.log(id)
        $.ajax({
            url:"/shop/rate_ajax",
            data: {"slug": id.split("-")[1], "rate": id.split("-")[2]},
            method: "GET",
            success: function (data) {
                console.log(data['rate']);

                $(`#${id6}`).html(data['rate']);
                $(`#${id7}`).html(`Число голосов: ${data['count_rated_users']}`);
//                var
//                    dark = document.getElementById(id9).innerHTML,
//                    check = document.getElementById(id8).innerHTML;

                for (let i=1; i<6; i++) {
//                    if (data['rate'] >= i) {
//                        document.getElementById(`star-${id.split("-")[1]}-${i}`).innerHTML = check;
//                    }
//                    else {
//                        document.getElementById(`star-${id.split("-")[1]}-${i}`).innerHTML = dark;
//                    }
                    if (data['rate'] >= i) {
                        document.getElementById(`star-${id.split("-")[1]}-${i}`).attr('class', 'rate fa fa-star checked');
                    }
                    else {
                        document.getElementById(`star-${id.split("-")[1]}-${i}`).attr('class', 'rate fa fa-star');
                    }
                }

            }
        })
    });


    $('form').submit (function () {
        let form = $(this);
        slug=$(this).attr('id').split("-")[1]
        author=$(this).attr('id').split("-")[2]
        $.ajax({
            url:"/shop/add_comment_ajax",
            data: form.serialize() + "&book=" + slug,
            method: "POST",
            success: function (data) {
                console.log(data['id']);
                console.log(data['text']);
                console.log(data['date']);
                console.log(author);
                console.log(data['likes']);

                let divcom = document.createElement('div')
                    divcom.id = `block-comment-${data['id']}`

                const h4textcom = document.createElement('h4')
                    h4textcom.textContent = data['text']
//                    h4textcom.id = `comment-text-${data['id']`

                const h5datecom = document.createElement('h5')
                    h5datecom.textContent = data['date']
//                    h5datecom.id = `comment-date-${data['id']`

                const h6authcom = document.createElement('h6')
                    h6authcom.textContent = `Автор комментария: ${author}`
//                    h6authcom.id = `comment-author-${data['id']`

                const h4likecom = document.createElement('h4')
                    h4likecom.classList.add('like-comment')
                    h4likecom.textContent = `Likes: ${data['likes']}`
                    h4likecom.id = `comment-like-${data['id']}`

                const button = document.createElement('button')
                      button.classList.add('btn')
                      button.textContent= ' Delete comment '
                      button.id = `delete-comment-${data['id']}`

                document.body.appendChild(divcom)
                divcom.appendChild(h4textcom)
                divcom.appendChild(h5datecom)
                divcom.appendChild(h6authcom)
                divcom.appendChild(h4likecom)
                divcom.appendChild(button)

                divcom.querySelector('.like-comment').addEventListener('click', function () {
                    let id=$(this).attr('id');
                    $.ajax({
                        url:"/shop/add_like2comment_ajax",
                        data: {"comment_id": id.split('-')[2]},
                        method: "GET",
                        success: function (data) {
                            $(`#${id}`).html(`Likes: ${data['likes']}`);
                        }
                    })
                })

                divcom.querySelector('.btn').addEventListener('click', function () {
                    let id=$(this).attr('id'), id2=`block-comment-${id.split("-")[2]}`;
                    $.ajax({
                        url: "/shop/delete_comment_ajax",
                        data: {"comment_id": id.split("-")[2]},
                        method: "GET",
                        success: function (data) {
                            $(`#${id2}`).remove()
                        }
                    })
                })


            }
        })
        event.target.reset();
        return false;
    });


})
