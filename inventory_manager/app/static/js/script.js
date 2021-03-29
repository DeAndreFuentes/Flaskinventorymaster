function deactivate(product_id) {
    $.ajax({
        url: `/product/${product_id}/remove`,
        type: 'GET',
        data: { product_id: product_id },
        success: res => {
            console.log("deactivated");
            location.reload();
        },
        error: err => console.log(err)
    });
}


function activate(product_id) {
    $.ajax({
        url: `/product/${product_id}/activate`,
        type: 'GET',
        data: { product_id: product_id },
        success: res => {
            console.log("activated");
            location.reload();
        },
        error: err => console.log(err)
    });
}

editProduct = product_id => window.location.href = `/product/${product_id}/edit`;


function init() {
    console.log("Document ready.");

    // E V E N T   L I S T E N E R S
    // $("#btn-edit").click(editProduct)
}

window.onload = init;