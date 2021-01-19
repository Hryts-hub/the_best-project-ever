$('document').ready(function () {
    $('.like-comment').on('click', function () {
        let id=$(this).attr('id');
        $.ajax({
            url:"/shop/add_like2comment_ajax",
            data: {"comment_id": id.split('-')[1]},
            method: "GET",
            success: function (data) {
                $(`#${id}`).html(`Likes: ${data['likes']}`);
            }
        })
    });

    $('.delete-comment').on('click', function () {
        let id=$(this).attr('id'), id2=`block-comment-${id.split("-")[2]}`;
        $.ajax({
            url: "/shop/delete_comment_ajax",
            data: {"comment_id": id.split("-")[2]},
            method: "GET",
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
            id7=`voice-${id.split("-")[1]}`,
            id8='check-star',
            id9='dark-star';
        console.log(id)
        $.ajax({
            url:"/shop/rate_ajax",
            data: {"slug": id.split("-")[1], "rate": id.split("-")[2]},
            method: "GET",
            success: function (data) {
                console.log(data['rate']);

                $(`#${id6}`).html(data['rate']);
                $(`#${id7}`).html(`Число голосов: ${data['count_rated_users']}`);
                var
                    dark = document.getElementById(id9).innerHTML,
                    check = document.getElementById(id8).innerHTML;

                for (let i=1; i<6; i++) {
                    if (data['rate'] >= i) {
                        document.getElementById(`star-${id.split("-")[1]}-${i}`).innerHTML = check;
                    }
                    else {
                        document.getElementById(`star-${id.split("-")[1]}-${i}`).innerHTML = dark;
                    }
                }

            }
        })
    });
})
