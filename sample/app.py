from flask import Blueprint, render_template

tree_mold = Blueprint('mold', __name__)


@tree_mold.route('/leaves')
def leaves():
    return 'This tree has leaves'


@tree_mold.route('/roots')
def roots():
    return 'This tree has roots'


@tree_mold.route('/rings')
@tree_mold.route('/rings/<int:year>')
def rings(year=None):
    return 'This tree is %s years old' % year


@tree_mold.route('/hello')
@tree_mold.route('/hello/<string:name>')
def hello(name=None):
    return render_template('hello.html', name=name)

