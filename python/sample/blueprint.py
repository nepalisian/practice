from flask import Blueprint, render_template

tree_mold = Blueprint('mold', __name__)


@tree_mold.route('/leaves')
def leaves():
    return 'This tree has leaves'


@tree_mold.route('/roots')
def roots():
    return 'This tree has roots'


@tree_mold.route('/rings')
@tree_mold.route('/rings/<year>')
def rings(year=10):
    return 'This tree is %s years old' % year

@tree_mold.route('/hello')
@tree_mold.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@tree_mold.route('/test')
def test():
    return render_template('bootstrap.html')