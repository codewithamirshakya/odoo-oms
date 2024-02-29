from odoo import models, fields

class Book(models.Model):
    _name = 'my.book'
    _description = 'Book Model'

    name = fields.Char(string='Book Title')
    author_ids = fields.Many2many(
        comodel_name='my.author', 
        relation='test', 
        column1='book_id', 
        column2='author_id', 
        string='Authors'
    )

class Author(models.Model):
    _name = 'my.author'
    _description = 'Author Model'

    name = fields.Char(string='Author Name')


class BookAuthorRel(models.Model):
    _name = 'my.book_author_rel'
    _description = 'Book Author Relationship Model'

    book_id = fields.Many2one('my.book', string='Book', ondelete='cascade')
    author_id = fields.Many2one('my.author', string='Author', ondelete='cascade')
    contribution_percentage = fields.Float(string='Contribution Percentage')
    notes = fields.Text(string='Notes')

