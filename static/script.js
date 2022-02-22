$('button.stone-btn').on('click', function(){
    var $button = $(this)
    var $product_id = $(this).data('id')
    var $mkv = $(this).data('mkv')
    $.ajax({
        url:'/cart-create/',
        type:'GET',
        data:{
            'product_id':$product_id,
            'mkv':$mkv
        },
        success:function(response){
            if(response['data']==='created'){
                $button.css('background-color','#000')
            }
        }
    })
})

$('input.mkv').on('keyup',function(){
    var $all_price = $('b.all')
    var $price = $(this).next().next().children()
    var $mkv = $(this)
    $.ajax({
        url:'/cart-update/',
        type:'GET',
        data:{
            'mkv':$mkv.val(),
            'cart_id':$mkv.data('id')
        },
        success:function(response){
            $price.html(response['price'])
            $all_price.html(response['main_price'])
        }
    })
})

$('button.delete').on('click',function(){
    $(this).parent().parent().parent().hide()
    var $all_price = $('b.all')
    var $cart = $(this).data('id')
    $.ajax({
        url:'/cart-delete/',
        type:'GET',
        data:{
            'cart_id':$cart
        },
        success:function(response){
            $all_price.html(response['main_price'])
        }
    })
})

const burger = document.getElementById('burger')
const menu = document.getElementById('ul')

burger.addEventListener('click', () => {
    menu.classList.toggle('show')
})


const search = document.querySelector(".search-btn")
const background = document.querySelector('.white')
const clear = document.querySelector(".clear-btn")

search.addEventListener('click', () => {
    background.classList.add('wash')
})

clear.addEventListener('click', () => {
    background.classList.remove('wash')
})

const filter = document.querySelector(".catalog-btn")
const unhiddenItem = document.querySelector(".catalog-hid")

filter.addEventListener('click', () => {
    unhiddenItem.classList.toggle('showes')
})



