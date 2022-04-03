<template>
{{id}}
<div class="product-grid2">
    <div class="product-image2">
        <a href="#">
            <img class="pic-1" alt="no_image" :src="movie.image">
            <img class="pic-2" alt="no_image" :src="movie.image">
        </a>
        <ul class="social">
            <li><a href="#" data-tip="like"><i class="fa fa-eye"></i></a></li>
            <li><a href="#" data-tip="Add to Wishlist"><i class="fa fa-shopping-bag"></i></a></li>
        </ul>
        <a class="add-to-cart" href="">
            <router-link  :to="{ name: 'Film', params: { id: movie._id}}">
                quick view
            </router-link>
        </a>
    </div>
    <div class="product-content">
        <h3 class="title"><a href="#">{{movie.title}}</a></h3>
        <span class="price">{{movie.genres}}</span>
    </div>
</div>
</template>

<script>
export default {
    components: {},
    name: 'Film',
    props: ['movie'],
    data() {
        return {
            showDialog: false,
        }
    },
    mounted() {
    },
    methods: {
        goToFilm() {
            let url = '/film/';
            this.$router.push(url);
        }
    }
}
</script>

<style scoped>
.demo {
    padding: 45px 0
}

.product-grid2 {
    font-family: 'Open Sans', sans-serif;
    position: relative
}

.product-grid2 .product-image2 {
    overflow: hidden;
    position: relative
}

.product-grid2 .product-image2 a {
    display: block
}

.product-grid2 .product-image2 img {
    width: 100%;
    height: auto
}

.product-image2 .pic-1 {
    opacity: 1;
    transition: all .5s;
    max-width: 100%;
    height: auto;
}

.product-grid2:hover .product-image2 .pic-1 {
    opacity: 0
}

.product-image2 .pic-2 {
    width: 100%;
    height: 100%;
    max-width: 100%;
    height: auto;
    opacity: 0;
    top: 0;
    left: 0;
    position: absolute;
    transition: all .5s
}

.product-grid2:hover .product-image2 .pic-2 {
    opacity: 1
}

.product-grid2 .social {
    padding: 0;
    margin: 0;
    position: absolute;
    bottom: 50px;
    right: 25px;
    z-index: 1
}

.product-grid2 .social li {
    margin: 0 0 10px;
    display: block;
    transform: translateX(100px);
    transition: all .5s
}

.product-grid2:hover .social li {
    transform: translateX(0)
}

.product-grid2:hover .social li:nth-child(2) {
    transition-delay: .15s
}

.product-grid2:hover .social li:nth-child(3) {
    transition-delay: .25s
}

.product-grid2 .social li a {
    color: #505050;
    background-color: #fff;
    font-size: 17px;
    line-height: 45px;
    text-align: center;
    height: 45px;
    width: 45px;
    border-radius: 50%;
    display: block;
    transition: all .3s ease 0s
}

.product-grid2 .social li a:hover {
    color: #fff;
    background-color: #3498db;
    box-shadow: 0 0 10px rgba(0, 0, 0, .5)
}

.product-grid2 .social li a:after,
.product-grid2 .social li a:before {
    content: attr(data-tip);
    color: #fff;
    background-color: #000;
    font-size: 12px;
    line-height: 22px;
    border-radius: 3px;
    padding: 0 5px;
    white-space: nowrap;
    opacity: 0;
    transform: translateX(-50%);
    position: absolute;
    left: 50%;
    top: -30px
}

.product-grid2 .social li a:after {
    content: '';
    height: 15px;
    width: 15px;
    border-radius: 0;
    transform: translateX(-50%) rotate(45deg);
    top: -22px;
    z-index: -1
}

.product-grid2 .social li a:hover:after,
.product-grid2 .social li a:hover:before {
    opacity: 1
}

.product-grid2 .add-to-cart {
    color: #fff;
    background-color: #404040;
    font-size: 15px;
    text-align: center;
    width: 100%;
    padding: 10px 0;
    display: block;
    position: absolute;
    left: 0;
    bottom: -100%;
    transition: all .3s
}

.product-grid2 .add-to-cart:hover {
    background-color: #3498db;
    text-decoration: none
}

.product-grid2:hover .add-to-cart {
    bottom: 0
}

.product-grid2 .product-new-label {
    background-color: #3498db;
    color: #fff;
    font-size: 17px;
    padding: 5px 10px;
    position: absolute;
    right: 0;
    top: 0;
    transition: all .3s
}

.product-grid2:hover .product-new-label {
    opacity: 0
}

.product-grid2 .product-content {
    padding: 20px 10px;
    text-align: center
}

.product-grid2 .title {
    font-size: 17px;
    margin: 0 0 7px
}

.product-grid2 .title a {
    color: #303030
}

.product-grid2 .title a:hover {
    color: #3498db
}

.product-grid2 .price {
    color: #303030;
    font-size: 15px
}

@media screen and (max-width:990px) {
    .product-grid2 {
        margin-bottom: 30px
    }
}

.grid {
    overflow: hidden;
    margin-top: 120px;
    margin-left: 100px;
    z-index: -1;
    display: flex;
    flex-wrap: wrap;
    justify-content: center start;

    width: 100%;

}

.v-card {
    width: 300px;
    height: 500px;
    ;
    position: relative;

}

.card-text {
    color: rgba(var(--v-theme-on-surface), var(--v-medium-emphasis-opacity));
    font-size: 0.875rem;
    font-weight: 400;
    letter-spacing: 0.0178571429em;
    padding: 1rem;
    text-transform: none;
    transition: inherit;
    transition-property: color, opacity;
}

.v-card-title {}

.v-img {
    margin: 0;
    padding: 0;
    width: 100%;
    height: auto;
}

.v-img:hover {
    cursor: pointer;
}
</style>
