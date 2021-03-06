

from flask import request, render_template, redirect

from app.pagination_util.pagination import Pagination, get_page_args, get_page_args_for_reviews
from app.database.db_utils import *
from app.app import app
from app.utils import get_products, get_page_reviews


# INDEX
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


# ADD PRODUCT
@app.route("/product/add", methods=["POST"])
def add_product():
    data = request.form
    create(
        data.get("form-name"),
        data.get("form-price"),
        data.get("form-quantity"),
        data.get("form-description"),
        data.get("form-category")
    )

    return redirect("/")


#ADD REVIEW
@app.route("/review/<product_id>/add", methods=["POST"])
def add_review(product_id):
    data = request.form
    new_review = create_review(
        data.get("form-name"),
        data.get("form-review"),
        product_id
    )
    return redirect("/product/{}".format(product_id))


#ALL PRODUCTS
@app.route("/products")
def all_products():
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page', items_per_page=2)
    search = ''
    if request.args.get("q"):
        search = request.args.get("q")
        out = get_filter_products(search)
    else:
        out = get_all_products()
    pagination_products = get_products(offset=offset, per_page=per_page)
    if bool(out):
        try:
            result = [out[i] for i in pagination_products]
        except IndexError:
            result = [out[i] for i in pagination_products[:pagination_products.index(len(out) - 1) + 1]]
    else:
        result = []
    pagination = Pagination(page=page, per_page=per_page, total=len(out), css_framework='bootstrap4')
    return render_template("all_products.html", products=result, pagination=pagination,
                           page=page, per_page=per_page, search=search)


# ONEPRODUCT
@app.route("/product/<product_id>")
def one_product(product_id):
    page, per_page, offset = get_page_args_for_reviews(page_parameter='page',
                                                       per_page_parameter='per_page')
    one_product = get_one_product(product_id)
    out = get_reviews(product_id)
    pagination_reviews = get_page_reviews(offset=offset, per_page=per_page)
    if bool(out):
        try:
            reviews = [out[i] for i in pagination_reviews]
        except IndexError:
            reviews = [out[i] for i in pagination_reviews[:pagination_reviews.index(len(out) - 1) + 1]]
    else:
        reviews = []
    pagination = Pagination(page=page, per_page=per_page, total=len(out), css_framework='bootstrap4')
    return render_template("one_product.html", one_product=one_product, reviews=reviews,
                           pagination=pagination,
                           page=page, per_page=per_page)


# EDIT PRODUCT
@app.route("/product/<product_id>/edit")
def edit_product(product_id):
    one_product = get_one_product(product_id)
    return render_template("edit_product.html", one_product=one_product)


# UPDATE PRODUCT
@app.route("/product/<product_id>/update", methods=["POST"])
def update_product(product_id):
    data = request.form
    update_one_product(product_id, data)
    return redirect("/product/{}".format(product_id))


# DELETE PRODUCT
@app.route("/product/<product_id>/remove", methods=["GET"])
def remove_product(product_id):
    delete_product(product_id)
    q = ''
    if request.args.get("q"):
        q = request.args.get("q")
    return redirect("/products?q={}".format(q))


# INACTIVE PRODUCTS
@app.route("/products/inactive")
def inactive_products():
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    search = ''
    if request.args.get("q"):
        search = request.args.get("q")
        out = get_in_filter_products(search)
    else:
        out = get_inactive_products()
    pagination_products = get_products(offset=offset, per_page=per_page)
    if bool(out):
        try:
            result = [out[i] for i in pagination_products]
        except IndexError:
            result = [out[i] for i in pagination_products[:pagination_products.index(len(out) - 1) + 1]]
    else:
        result = []
    pagination = Pagination(page=page, per_page=per_page, total=len(out), css_framework='bootstrap4')
    return render_template("inactive.html", products=result, pagination=pagination,
                           page=page, per_page=per_page, search=search)


# ACTIVATE PRODUCT
@app.route("/product/<product_id>/activate")
def activate_product(product_id):
    set_is_active(product_id)
    q = ''
    if request.args.get("q"):
        q = request.args.get("q")
    return redirect("/products/inactive?q={}".format(q))


#NOTFOUND
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


