from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
        'id': 1,
        'title': 'Carnaval',
        'author': 'Manuel Bandeira'
    },

    {
        'id': 2,
        'title': 'Mensagem',
        'author': 'Fernando Pessoa'
    },

    {
        'id': 3,
        'title': 'Os Lusíadas',
        'author': 'Luiz Vaz de Camões'
    },


     {
        'id': 4,
        'title': 'Primeiros Cantos',
        'author': 'Gonçalves Dias'
    },

     {
        'id': 5,
        'title': 'Balada do Cárcere',
        'author': 'Bruno Tolentino'
    },

]

@app.route('/books',methods=['POST'])
def include_new_book():
    new_book = request.get_json()
    books.append(new_book)

    return jsonify(books)

@app.route('/books',methods=['GET'])
def get_books():
    return jsonify(books)


@app.route('/books/<int:id>',methods=['GET'])
def get_book_by_id(id):
    for book in books:
        if book.get('id') == id:
            return jsonify(book)

@app.route('/books/<int:id>',methods=['PUT'])       
def edit_book_by_id(id):
    modified_book = request.get_json()
    for index,book in enumerate(books):
        if book.get('id') == id:
            books[index].update(modified_book)
            return jsonify(books[index])


@app.route('/books/<int:id>',methods=['DELETE'])
def delete_books(id):
    for index,book in enumerate(books):
        if book.get('id') == id:
            del books[index]
    
    return jsonify(books)


app.run(port=5000,host='localhost',debug=True)


